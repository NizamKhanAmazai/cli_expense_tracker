# Expense Tracker

A command-line expense tracker built with Python.

This project allows you to add, view, search, delete, and analyze expenses directly from an interactive command-line interface.

The project was developed in two versions:

1. **JSON version** — stores expenses directly in a JSON file.
2. **SQLite version** — stores expenses in an SQLite database and can export the stored data to JSON.

The SQLite version is the more recent implementation of the project.

---

## Features

- Add a new expense
- List all expenses
- Delete an expense by ID
- Search expenses
- View all expense categories
- Calculate total expenses
- Calculate average expense
- View expenses grouped by category
- View monthly expense statistics
- Find the highest expense
- Count the total number of expenses
- Run application tests from the CLI
- Store data using JSON
- Store data using SQLite
- Export SQLite data to JSON
- Interactive command-line interface
- `exit` and `quit` commands to close the application

---

# Project Versions

The project contains two implementations.

## Version 1 — JSON Storage

The first version stores all expenses in:

```text
data/expenses.json
```

The `Storage` class reads and writes expense data directly to the JSON file.

The JSON version provides the main expense-management features and demonstrates file handling with Python's built-in `json` module.

---

## Version 2 — SQLite Storage

The second version uses SQLite as the primary storage system.

The database is stored in:

```text
data/expenses.db
```

The SQLite database contains an `expenses` table with the following fields:

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Unique expense ID |
| `amount` | REAL | Expense amount |
| `category` | TEXT | Expense category |
| `description` | TEXT | Description of the expense |
| `date` | TEXT | Date when the expense was added |

The SQLite version also provides a `save_to_json` command that exports the database contents to a JSON file.

---

# Requirements

- Python 3.x
- No third-party Python packages are required.

The project uses Python's standard library, including modules such as:

```text
argparse
shlex
sqlite3
json
datetime
dataclasses
pathlib
unittest
```

A virtual environment is not required for this project.

---

# Project Structure

The project contains two versions.

## JSON Version

```text
expence-tracker_1/
│
├── expense_tracker/
│   ├── __init__.py
│   ├── cli.py
│   ├── models.py
│   ├── service.py
│   ├── statistics.py
│   └── storage.py
│
├── tests/
│   ├── run_test.py
│   └── storage.py
│
├── data/
│   └── expenses.json
│
├── main.py
└── README.md
```

## SQLite Version

```text
expence-tracker_2/
│
├── expense_tracker/
│   ├── __init__.py
│   ├── cli.py
│   ├── db.py
│   ├── models.py
│   ├── service.py
│   ├── statistics.py
│   └── storage.py
│
├── tests/
│   ├── run_test.py
│   └── storage.py
│
├── data/
│   └── expenses.db
│
├── main.py
└── README.md
```

---

# Application Architecture

The application is separated into different modules, with each module having a specific responsibility.

```text
                         main.py
                            │
                            ▼
                          cli.py
                            │
                            ▼
                       service.py
                       /         \
                      /           \
                     ▼             ▼
                models.py      storage.py
                                   │
                         ┌─────────┴─────────┐
                         ▼                   ▼
                       JSON               SQLite
                         │                   │
                         └─────────┬─────────┘
                                   ▼
                            statistics.py
```

### `main.py`

The entry point of the application.

It starts the interactive CLI.

---

### `expense_tracker/__init__.py`

Exposes the main classes and functions of the `expense_tracker` package.

It provides access to:

- `Expense`
- `ExpenseService`
- `Storage`
- `start`
- `start_cmd`

The package also defines the current project version as:

```text
0.1.0
```

---

### `models.py`

Defines the `Expense` data model.

The project uses a Python `dataclass`:

```python
@dataclass
class Expense:
    id: str
    amount: float
    category: str
    description: str
    date: date
```

An expense contains:

- ID
- Amount
- Category
- Description
- Date

---

### `cli.py`

Contains the interactive command-line interface.

