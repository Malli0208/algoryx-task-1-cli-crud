import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data/students.db")


def get_connection():
    """Create and return a database connection."""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    """Create the students table if it does not already exist."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    course TEXT NOT NULL
                )
            """)

            connection.commit()

    except sqlite3.Error as error:
        print(f"Database initialization error: {error}")