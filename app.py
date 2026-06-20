from flask import Flask, render_template, request
from algorithms.branch_bound import branch_and_bound
from database.db import get_connection, initialize_database

app = Flask(__name__)
initialize_database()

GOAL_LABELS = {
    "muscle_gain": "Muscle Gain",
    "fat_loss": "Weight Loss",
    "endurance": "Endurance",
}

LEVEL_LABELS = {
    "beginner": "Beginner",
    "intermediate": "Intermediate",
    "advanced": "Advanced",
}

LEVEL_RANK = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
}

EQUIPMENT_LABELS = {
    "bodyweight": "No Equipment",
    "dumbbells": "Dumbbells",
    "pull_up_bar": "Pull-up Bar",
    "gym": "Gym Equipment",
}

EQUIPMENT_COMPATIBILITY = {
    "bodyweight": ["bodyweight"],
    "dumbbells": ["bodyweight", "dumbbells"],
    "pull_up_bar": ["bodyweight", "pull_up_bar"],
    "gym": ["bodyweight", "dumbbells", "pull_up_bar", "gym"],
}


def _title(value: str) -> str:
    return value.replace("_", " ").title()


def _parse_int(value, default, minimum, maximum):
    try:
        number = int(value)
    except (TypeError, ValueError):
        number = default
    return max(minimum, min(maximum, number))


def get_exercises(goal: str, level: str, equipment: str):
    """Fetch matching exercises and normalize database rows for the algorithms/templates."""
    allowed_rank = LEVEL_RANK.get(level, 1)
    allowed_levels = [name for name, rank in LEVEL_RANK.items() if rank <= allowed_rank]
    allowed_equipment = EQUIPMENT_COMPATIBILITY.get(equipment, ["bodyweight"])

    level_marks = ",".join("?" for _ in allowed_levels)
    equipment_marks = ",".join("?" for _ in allowed_equipment)

    query = f"""
        SELECT *
        FROM exercises
        WHERE goal = ?
          AND level IN ({level_marks})
          AND equipment IN ({equipment_marks})
        ORDER BY calories_per_min DESC, duration_min DESC, name ASC
    """

    conn = get_connection()
    try:
        rows = conn.execute(query, [goal, *allowed_levels, *allowed_equipment]).fetchall()
    finally:
        conn.close()

    exercises = []
    for row in rows:
        duration = int(row["duration_min"])
        calories = round(duration * float(row["calories_per_min"]))
        exercises.append({
            "id": row["id"],
            "name": row["name"],
            "variation": f"{row['sets']} sets • {row['reps']} • {row['rest_sec']}s rest",
            "time": duration,
            "calories": calories,
            "equipment": EQUIPMENT_LABELS.get(row["equipment"], _title(row["equipment"])),
            "muscle_group": _title(row["primary_muscle"]),
            "muscle_groups": row["muscle_groups"],
            "intensity": _title(row["intensity"]),
            "description": row["description"],
        })
    return exercises


def build_weekly_plan(exercises, days, daily_time):
    """Build a day-wise plan while avoiding repeated exercises until the pool is exhausted."""
    daily_plan = {}
    used_ids = set()

    for day in range(1, days + 1):
        available = [ex for ex in exercises if ex["id"] not in used_ids]
        if not any(ex["time"] <= daily_time for ex in available):
            available = exercises[:]
            used_ids.clear()

        best_plan = [{"plan": [], "calories": 0, "time": 0}]
        branch_and_bound(
            available,
            index=0,
            current_plan=[],
            current_time=0,
            current_calories=0,
            time_limit=daily_time,
            best_plan=best_plan,
        )

        plan = best_plan[0]["plan"]
        daily_plan[f"Day {day}"] = plan
        for exercise in plan:
            used_ids.add(exercise["id"])

    return daily_plan


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form")
def form():
    return render_template(
        "form.html",
        goals=GOAL_LABELS,
        levels=LEVEL_LABELS,
        equipment_options=EQUIPMENT_LABELS,
    )


@app.route("/generate", methods=["POST"])
def generate():
    goal = request.form.get("goal", "muscle_gain")
    level = request.form.get("level", "beginner")
    equipment = request.form.get("equipment", "bodyweight")
    daily_time = _parse_int(request.form.get("time"), default=30, minimum=5, maximum=180)
    days = _parse_int(request.form.get("days"), default=3, minimum=1, maximum=7)

    exercises = get_exercises(goal, level, equipment)
    exercises = [exercise for exercise in exercises if exercise["time"] <= daily_time]

    daily_plan = build_weekly_plan(exercises, days, daily_time) if exercises else {
        f"Day {day}": [] for day in range(1, days + 1)
    }

    total_calories = sum(ex["calories"] for day in daily_plan.values() for ex in day)
    total_time = sum(ex["time"] for day in daily_plan.values() for ex in day)
    total_exercises = sum(len(day) for day in daily_plan.values())

    status_message = None
    if not exercises:
        status_message = "No exercises matched these filters and time limit. Try increasing time or choosing more equipment."

    return render_template(
        "result.html",
        daily_plan=daily_plan,
        goal=GOAL_LABELS.get(goal, _title(goal)),
        level=LEVEL_LABELS.get(level, _title(level)),
        equipment=EQUIPMENT_LABELS.get(equipment, _title(equipment)),
        days=days,
        calories=total_calories,
        daily_time=daily_time,
        weekly_time=daily_time * days,
        planned_time=total_time,
        total_exercises=total_exercises,
        status_message=status_message,
    )


if __name__ == "__main__":
    app.run(debug=True)