The application uses Python's `argparse` module to define the available commands.

It also uses `shlex` so that commands containing quoted text can be entered correctly.

For example:

```text
Expense> add 400 Food "Party with friends"
```

The application continues accepting commands until the user enters:

```text
exit
```

or:

```text
quit
```

---

### `service.py`

Contains the application's main service layer.

The `ExpenseService` class connects the CLI with the storage and statistics functionality.

It handles operations such as:

- Adding expenses
- Listing expenses
- Deleting expenses
- Searching expenses
- Showing categories
- Calculating statistics
- Exporting data to JSON

---

### `storage.py`

Handles persistent expense data.

In the JSON version, it manages:

```text
data/expenses.json
```

In the SQLite version, it manages:

```text
data/expenses.db
```

The SQLite version also provides the functionality to export database records to JSON.

---

### `db.py`

This file exists in the SQLite version.

It initializes the SQLite database and creates the `expenses` table if it does not already exist.

The database table is created with:

```sql
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    date TEXT NOT NULL
)
```

---

### `statistics.py`

Contains functions that calculate expense statistics.

The available calculations include:

- Monthly expenses
- Total expenses
- Average expenses
- Expenses by category
- Highest expense
- Number of expenses

---

### `tests/`

Contains the project's tests.

The tests use Python's built-in `unittest` framework.

The test suite checks storage functionality such as:

- Adding an expense
- Loading expenses
- Deleting an expense
- Listing expenses
- Searching expenses
- Retrieving categories
- Retrieving statistics
- Saving data to JSON

---

# Running the Application

The application starts from `main.py`.

Run:

```bash
python main.py
```

After starting, the application displays a welcome message and provides an interactive prompt:

```text
Expense>
```

Commands are entered directly after this prompt.

For example:

```text
Expense> add 400 Food Party with friends
```

---

# CLI Commands

The application supports the following commands.

| Command | Purpose |
|---|---|
| `add` | Add a new expense |
| `list` | List expenses |
| `delete` | Delete an expense by ID |
| `search` | Search for an expense |
| `categories` | Show available categories |
| `total` | Show total expenses |
| `average` | Show average expense |
| `expense_by_category` | Show expenses grouped by category |
| `m-stats` | Show monthly statistics |
| `max` | Show the highest expense |
| `count` | Show the number of expenses |
| `test` | Run the application tests |
| `save_to_json` | Save/export data to JSON |
| `exit` | Exit the application |
| `quit` | Exit the application |

---

# `add`

Adds a new expense.

### Syntax

```text
Expense> add <amount> <category> <description>
```

### Example

```text
Expense> add 400 Food Party with friends
```

The description can also be enclosed in quotes:

```text
Expense> add 400 Food "Party with friends"
```

The application automatically generates an ID and uses the current date for the expense.

Example output:

```text
Expense added successfully, you can find it • search 1234
```

---

# `list`

Displays the stored expenses.

### Syntax

```text
Expense> list
```

Example:

```text
Expense> list
```

The output contains:

```text
id
amount
category
description
date
```

Example:

```text
| id     | amount       | category                  | description               | date         |
------------------------------------------------------------------------------------------
| 1228   | 500.0        | Good                      | good                      | 2026-09-17   |
```

The description is shortened with `...` when it is longer than the available display width.

---

# `delete`

Deletes an expense using its ID.

### Syntax

```text
Expense> delete <id>
```

### Example

```text
Expense> delete 5
```

If the expense exists, the application reports that the item was deleted.

If the ID does not exist, the application reports:

```text
X • item doesn't exist.
```

---

# `search`

Searches for expenses using a keyword/value.

### Syntax

```text
Expense> search <keyword>
```

### Example

```text
Expense> search Food
```

The search can match:

- Expense ID
- Amount
- Category
- Description

For category and description searches, partial matching is supported.

For example:

```text
Expense> search food
```

can find an expense whose category contains `Food`.

