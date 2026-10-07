import sqlite3

from database import get_connection


def create_student(name, age, email, course):
    """Create a new student record."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO students (name, age, email, course)
                VALUES (?, ?, ?, ?)
                """,
                (name, age, email, course)
            )

            connection.commit()
            return True, "Student added successfully."

    except sqlite3.IntegrityError:
        return False, "A student with this email already exists."

    except sqlite3.Error as error:
        return False, f"Database error: {error}"


def get_all_students():
    """Retrieve all student records."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, name, age, email, course
                FROM students
                ORDER BY id
                """
            )

            return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return []


def search_students(keyword):
    """Search students by name, email, or course."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()

            search_pattern = f"%{keyword}%"

            cursor.execute(
                """
                SELECT id, name, age, email, course
                FROM students
                WHERE name LIKE ?
                   OR email LIKE ?
                   OR course LIKE ?
                ORDER BY id
                """,
                (search_pattern, search_pattern, search_pattern)
            )

            return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return []


def get_student_by_id(student_id):
    """Retrieve one student using their ID."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, name, age, email, course
                FROM students
                WHERE id = ?
                """,
                (student_id,)
            )

            return cursor.fetchone()

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return None


def update_student(student_id, name, age, email, course):
    """Update an existing student record."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE students
                SET name = ?, age = ?, email = ?, course = ?
                WHERE id = ?
                """,
                (name, age, email, course, student_id)
            )

            if cursor.rowcount == 0:
                return False, "Student not found."

            connection.commit()
            return True, "Student updated successfully."

    except sqlite3.IntegrityError:
        return False, "A student with this email already exists."

    except sqlite3.Error as error:
        return False, f"Database error: {error}"


def delete_student(student_id):
    """Delete a student record."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM students
                WHERE id = ?
                """,
                (student_id,)
            )

            if cursor.rowcount == 0:
                return False, "Student not found."

            connection.commit()
            return True, "Student deleted successfully."

    except sqlite3.Error as error:
        return False, f"Database error: {error}"