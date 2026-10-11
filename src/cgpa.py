"""Core calculations for the Student Performance Management System."""

import math


def validate_student(roll_no: str, name: str) -> None:
    """Validate a student's roll number and name."""
    if not isinstance(roll_no, str) or not roll_no.strip():
        raise ValueError("Roll number cannot be empty.")

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name cannot be empty.")


def calculate_sgpa(subjects: list[tuple[float, float]]) -> float:
    """Calculate SGPA using (credits, grade points) for each subject."""
    if not subjects:
        raise ValueError("At least one subject is required.")

    total_credits = 0.0
    weighted_points = 0.0

    for credits, grade_points in subjects:
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

        total_credits += credits
        weighted_points += credits * grade_points

    return round(weighted_points / total_credits, 2)


def calculate_cgpa(
    semesters: list[list[tuple[float, float]]],
) -> float:
    """Calculate cumulative GPA across all semesters."""
    if not semesters:
        raise ValueError("At least one semester is required.")

    all_subjects = [
        subject
        for semester in semesters
        for subject in semester
    ]

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