---

# `categories`

Displays the categories currently present in the stored expenses.

### Syntax

```text
Expense> categories
```

Example:

```text
Expense> categories
```

The application displays the categories in sorted order.

Example:

```text
1. Food
2. Shopping
3. Transport
4. Work
```

Categories are taken from the expenses already stored in the application.

---

# `total`

Displays the total amount of all stored expenses.

### Syntax

```text
Expense> total
```

Example:

```text
Expense> total
```

Example output:

```text
| Expense:             8500|
```

The total is calculated by adding the amounts of all stored expenses.

---

# `average`

Displays the average expense amount.

### Syntax

```text
Expense> average
```

Example:

```text
Expense> average
```

Example output:

```text
| Average expenses:    1062.5              |
```

The average is calculated using:

```text
Total expenses / Number of expenses
```

---

# `expense_by_category`

Displays the total amount spent in each category.

### Syntax

```text
Expense> expense_by_category
```

Example:

```text
Expense> expense_by_category
```

Example output:

```text
| Category             | Amount     |
-------------------------------------------------------
| Food                 : 2500.0     |
| Transport            : 1500.0     |
| Shopping             : 3000.0     |
```

Expenses belonging to the same category are combined together.

---

# `m-stats`

Displays the total expense for a specific month and year.

### Syntax

```text
Expense> m-stats <month> <year>
```

The month is expected as a two-digit value.

### Example

```text
Expense> m-stats 09 2026
```

Example output:

```text
| Expense         | Month  | Year       |
-------------------------------------------------------
| 8500            | 09     | 2026       |
```

The command checks the date stored with each expense and adds the amounts that belong to the requested month and year.

---

# `max`

Displays the highest expense amount.

### Syntax

```text
Expense> max
```

Example:

```text
Expense> max
```

Example output:

```text
| Max amount:          3000.0 |
```

---

# `count`

Displays the total number of stored expenses.

### Syntax

```text
Expense> count
```

Example:

```text
Expense> count
```

Example output:

```text
| Number of expenses:  8 |
```

---

# `test`

Runs the application's test suite from inside the CLI.

### Syntax

```text
Expense> test
```

The test runner uses Python's built-in `unittest` framework.

The current test suite focuses primarily on the storage layer.

---

# `save_to_json`

Exports the stored expenses to a JSON file.

This command is particularly useful in the **SQLite version**, where SQLite is the primary storage system.

### Syntax

```text
Expense> save_to_json <fileName>
```

### Example

```text
Expense> save_to_json backup
```

The application creates:

```text
data/backup.json
```

The `.json` extension is added automatically.

Example:

```text
Expense> save_to_json september_backup
```

creates:

```text
data/september_backup.json
```

If the database contains no expenses, the application reports that there is no data to export.

---

# Getting Help

The CLI uses `argparse`, so help can be displayed using:

```text
Expense> -h
```

The help screen displays the available commands and their descriptions.

The CLI also provides examples for many commands.

---

# Exiting the Application

The application can be closed using either:

```text
Expense> exit
```

or:

```text
Expense> quit
```

The application then displays:

```text
Goodbye!
```

---

# Example Session

A typical session can look like this:

```text
Expense> add 400 Food Lunch
Expense added successfully, you can find it • search 1234

Expense> add 800 Transport Taxi
Expense added successfully, you can find it • search 5678

Expense> list

| id     | amount       | category                  | description               | date         |
------------------------------------------------------------------------------------------
| 5678   | 800.0        | Transport                 | Taxi                      | 2026-09-17   |
| 1234   | 400.0        | Food                      | Lunch                     | 2026-09-17   |

Expense> search Food

Expense> categories

Expense> total

Expense> average

Expense> expense_by_category

Expense> m-stats 09 2026

Expense> max

Expense> count

Expense> save_to_json backup

Expense> test

Expense> exit

Goodbye!
```

---

# Data Storage

## JSON Version

