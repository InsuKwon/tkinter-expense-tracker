"""
Create an old-style database to test migration.
"""

import sqlite3
from repository import DB_NAME


def create_old_style_database():
    """Create a database with the old schema (without user_comments and tags)."""
    # Remove existing database
    import os
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create old-style table
    cursor.execute(
        """
        CREATE TABLE expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL,
            payment_method TEXT
        )
        """
    )

    # Add some sample data
    cursor.execute(
        """
        INSERT INTO expenses (date, category, description, amount, payment_method)
        VALUES (?, ?, ?, ?, ?)
        """,
        ("2024-11-25", "Food", "Lunch at restaurant", 25.50, "Credit Card")
    )

    conn.commit()
    conn.close()
    print(f"Created old-style database: {DB_NAME}")


if __name__ == "__main__":
    create_old_style_database()