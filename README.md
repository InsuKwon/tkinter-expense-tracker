# Tkinter Expense Tracker  
CCT211H5F – Project 2: Persistent Form  

## Group Members  
- Insu Kwon  
- Rooney 

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
- **Matplotlib analytics** for visual spending insights

Users can add, edit, delete, and view expenses. The dashboard provides a quick summary of spending patterns.

### Key Technologies
- **Tkinter GUI** - Modern, multi-window interface with ttk widgets
- **SQLite Persistence** - Automatic database creation and management
- **Matplotlib Analytics** - Interactive charts including pie charts and trend graphs

---

## Features  

### CRUD Expense Management  
- Add new expenses  
- Edit existing entries  
- Delete entries  
- View expenses in a table using `ttk.Treeview`

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
- Spending by category (pie chart with top 5 + "Other")
- Monthly spending trends (chronological chart)
- Recent activity list (sorted by date)  

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
- Matplotlib (`pip install matplotlib`)  

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