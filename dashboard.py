"""Dashboard window for summary stats and category breakdown."""


import tkinter as tk
from tkinter import ttk


class DashboardWindow(tk.Toplevel):
    """Dashboard summary for expenses."""

    def __init__(self, master, repo):
        super().__init__(master)
        self.title("Expense Dashboard")
        self.repo = repo
        self._build_ui()
        self.refresh()

    def _build_ui(self):
        self.total_label = tk.Label(self, text="Total Spent: $0.00", font=("Arial", 12, "bold"))
        self.count_label = tk.Label(self, text="Number of Expenses: 0")
        self.avg_label = tk.Label(self, text="Average Expense: $0.00")

        self.total_label.pack(pady=4)
        self.count_label.pack(pady=4)
        self.avg_label.pack(pady=4)

        tk.Label(self, text="Spending by Category:", font=("Arial", 11, "bold")).pack(pady=4)
        self.cat_tree = ttk.Treeview(self, columns=("cat", "total"), show="headings", height=6)
        self.cat_tree.heading("cat", text="Category")
        self.cat_tree.heading("total", text="Total Spent")
        self.cat_tree.pack(padx=10, pady=4)

        tk.Label(self, text="Top 5 Expenses:", font=("Arial", 11, "bold")).pack(pady=4)
        self.top_tree = ttk.Treeview(
            self,
            columns=("date", "category", "description", "amount"),
            show="headings",
            height=5,
        )
        for col in ("date", "category", "description", "amount"):
            self.top_tree.heading(col, text=col.capitalize())

        self.top_tree.pack(padx=10, pady=4)

    def refresh(self):
        total, count, avg = self.repo.get_summary_stats()
        self.total_label.config(text=f"Total Spent: ${total:.2f}")
        self.count_label.config(text=f"Number of Expenses: {count}")
        self.avg_label.config(text=f"Average Expense: ${avg:.2f}")

        for row in self.cat_tree.get_children():
            self.cat_tree.delete(row)
        for cat, t in self.repo.get_totals_by_category():
            self.cat_tree.insert("", "end", values=(cat, f"${t:.2f}"))

        for row in self.top_tree.get_children():
            self.top_tree.delete(row)
        for date, cat, desc, amount in self.repo.get_top_expenses():
            self.top_tree.insert("", "end", values=(date, cat, desc, f"${amount:.2f}"))