The first version stores expenses in:

```text
data/expenses.json
```

The data is stored as a JSON array.

Example:

```json
[
    {
        "id": 1228,
        "amount": 500.0,
        "category": "Good",
        "description": "good",
        "date": "2026-09-17"
    }
]
```

The JSON storage implementation uses Python's:

```python
json
```

module.

---

## SQLite Version

The second version stores expenses in:

```text
data/expenses.db
```

The application uses Python's built-in:

```python
sqlite3
```

module.

The database is initialized automatically and the `expenses` table is created if it does not already exist.

---

# How Data Flows Through the Application

When an expense is added, the general flow is:

```text
User
  │
  ▼
Expense CLI
  │
  ▼
ExpenseService
  │
  ▼
Expense Model
  │
  ▼
Storage
  │
  ▼
JSON / SQLite
```

When statistics are requested:

```text
User
  │
  ▼
CLI
  │
  ▼
ExpenseService
  │
  ▼
Storage
  │
  ▼
Stored Expenses
  │
  ▼
Statistics
  │
  ▼
Terminal Output
```

This separation keeps the CLI, application logic, storage, and calculations in different modules.

---

# Testing

The project uses Python's built-in `unittest` framework.

The tests are located in:

```text
tests/
├── run_test.py
└── storage.py
```

The current tests cover storage functionality including:

- Checking basic functionality
- Checking the data path
- Adding an expense
- Loading expenses
- Deleting an expense
- Listing expenses
- Searching expenses
- Retrieving categories
- Retrieving statistics
- Saving data to JSON
- Cleaning up test data

Tests can be started from the application itself:

```text
Expense> test
```

---

# Technologies Used

The project is built using Python's standard library.

Main technologies and modules include:

- Python
- `argparse` — command-line argument parsing
- `shlex` — parsing interactive CLI input
- `dataclasses` — expense data model
- `datetime` — expense dates
- `json` — JSON data storage/export
- `sqlite3` — SQLite database storage
- `pathlib` — file and directory handling
- `unittest` — automated testing

No external Python packages are required.

---

# Learning Objectives

This project demonstrates several Python and software-development concepts:

- Building an interactive command-line application
- Using `argparse`
- Parsing command-line input
- Using `shlex` for quoted input
- Creating Python packages
- Using classes and dataclasses
- Separating application responsibilities
- File handling
- JSON serialization and deserialization
- SQLite database operations
- SQL queries
- Data aggregation
- Date-based filtering
- Unit testing with `unittest`
- Organizing a Python project into modules

---

# Project Development

The project was developed in two stages.

### Stage 1 — JSON

The initial implementation used:

```text
Python
   │
   ▼
Storage
   │
   ▼
expenses.json
```

This version focused on learning file handling and JSON-based persistence.

### Stage 2 — SQLite

The second implementation moved the primary storage to:

```text
Python
   │
   ▼
Storage
   │
   ▼
SQLite
   │
   ▼
expenses.db
```

The SQLite implementation provides more structured data storage while retaining the ability to export the data to JSON.

---

# Current Limitations

The current implementation is intentionally simple and can be extended in the future.

Possible improvements include:

- Adding a dedicated category-management command
- Adding an edit/update expense command
- Improving category filtering in the `list` command
- Adding more comprehensive service and statistics tests
- Improving validation for amounts and dates
- Improving error messages
- Preventing duplicate expense IDs
- Adding date-range filtering
- Adding CSV export
- Adding import functionality
- Adding configurable storage backends
- Improving empty-database handling
- Adding more detailed monthly reports
- Adding test isolation using a separate test database

---

# Future Improvements

Possible future features include:

```text
Edit expense
Delete multiple expenses
Date-range search
Custom categories
Monthly budget
Budget warnings
CSV export
CSV import
Detailed monthly reports
Interactive statistics
Database configuration
More comprehensive unit tests
```

---

# License

This project is created for learning and educational purposes.