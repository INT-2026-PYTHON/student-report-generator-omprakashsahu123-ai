"""gradebook.reports — build a printable report from grade records."""
from .stats import average_per_student
from .stats import subjects_offered
from .stats import top_scorer
from .stats import passing_students
def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    averages = average_per_student(records)
    subjects = sorted(subjects_offered(records))
    top_name, top_avg = top_scorer(records)
    passed = passing_students(records)
    lines = []
    lines.append("=== Gradebook Report ===")
    lines.append(f"Total records: {len(records)}")
    lines.append("Subjects offered: " + ", ".join(subjects))
    lines.append("")
    lines.append("Averages:")
    for name in sorted(averages):
        lines.append(
            f"  {name:<8}: {averages[name]}"
        )

    lines.append("")
    lines.append(
        f"Top scorer: {top_name} ({top_avg})"
    )

    lines.append(
        "Passing students (>= 60.0): "
        + ", ".join(passed)
    )

    return "\n".join(lines)




