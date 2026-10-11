"""Core calculations for the Student Performance Management System."""

import math


def _validate_subject(subject: object, index: int) -> tuple[float, float]:
    """Validate a subject entry and return normalized numeric values."""
    if not isinstance(subject, tuple) or len(subject) != 2:
        raise ValueError(f"Subject {index} must be a (credits, grade_points) tuple.")

    credits, grade_points = subject

    if (
        isinstance(credits, bool)
        or not isinstance(credits, (int, float))
        or not math.isfinite(credits)
        or credits <= 0
    ):
        raise ValueError("Credits must be positive and finite.")

    if (
        isinstance(grade_points, bool)
        or not isinstance(grade_points, (int, float))
        or not math.isfinite(grade_points)
        or not 0 <= grade_points <= 10
    ):
        raise ValueError("Grade points must be between 0 and 10.")

    return float(credits), float(grade_points)


def validate_student(roll_no: str, name: str) -> None:
    """Validate a student's roll number and name."""
    if not isinstance(roll_no, str) or not roll_no.strip():
        raise ValueError("Roll number cannot be empty.")

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name cannot be empty.")


def calculate_sgpa(subjects: list[tuple[float, float]]) -> float:
    """Calculate SGPA using (credits, grade points) for each subject."""
    if not isinstance(subjects, (list, tuple)) or not subjects:
        raise ValueError("At least one subject is required.")

    normalized_subjects = [
        _validate_subject(subject, index) for index, subject in enumerate(subjects)
    ]

    total_credits = sum(credits for credits, _ in normalized_subjects)
    weighted_points = sum(
        credits * grade_points for credits, grade_points in normalized_subjects
    )

    return round(weighted_points / total_credits, 2)


def calculate_cgpa(
    semesters: list[list[tuple[float, float]]],
) -> float:
    """Calculate cumulative GPA across all semesters."""
    if not isinstance(semesters, (list, tuple)) or not semesters:
        raise ValueError("At least one semester is required.")

    all_subjects: list[tuple[float, float]] = []

    for semester_index, semester in enumerate(semesters):
        if not isinstance(semester, (list, tuple)):
            raise ValueError(
                f"Semester {semester_index} must be a list or tuple of subjects."
            )

        for subject_index, subject in enumerate(semester):
            all_subjects.append(_validate_subject(subject, subject_index))

    if not all_subjects:
        raise ValueError("At least one subject is required.")

    return calculate_sgpa(all_subjects)


def performance_category(cgpa: float) -> str:
    """Return a simple performance category for a CGPA."""
    if (
        isinstance(cgpa, bool)
        or not isinstance(cgpa, (int, float))
        or not math.isfinite(cgpa)
        or not 0 <= cgpa <= 10
    ):
        raise ValueError("CGPA must be between 0 and 10.")

    if cgpa >= 9:
        return "Excellent"
    if cgpa >= 8:
        return "Very Good"
    if cgpa >= 7:
        return "Good"
    if cgpa >= 6:
        return "Satisfactory"
    return "Needs Improvement"
