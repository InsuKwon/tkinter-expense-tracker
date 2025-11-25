import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ExpenseForm(tk.Toplevel):
    """Form window for adding or editing an expense."""

    def __init__(self, master, repo, on_save, expense=None):
        super().__init__(master)
        self.title("Expense Form")
        self.repo = repo
        self.on_save = on_save
        self.expense = expense

        self._build_widgets()
        self._populate_fields()

        self.grab_set()
        self.focus()

    def _build_widgets(self):
        self.resizable(False, False)

        tk.Label(self, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(self, text="Category:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Label(self, text="Description / Notes:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
        tk.Label(self, text="Amount:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        tk.Label(self, text="Payment Method:").grid(row=4, column=0, sticky="e", padx=5, pady=5)

        self.date_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.payment_var = tk.StringVar()

        tk.Entry(self, textvariable=self.date_var).grid(row=0, column=1, padx=5, pady=5)
        tk.Entry(self, textvariable=self.category_var).grid(row=1, column=1, padx=5, pady=5)

        self.desc_text = tk.Text(self, width=30, height=4)
        self.desc_text.grid(row=2, column=1, padx=5, pady=5)

        tk.Entry(self, textvariable=self.amount_var).grid(row=3, column=1, padx=5, pady=5)
        tk.Entry(self, textvariable=self.payment_var).grid(row=4, column=1, padx=5, pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

        tk.Button(btn_frame, text="Save", command=self._on_save).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.destroy).pack(side="left", padx=5)

    def _populate_fields(self):
        if self.expense:
            _, date, category, description, amount, payment = self.expense
            self.date_var.set(date)
            self.category_var.set(category)
            self.desc_text.insert("1.0", description or "")
            self.amount_var.set(str(amount))
            self.payment_var.set(payment or "")
        else:
            self.date_var.set(datetime.today().strftime("%Y-%m-%d"))

    def _on_save(self):
        date = self.date_var.get().strip()
        category = self.category_var.get().strip()
        description = self.desc_text.get("1.0", "end").strip()
        amount_str = self.amount_var.get().strip()
        payment = self.payment_var.get().strip()

        if not date or not category or not amount_str:
            messagebox.showerror("Error", "Date, category, and amount are required.")
            return

        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Error", "Amount must be numeric.")
            return

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format.")
            return

        if self.expense:
            self.repo.update(self.expense[0], date, category, description, amount, payment)
        else:
            self.repo.insert(date, category, description, amount, payment)

        self.on_save()
        self.destroy()
