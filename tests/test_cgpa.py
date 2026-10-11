"""Tests for the Student CGPA Performance Management System."""

import pytest

from src.cgpa import (
    calculate_cgpa,
    calculate_sgpa,
    performance_category,
    validate_student,
)


def test_calculate_sgpa():
    subjects = [(4, 9), (3, 8), (3, 7)]
    assert calculate_sgpa(subjects) == 8.1


def test_calculate_sgpa_with_equal_grade_points():
    subjects = [(4, 8), (2, 8)]
    assert calculate_sgpa(subjects) == 8.0


def test_calculate_cgpa_across_semesters():
    semester_1 = [(4, 9), (4, 8)]
    semester_2 = [(2, 7), (2, 9)]

    assert calculate_cgpa([semester_1, semester_2]) == 8.25


def test_reject_empty_subjects():
    with pytest.raises(ValueError):
        calculate_sgpa([])


def test_reject_zero_credits():
    with pytest.raises(ValueError):
        calculate_sgpa([(0, 8)])


def test_reject_invalid_grade_points():
    with pytest.raises(ValueError):
        calculate_sgpa([(3, 11)])


def test_reject_nan_grade_points():
    with pytest.raises(ValueError):
        calculate_sgpa([(3, float("nan"))])


def test_reject_empty_student_name():
    with pytest.raises(ValueError):
        validate_student("MTECH001", " ")


def test_performance_category():
    assert performance_category(9.2) == "Excellent"
    assert performance_category(8.5) == "Very Good"
    assert performance_category(7.2) == "Good"
    assert performance_category(6.3) == "Satisfactory"
    assert performance_category(5.5) == "Needs Improvement"