
from pathlib import Path
import json 
from .db import init_db
import sqlite3


class Storage:
    """It save the data"""

    def __init__(self):
        self.parentPath = Path(__file__).parent.parent / "data"
        self.fileName = "expenses.json"
        self.fullPath = self.parentPath / self.fileName
        self.DB_PATH = self.parentPath / "expenses.db"

    def initialize_database(self):
        """creating the database"""
        init_db(self.DB_PATH) 

    def load_expense(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            conn.row_factory = sqlite3.Row # lets us access columns by name
            data = conn.execute("SELECT * FROM expenses ORDER BY date DESC").fetchall()
        return data

    def add_expense(self, data):
        """It save the data into the storage sqlite""" 

        with sqlite3.connect(self.DB_PATH) as conn:
            conn.execute( """
                INSERT INTO expenses(id, amount, category, description, date)
                VALUES (?, ?, ?, ?, ?)
                """, (
                    data.id,
                    data.amount,
                    data.category,
                    data.description,
                    data.date.isoformat()
                ))
            conn.commit()

        return data 

    # def add_list_of_expenses(self, dataList):
    #     pass

    def delete_expense(self, id):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.execute("DELETE FROM expenses WHERE id = ?", (id,))
            conn.commit()

            if cursor.rowcount == 0:
                return "X • item doesn't exist."

            else:
                return "•ϡ 1 item deleted."
 

    def show_list_of_expenses(self):
        expenseList = self.load_expense()
        return expenseList

    def search_expense(self, value):
        """
        Search expenses using a single value.

        The value can match:
        - id       -> exact match
        - amount   -> exact match
        - category -> partial match
        - description -> partial match
        """
        query = """
            SELECT *
            FROM expenses
            WHERE id = ?
            OR amount = ?
            OR category LIKE ?
            OR description LIKE ?
            ORDER BY date DESC
        """

        params = [
            value,
            value,
            f"%{value}%",
            f"%{value}%"
        ]

        with sqlite3.connect(self.DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(query, params).fetchall()
            return rows


    def show_categories(self):
        expense = self.load_expense()
        categories = []

        if not expense:
            return False

        for e in expense:
            if e["category"] in categories:
                pass
            else:
                categories.append(e["category"])

        return categories

    def statistics(self):
        expenses = self.load_expense()

        if not expenses:
            return []
        else:
            return expenses


    def save_to_json(self, filename):
        expenses = self.load_expense()

        if not expenses:
            print("-" * 8, "|")
            print("\tDatabase is empty. Add some expenses!")
            print("-" * 8, "|")
            return False

        expenses = [dict(expense) for expense in expenses]

        self.parentPath.mkdir(parents=True, exist_ok=True)

        file = self.parentPath / f"{filename}.json"
        # print(expenses)
        try:
            with open(file, "w") as f:
                json.dump(expenses, f, indent=4, default=str)

            # print(f"Expenses saved to {file}")
            return True

        except Exception as e:
            print(f"\tError: {e}")
            return False




store = Storage()
store.initialize_database()

