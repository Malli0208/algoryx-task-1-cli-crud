import re


def validate_name(name):
    """Validate student name."""
    name = name.strip()

    if not name:
        return False, "Name cannot be empty."

    if not re.fullmatch(r"[A-Za-z ]+", name):
        return False, "Name can contain only letters and spaces."

    return True, name


def validate_age(age):
    """Validate student age."""
    try:
        age = int(age)

        if age < 1 or age > 120:
            return False, "Age must be between 1 and 120."

        return True, age

    except ValueError:
        return False, "Age must be a valid number."


def validate_email(email):
    """Validate email address."""
    email = email.strip()

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        return False, "Please enter a valid email address."

    return True, email


def validate_course(course):
    """Validate course name."""
    course = course.strip()

    if not course:
        return False, "Course cannot be empty."

    return True, course