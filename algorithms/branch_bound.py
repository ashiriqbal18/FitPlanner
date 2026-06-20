def branch_and_bound(
    exercises,
    index,
    current_plan,
    current_time,
    current_calories,
    time_limit,
    best_plan,
):
    """Select the highest-calorie exercise combination that fits the time limit.

    The function uses a simple optimistic upper bound: the current calories plus
    every remaining exercise calorie. If that cannot beat the best solution, the
    branch is pruned.
    """
    if current_time > time_limit:
        return

    current_is_better = current_calories > best_plan[0]["calories"]
    current_tie_uses_time_better = (
        current_calories == best_plan[0]["calories"]
        and current_time > best_plan[0].get("time", 0)
    )
    if current_is_better or current_tie_uses_time_better:
        best_plan[0] = {
            "plan": current_plan[:],
            "calories": current_calories,
            "time": current_time,
        }

    if index >= len(exercises):
        return

    remaining_potential = sum(ex["calories"] for ex in exercises[index:])
    if current_calories + remaining_potential < best_plan[0]["calories"]:
        return

    exercise = exercises[index]

    # Include this exercise.
    current_plan.append(exercise)
    branch_and_bound(
        exercises,
        index + 1,
        current_plan,
        current_time + exercise["time"],
        current_calories + exercise["calories"],
        time_limit,
        best_plan,
    )
    current_plan.pop()

    # Skip this exercise.
    branch_and_bound(
        exercises,
        index + 1,
        current_plan,
        current_time,
        current_calories,
        time_limit,
        best_plan,
    )
