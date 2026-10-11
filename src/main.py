"""Command-line demonstration of the student CGPA system."""

from src.cgpa import (
    calculate_cgpa,
    calculate_sgpa,
    performance_category,
    validate_student,
)


def main() -> None:
    """Run a sample student performance calculation."""
    roll_no = "MTECH001"
    name = "Rahul Sharma"

    semester_1 = [
        (4, 9),
        (3, 8),
        (3, 9),
        (2, 8),
    ]

    semester_2 = [
        (4, 8),
        (3, 9),
        (3, 8),
        (2, 9),
    ]

    validate_student(roll_no, name)

    sgpa_1 = calculate_sgpa(semester_1)
    sgpa_2 = calculate_sgpa(semester_2)
    cgpa = calculate_cgpa([semester_1, semester_2])
    category = performance_category(cgpa)

    print("\nSTUDENT CGPA PERFORMANCE REPORT")
    print("-" * 36)
    print(f"Roll Number : {roll_no}")
    print(f"Student Name: {name}")
    print(f"Semester 1 SGPA: {sgpa_1:.2f}")
    print(f"Semester 2 SGPA: {sgpa_2:.2f}")
    print(f"Overall CGPA   : {cgpa:.2f}")
    print(f"Performance    : {category}")


if __name__ == "__main__":
    main()