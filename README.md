# SmartSpend — Personal Expense Tracking System

SmartSpend is a lightweight command-line expense tracking application built in Python.  
It allows users to record, categorize, and analyze personal spending data while maintaining persistent storage using JSON.

The project demonstrates core computer science concepts such as data aggregation, hash-map based summaries, file persistence, and modular software design.

---

## Features

- Add new expense records
- View all recorded expenses
- Filter expenses by category
- Calculate total spending
- Generate category-based spending summaries
- Persistent storage using JSON files
- Simple command-line interface

---

## Technologies Used

- Python
- Hash maps (Python dictionaries)
- File I/O
- JSON data storage
- Modular program structure

---

## Project Structure

```text
SmartSpend/
├── main.py
├── expense_manager.py
├── storage.py
├── expenses.json
└── README.md
```

---

## How It Works

Each expense is stored as a structured record:

```python
{
    "id": 1,
    "amount": 12.50,
    "category": "Food",
    "description": "Lunch",
    "date": "2026-03-16"
}
```

Category summaries are generated using dictionary-based aggregation for efficient spending analysis.

---

## Running the Project

1. Make sure Python is installed on your system.
2. Download or clone the repository.
3. Navigate to the project folder.
4. Run:

```bash
python main.py
```

If your system uses Python 3 explicitly:

```bash
python3 main.py
```

---

## Example Interface

```text
=== SmartSpend Expense Tracker ===
1. Add Expense
2. View All Expenses
3. View Expenses by Category
4. Show Total Spending
5. Show Spending by Category
6. Exit
```

---

## Example Use Cases

- Tracking day-to-day personal spending
- Practicing CRUD-style data management
- Demonstrating hash-map based aggregation
- Learning JSON-based persistence in Python

---

## Future Improvements

- Monthly spending summaries
- Edit and delete expense entries
- CSV export/import support
- Budget alerts by category
- GUI version using Tkinter
- Unit testing with pytest

---

## Author

Anirudh Jha  
Computer Science — San Diego State University
