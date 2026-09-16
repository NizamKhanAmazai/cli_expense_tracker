from datetime import date
from .storage import Storage
from .models import Expense
import time
from .statistics import *


# add expense · delete expense · search · categories · monthly statistics
def start():
    print("\n\t\t\t\t\t -----------------------------------------")
    print("\t\t\t\t\t |   -- Wellcome to expense tracker --   |")
    print("\t\t\t\t\t -----------------------------------------")
    print(
        "\t\t You can add expense, delete expense, search expense and also get monthly statistics of expenses \n"
    )
    print(
        """\t--------------------------------------------------------------------------------------------------------------------------\n"""
    )


class ExpenseService:
    """all services"""

    def __init__(self):
        self.store = Storage()
        pass

    def add_expense(self, amount, cat, desc):
        id = int((time.time() * 1000000) % 10000)
        today = date.today()
        ex = Expense(id, amount, cat.title(), desc, today)

        self.store.add_expense(ex)

        print("-" * 8, "|")
        print(f"\t•ϡ Expense added successfully, you can find it • search {id}")
        print("-" * 8, "|")

    def list_expenses(self, cat):
        data = self.store.show_list_of_expenses()
        if not data:
            print("-" * 8, "|")
            print(f"\t There is no expense in the list!")
            print("-" * 8, "|")
            return 

        # set columns width
        w = {"id": 6, "amount": 12, "category": 25, "description": 25, "date": 12}

        # Header
        print(
            f"| {'id':<{w['id']}} | {'amount':<{w['amount']}} | {'category':<{w['category']}} | {'description':<{w['description']}} | {'date':<{w['date']}} |"
        )
        print("-" * 90)

        # Rows
        for e in data:
            desc = (
                e["description"][: w["description"] - 3] + "..."
                if len(e["description"]) > w["description"]
                else e["description"]
            )
            print(
                f"| {e['id']:<{w['id']}} | {e['amount']:<{w['amount']}} | {e['category']:<{w['category']}} | {desc:<{w['description']}} | {e['date']:<{w['date']}} |"
            )

    def delete_expense(self, id):
        message = self.store.delete_expense(id)

        print("-" * 8, "|")
        print("\t", message)
        print("-" * 8, "|")

    def search_expenses(self, keyword):
        expense = self.store.search_expense(keyword)
        if expense == False or expense == None or len(expense) == 0:
            print("-" * 8, "|")
            print(f"\t Expense not found!")
            print("-" * 8, "|")

        else:
            w = {"id": 6, "amount": 12, "category": 25, "description": 25, "date": 12}

            print(
                f"| {'id':<{w['id']}} | {'amount':<{w['amount']}} | {'category':<{w['category']}} | {'description':<{w['description']}} | {'date':<{w['date']}} |"
            )
            print("-" * 90)
            for e in expense:
                # desc = e['description'][:w['description']-3] + "..." if len(e['description']) > w['description'] else e['description']
                print(
                    f"| {e['id']:<{w['id']}} | {e['amount']:<{w['amount']}} | {e['category']:<{w['category']}} | {e['description']:<{w['description']}} | {e['date']:<{w['date']}} |"
                )

    def show_all_categories(self):
        categories = self.store.show_categories()
        print("\t", "-" * 40)
        count = 1

        for category in sorted(categories):
            print(f"\t | \t {count}. {category:<30} |")
            count += 1

    def monthly_statistics(self, month, year):
        expenses = self.store.statistics()
        if len(expenses) == 0 or expenses == None:
            print("-" * 8, "|")
            print(f"\t Expense not found!")
            print("-" * 8, "|")

        get_monthly_stats(expenses, month, year)

    def total_expenses(self):
        expenses = self.store.statistics()
        if len(expenses) == 0 or expenses == None:
            print("-" * 8, "|")
            print(f"\t Expense not found!")
            print("-" * 8, "|")

        show_total_expense(expenses)

    def average_expense(self):
        expenses = self.store.statistics()
        if len(expenses) == 0 or expenses == None:
            print("-" * 8, "|")
            print(f"\t Expense not found!")
            print("-" * 8, "|")

        show_average_expenses(expenses)

    def expenses_by_category(self):
        expenses = self.store.statistics()
        if len(expenses) == 0 or expenses == None:
            print("-" * 8, "|")
            print(f"\t Expense not found!")
            print("-" * 8, "|")

        expenses_by_category(expenses)

    def highest_expense(self):
        expenses = self.store.statistics()
        if len(expenses) == 0 or expenses == None:
            print("-" * 8, "|")
            print(f"\t Expense not found!")
            print("-" * 8, "|")

        highest_expense(expenses)

    def count_expenses(self):
        expenses = self.store.statistics()
        if len(expenses) == 0 or expenses == None:
            print("-" * 8, "|")
            print(f"\t Expense not found!")
            print("-" * 8, "|")

        count_expense(expenses)

    def save_to_json(self, filename):
        file = self.store.save_to_json(filename)
        if file:
            print('-'*50)
            # print(f"\t| {'Data saved in:':<15} {f'{filename}.json':<20} |")
            print(f"\t| {'Data successfully saved!'} |")
            print('-'*50)
        else:
            print("-" * 8, "|")
            print(f"\t Error in creating file!")
            print("-" * 8, "|")

        