def backtrack(exercises, index, current_plan, current_time, time_limit, best_plan):
    """Explore all valid workout combinations and keep the largest valid plan."""
    if current_time > time_limit:
        return

    if len(current_plan) > len(best_plan[0]):
        best_plan[0] = current_plan[:]

    for i in range(index, len(exercises)):
        exercise = exercises[i]
        current_plan.append(exercise)
        backtrack(
            exercises,
            i + 1,
            current_plan,
            current_time + exercise["time"],
            time_limit,
            best_plan,
        )
        current_plan.pop()
