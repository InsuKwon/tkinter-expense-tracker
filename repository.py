"""Database access layer for the expense tracker (SQLite + CRUD)."""

import sqlite3

DB_NAME = "expenses.db"


class ExpenseRepository:
    """Handles all database operations for expenses."""

    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self._create_table()

    def _get_conn(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    amount REAL NOT NULL,
                    payment_method TEXT,
                    user_comments TEXT,
                    tags TEXT
                )
                """
            )
            conn.commit()
            # Ensure new columns exist (for backward compatibility)
            self._ensure_columns_exist(conn)

    # CRUD operations
    def get_all(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            # Check which columns exist to be backward compatible
            cur.execute("PRAGMA table_info(expenses)")
            columns = [column[1] for column in cur.fetchall()]

            # Build query based on available columns
            if 'user_comments' in columns and 'tags' in columns:
                cur.execute(
                    "SELECT id, date, category, description, amount, payment_method, user_comments, tags "
                    "FROM expenses ORDER BY date DESC, id DESC"
                )
                results = cur.fetchall()
            else:
                # Fallback for older databases
                cur.execute(
                    "SELECT id, date, category, description, amount, payment_method "
                    "FROM expenses ORDER BY date DESC, id DESC"
                )
                results = [row + (None, None) for row in cur.fetchall()]  # Add None for missing columns

            return results

    def insert(self, date, category, description, amount, payment_method, user_comments=None, tags=None):
        with self._get_conn() as conn:
            cur = conn.cursor()
            # Ensure columns exist before inserting
            self._ensure_columns_exist(conn)

            cur.execute(
                """
                INSERT INTO expenses (date, category, description, amount, payment_method, user_comments, tags)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (date, category, description, amount, payment_method, user_comments, tags),
            )
            conn.commit()

    def update(self, expense_id, date, category, description, amount, payment_method, user_comments=None, tags=None):
        with self._get_conn() as conn:
            cur = conn.cursor()
            # Ensure columns exist before updating
            self._ensure_columns_exist(conn)

            cur.execute(
                """
                UPDATE expenses
                SET date = ?, category = ?, description = ?, amount = ?, payment_method = ?, user_comments = ?, tags = ?
                WHERE id = ?
                """,
                (date, category, description, amount, payment_method, user_comments, tags, expense_id),
            )
            conn.commit()

    def delete(self, expense_id):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()

    # Dashboard queries
    def get_summary_stats(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT SUM(amount), COUNT(*), AVG(amount) FROM expenses")
            total, count, avg = cur.fetchone()
            return total or 0.0, count or 0, avg or 0.0

    def get_totals_by_category(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT category, SUM(amount)
                FROM expenses
                GROUP BY category
                ORDER BY SUM(amount) DESC
                """
            )
            return cur.fetchall()

    def get_top_expenses(self, limit=5):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT date, category, description, amount
                FROM expenses
                ORDER BY amount DESC
                LIMIT ?
                """,
                (limit,),
            )
            return cur.fetchall()

    def _ensure_columns_exist(self, conn):
        """Ensure that user_comments and tags columns exist (for backward compatibility)."""
        cursor = conn.cursor()
        try:
            # Check current schema
            cursor.execute("PRAGMA table_info(expenses)")
            columns = [column[1] for column in cursor.fetchall()]

            # Add missing columns if needed
            if 'user_comments' not in columns:
                cursor.execute("ALTER TABLE expenses ADD COLUMN user_comments TEXT")
                print("Added user_comments column")

            if 'tags' not in columns:
                cursor.execute("ALTER TABLE expenses ADD COLUMN tags TEXT")
                print("Added tags column")

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error ensuring columns exist: {e}")
            conn.rollback()

    def get_monthly_spending(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT strftime('%Y-%m', date) as month, SUM(amount) as total
                FROM expenses
                GROUP BY month
                ORDER BY month DESC
                LIMIT 12
                """
            )
            return cur.fetchall()

    def get_category_counts(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT category, COUNT(*) as count
                FROM expenses
                GROUP BY category
                ORDER BY count DESC
                """
            )
            return cur.fetchall()

    def get_expenses_by_tag(self, tag):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT date, category, description, amount, user_comments
                FROM expenses
                WHERE tags LIKE ?
                ORDER BY date DESC
                """,
                (f'%{tag}%',)
            )
            return cur.fetchall()

    def get_recent_expenses(self, limit=15):
        """Get the most recent expenses ordered by date (most recent first)."""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT date, category, description, amount
                FROM expenses
                ORDER BY date DESC, id DESC
                LIMIT ?
                """,
                (limit,),
            )
            return cur.fetchall()
