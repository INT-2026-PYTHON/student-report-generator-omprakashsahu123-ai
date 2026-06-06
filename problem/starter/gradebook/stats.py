def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    student_scores = {}
    for record in records:
        name = record["name"]
        score = record["score"]
        student_scores.setdefault(name, []).append(score)

    averages = {}
    for name, scores in student_scores.items():
        averages[name] = round(sum(scores) / len(scores), 2)

    return averages

def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    return {record["subject"] for record in records}

def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    averages = average_per_student(records)
    return max(averages.items(), key=lambda item: item[1])

def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    averages = average_per_student(records)
    passed = [
        name
        for name, avg in averages.items()
        if avg >= threshold
    ]
    return sorted(passed)

