# Tkinter Expense Tracker

A persistent form application for tracking personal expenses built with Python's Tkinter GUI framework and SQLite database.

## Description

This application is a Tkinter-based **expense tracker** that provides a simple and intuitive interface for managing personal finances. It demonstrates persistent data storage, multi-window GUI design, and data visualization capabilities.

Users can add, edit, delete, and view expenses. The dashboard provides comprehensive analytics and visualizations of spending patterns.

## Installation

**Requirements:**
- Python 3.10+
- Tkinter (included with Python)
- SQLite (included with Python)
- Matplotlib (for charts)

**Install dependencies:**
```bash
pip install matplotlib
```

## Execution

Run the application:
```bash
python main.py
```

Running the program will automatically:
- Create `expenses.db` if it does not exist
- Launch the main Tkinter interface

## Features

### Dashboard
- Overview with summary cards (Total Spent, Number of Expenses, Average, Top Category)
- Quick insights and recent activity
- Analytics with charts and visualizations

### CRUD Operations
- Add new expenses with categories and payment methods
- Edit existing entries
- Delete entries
- View expenses in a table using `ttk.Treeview`

### Analytics
- Spending by category (Pie chart - top 5 + Other)
- Monthly spending trends (chronological)
- Category breakdown analysis
- Transaction volume statistics

## Project Structure

```
/tkinter-expense-tracker
├── main.py           # Main GUI (treeview, menu, buttons)
├── repository.py     # SQLite database CRUD operations
├── forms.py          # Add/Edit expense form (Toplevel)
├── dashboard.py      # Dashboard summary and category breakdown
├── .gitignore
└── README.md
```

## Group Members
- Insu Kwon
- Rooney