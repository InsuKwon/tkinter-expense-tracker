"""Main Tkinter application for the expense tracker."""

import tkinter as tk
from tkinter import ttk, messagebox

from repository import ExpenseRepository
from forms import ExpenseForm
from dashboard import DashboardWindow


class ExpenseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker")
        self.geometry("800x400")

        self.repo = ExpenseRepository()
        self._build_menu()
        self._build_table()
        self.refresh()

    def _build_menu(self):
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Dashboard", command=self.open_dashboard)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

    def _build_table(self):
        toolbar = tk.Frame(self)
        toolbar.pack(fill="x", pady=5)

        tk.Button(toolbar, text="Add", command=self.add).pack(side="left", padx=3)
        tk.Button(toolbar, text="Edit", command=self.edit).pack(side="left", padx=3)
        tk.Button(toolbar, text="Delete", command=self.delete).pack(side="left", padx=3)
        tk.Button(toolbar, text="Dashboard", command=self.open_dashboard).pack(side="left", padx=3)

        cols = ("id", "date", "category", "description", "amount", "payment_method")
        self.tree = ttk.Treeview(self, columns=cols, show="headings")
        for c in cols:
            self.tree.heading(c, text=c.capitalize())

        self.tree.pack(fill="both", expand=True)

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for exp in self.repo.get_all():
            self.tree.insert("", "end", values=exp)

    def selected(self):
        sel = self.tree.selection()
        if not sel:
            return None
        vals = self.tree.item(sel[0], "values")
        return (int(vals[0]), *vals[1:])

    def add(self):
        ExpenseForm(self, self.repo, self.refresh)

    def edit(self):
        exp = self.selected()
        if not exp:
            messagebox.showinfo("No selection", "Select an expense.")
            return
        ExpenseForm(self, self.repo, self.refresh, expense=exp)

    def delete(self):
        exp = self.selected()
        if not exp:
            messagebox.showinfo("No selection", "Select an expense.")
            return
        if messagebox.askyesno("Confirm", "Delete selected?"):
            self.repo.delete(exp[0])
            self.refresh()

    def open_dashboard(self):
        DashboardWindow(self, self.repo)


if __name__ == "__main__":
    ExpenseApp().mainloop()
