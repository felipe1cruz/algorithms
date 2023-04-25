def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    students = 0
    for time in permanence_period:
        if not isinstance(time[0], int) or not isinstance(time[1], int):
            return None
        if time[0] <= target_time <= time[1]:
            students += 1

    return students
