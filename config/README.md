# Student CGPA Performance Management System

## Overview

A Python project that calculates SGPA and CGPA using
subject credits and grade points.

## Features

- Student input validation
- SGPA calculation
- Cumulative CGPA calculation
- Performance categorization
- Automated unit testing
- AI-assisted development documentation

## Requirements

- Python 3.11+
- Pytest
- Ruff

## Setup

Create and activate a virtual environment, then install
the development tools:

    python -m pip install pytest ruff

## Run

    python -m src.main

## Test

    python -m pytest -v

## Code Quality

    python -m ruff check .
    python -m ruff format --check .

## Project Structure

- src/: application code
- tests/: automated tests
- docs/: engineering journal
- config/: project configuration resources
- .github/: AI repository instructions
- .gitignore
- pyproject.toml

## Limitations

- Uses sample data rather than a database.
- Performance categories are illustrative.
- Official university grading rules must be configured
  before real academic use.

## Responsible AI

AI-generated code is reviewed and tested by the developer.
No passwords, API keys, or real private student records
should be sent to an AI coding assistant.