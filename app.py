from database import initialize_database
from crud import (
    create_student,
    get_all_students,
    get_student_by_id,
    search_students,
    update_student,
    delete_student,
)
from validators import (
    validate_name,
    validate_age,
    validate_email,
    validate_course,
)


def display_header():
    """Display application header."""
    print("\n" + "=" * 50)
    print("          STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)


def display_students(students):
    """Display student records in a readable format."""
    if not students:
        print("\nNo student records found.")
        return

    print("\n" + "-" * 85)
    print(
        f"{'ID':<5}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Email':<30}"
        f"{'Course':<20}"
    )
    print("-" * 85)

    for student in students:
        student_id, name, age, email, course = student

        print(
            f"{student_id:<5}"
            f"{name:<20}"
            f"{age:<8}"
            f"{email:<30}"
            f"{course:<20}"
        )

    print("-" * 85)


def add_student():
    """Handle student creation."""
    print("\n--- ADD STUDENT ---")

    name = input("Enter name: ")
    valid, result = validate_name(name)

    if not valid:
        print(f"Error: {result}")
        return

    name = result

    age = input("Enter age: ")
    valid, result = validate_age(age)

    if not valid:
        print(f"Error: {result}")
        return

    age = result

    email = input("Enter email: ")
    valid, result = validate_email(email)

    if not valid:
        print(f"Error: {result}")
        return

    email = result

    course = input("Enter course: ")
    valid, result = validate_course(course)

    if not valid:
        print(f"Error: {result}")
        return

    course = result

    success, message = create_student(
        name,
        age,
        email,
        course
    )

    print(f"\n{message}")


def view_students():
    """Display all students."""
    print("\n--- ALL STUDENTS ---")

    students = get_all_students()
    display_students(students)


def search_student():
    """Search students."""
    print("\n--- SEARCH STUDENT ---")

    keyword = input("Enter name, email, or course: ").strip()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    students = search_students(keyword)
    display_students(students)


def update_student_record():
    """Handle student update."""
    print("\n--- UPDATE STUDENT ---")

    student_id = input("Enter student ID: ").strip()

    try:
        student_id = int(student_id)
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    student = get_student_by_id(student_id)

    if not student:
        print("Student not found.")
        return

    print("\nCurrent record:")
    display_students([student])

    print("\nEnter the new details.")

    name = input("Enter name: ")
    valid, result = validate_name(name)

    if not valid:
        print(f"Error: {result}")
        return

    name = result

    age = input("Enter age: ")
    valid, result = validate_age(age)

    if not valid:
        print(f"Error: {result}")
        return

    age = result

    email = input("Enter email: ")
    valid, result = validate_email(email)

    if not valid:
        print(f"Error: {result}")
        return

    email = result

    course = input("Enter course: ")
    valid, result = validate_course(course)

    if not valid:
        print(f"Error: {result}")
        return

    course = result

    success, message = update_student(
        student_id,
        name,
        age,
        email,
        course
    )

    print(f"\n{message}")


def delete_student_record():
    """Handle student deletion."""
    print("\n--- DELETE STUDENT ---")

    student_id = input("Enter student ID: ").strip()

    try:
        student_id = int(student_id)
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    student = get_student_by_id(student_id)

    if not student:
        print("Student not found.")
        return

    print("\nStudent to be deleted:")
    display_students([student])

    confirmation = input(
        "\nAre you sure you want to delete this student? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("Deletion cancelled.")
        return

    success, message = delete_student(student_id)

    print(f"\n{message}")


def display_menu():
    """Display the main menu."""
    print("\n")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def main():
    """Run the Student Management System."""
    initialize_database()

    while True:
        display_header()
        display_menu()

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student_record()

        elif choice == "5":
            delete_student_record()

        elif choice == "6":
            print("\nThank you for using Student Management System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()