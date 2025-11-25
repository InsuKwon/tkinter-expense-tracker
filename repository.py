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
                    payment_method TEXT
                )
                """
            )
            conn.commit()

    # CRUD operations
    def get_all(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, date, category, description, amount, payment_method "
                "FROM expenses ORDER BY date DESC, id DESC"
            )
            return cur.fetchall()

    def insert(self, date, category, description, amount, payment_method):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO expenses (date, category, description, amount, payment_method)
                VALUES (?, ?, ?, ?, ?)
                """,
                (date, category, description, amount, payment_method),
            )
            conn.commit()

    def update(self, expense_id, date, category, description, amount, payment_method):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE expenses
                SET date = ?, category = ?, description = ?, amount = ?, payment_method = ?
                WHERE id = ?
                """,
                (date, category, description, amount, payment_method, expense_id),
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
