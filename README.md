# Tkinter Expense Tracker  
CCT211H5F – Project 2: Persistent Form  

## Group Members  
- Insu Kwon  
- Rooney 

---

**Note on AI Assistance (Post-Deadline Work)**  
This repository contains a few GitHub Copilot–tagged commits made *after* the official due date (Nov 25). These were experiments for UI refinement and were not part of the submitted work.  
The project submitted for grading was created and implemented by our group, and all core functionality, code structure, and implementation decisions were done manually before the deadline.


## Overview  
This application is a Tkinter-based **expense tracker** built for the final project of **CCT211H5F – Python Programming**.  
It demonstrates:

- CRUD operations  
- SQLite data persistence  
- Multi-window GUI design  
- Error handling and validation  
- Object-oriented code organization  
- Dashboard with interactive Matplotlib charts
- Dropdown selection for categories and payment methods

Users can add, edit, delete, and view expenses. The dashboard provides comprehensive analytics with pie charts, bar charts, and monthly spending trends.

---

## Features  

### CRUD Expense Management  
- Add new expenses with dropdown category and payment method selection
- Edit existing entries  
- Delete entries  
- View expenses in a table using `ttk.Treeview`

### Category & Payment Selection
- Pre-defined category options: Food, Transport, Shopping, Entertainment, Rent, Other
- Pre-defined payment methods: Cash, Credit Card, Debit Card, Other
- Dropdown selection using `ttk.Combobox` for consistent data entry

### Data Validation  
- Required fields (date, category, amount)  
- Date format validation (`YYYY-MM-DD`)  
- Numeric + positive amount check  
- Optional description limits  

### SQLite Persistence  
- Automatic creation of `expenses.db`  
- Stores all data permanently  
- Database logic isolated in `repository.py`  

### Multi-Window Tkinter Interface  
- **Main window:** view and manage expenses  
- **Form window:** add/edit expenses with dropdowns (`forms.py`)  
- **Dashboard window:** analytics and visualizations (`dashboard.py`)  

### Dashboard Analytics  
- Total amount spent  
- Number of expenses  
- Average expense  
- Top spending category
- Recent activity (last 15 expenses, chronologically sorted)
- Quick insights with spending trend analysis

### Interactive Charts (Matplotlib)
- **Spending by Category (Pie Chart):** Top 5 categories with "Other" aggregation
- **Top Spending Categories (Bar Chart):** Visual comparison of top 5 categories
- **Monthly Spending Trend (Line Chart):** Chronological view (oldest to newest)
- **Transaction Volume (Bar Chart):** Number of transactions per category

---

## Project Structure  

```
/tkinter-expense-tracker
│
├── main.py           # Main GUI (treeview, menu, buttons)
├── repository.py     # SQLite database CRUD operations
├── forms.py          # Add/Edit expense form with Comboboxes
├── dashboard.py      # Dashboard with Matplotlib charts
├── expenses.db       # SQLite database (auto-created)
├── .gitignore
└── README.md
```

---

## How to Run  

**Requirements:**  
- Python 3.10+  
- Tkinter (included with Python)  
- SQLite (included with Python)  
- Matplotlib (`pip install matplotlib`)

```bash
# Install matplotlib if not already installed
pip install matplotlib

# Run the application
python main.py
```

Running the program will automatically:
- Create `expenses.db` if it does not exist
- Launch the main Tkinter interface 

---

## Testing

- Manually tested for:
  - Valid/invalid date inputs
  - Numeric amount and negative amount prevention
  - Adding, editing, deleting expenses
  - Dashboard chart accuracy
  - Dropdown selection functionality
  - Multi-window flow

---

## Division of Work
**Insu:**
- SQLite database setup
- CRUD logic (repository.py)
- Data validation
- Code organization and file structure
- Documentation and Git commits

**Rooney:**
- GUI layout and styling
- Dashboard design with Matplotlib charts
- Visual hierarchy improvements
- User experience enhancements