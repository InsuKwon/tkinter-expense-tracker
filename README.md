# Tkinter Expense Tracker  
CCT211H5F – Project 2: Persistent Form  

## Group Members  
- Insu Kwon  
- Rooney 

---

## Project Description

This project is a **Persistent Form Application** built using Python's Tkinter GUI toolkit. The application is an **Expense Tracker** that allows users to manage their personal finances through a graphical interface with full CRUD (Create, Read, Update, Delete) functionality.

### Rubric Requirements Met

| Requirement | Implementation |
|-------------|----------------|
| **Tkinter GUI** | Multi-window interface with main window, form dialogs, and dashboard |
| **CRUD Functionality** | Full Create, Read, Update, Delete operations for expenses |
| **Data Persistence** | SQLite database (`expenses.db`) for permanent storage |
| **Form Validation** | Date format, required fields, and numeric amount validation |
| **Multi-Window Design** | Main window, ExpenseForm (Toplevel), DashboardWindow (Toplevel) |
| **User Experience** | Dropdown menus (Combobox) for Category and Payment Method |
| **Data Visualization** | Charts and graphs in the Analytics dashboard |
| **Error Handling** | Try-catch blocks, user-friendly error messages |

---

## Overview  
This application is a Tkinter-based **expense tracker** built for the final project of **CCT211H5F – Python Programming**.  
It demonstrates:

- CRUD operations  
- SQLite data persistence  
- Multi-window GUI design  
- Error handling and validation  
- Object-oriented code organization  
- Dashboard summary using a separate window  
- Data visualization with matplotlib charts

Users can add, edit, delete, and view expenses. The dashboard provides a quick summary of spending patterns with visual analytics.

---

## Features  

### CRUD Expense Management  
- Add new expenses  
- Edit existing entries  
- Delete entries  
- View expenses in a table using `ttk.Treeview`

### Form Input Controls
- **Category Selection**: Dropdown (Combobox) with predefined options:
  - Food, Transport, Shopping, Entertainment, Rent, Other
- **Payment Method Selection**: Dropdown (Combobox) with predefined options:
  - Credit Card, Debit Card, Cash, E-Transfer, Other

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
- **Form window:** add/edit expenses (`forms.py`)  
- **Dashboard window:** summary statistics (`dashboard.py`)  

### Dashboard Summary  
- Total amount spent  
- Number of expenses  
- Average expense  
- Spending by category (Top 5 + Other aggregation)
- Recent activity list (sorted by date)

### Analytics & Visualization
- **Pie Chart**: Spending by category (Top 5 categories + "Other")
- **Bar Chart**: Top spending categories
- **Line Chart**: Monthly spending trend (chronologically ordered)
- **Transaction Volume**: Number of transactions per category  

---

## Project Structure  

/tkinter-expense-tracker
│
├── main.py # Main GUI (treeview, menu, buttons)
├── repository.py # SQLite database CRUD operations
├── forms.py # Add/Edit expense form (Toplevel)
├── dashboard.py # Dashboard summary and category breakdown
├── .gitignore
└── README.md

---

## How to Run  

**Requirements:**  
- Python 3.10+  
- Tkinter (included with Python)  
- SQLite (included with Python)  

````
Run the application:
````

bash
python main.py

Running the program will automatically:
Create expenses.db if it does not exist
Launch the main Tkinter interface 

## Testing

- Manually tested for:
- Valid/invalid date inputs
- Numeric amount and negative amount prevention
- Adding, editing, deleting expenses
- Dashboard accuracy
- Multi-window flow

## Division of Work
Insu:
- SQLite database setup
- CRUD logic (repository.py)
- Data validation
- Code organization and file structure
- Documentation and Git commits

Rooney:
- GUI layout and styling
- Dashboard design
- Visual hierarchy improvements
- User experience enhancements