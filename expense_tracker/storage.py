from pathlib import Path
import json
from dataclasses import asdict


class Storage:
    """It save the data"""

    def __init__(self):
        self.parentPath = Path(__file__).parent.parent / "data"
        self.fileName = "expenses.json"
        self.fullPath = self.parentPath / self.fileName
        self.DB_PATH = self.parentPath / "expenses.db"

    def does_path_exist(self):
        """check does the file exist if not create it"""
        if self.parentPath.exists():
            if (self.parentPath / self.fileName).exists():
                return True
            else:
                (self.parentPath / self.fileName).touch()
                return False
        else:
            self.parentPath.mkdir()
            return False

    def load_expense(self):
        try:
            with open(self.fullPath, "r", encoding="utf-8") as jsonFile:
                return json.load(jsonFile)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_expense(self, data):
        """It save the data into the storage json/sqlite"""

        # check weather the folder and the file exist if not the function will create it
        file = self.does_path_exist()
        while not file:
            file = self.does_path_exist()

        oldData = self.load_expense()
        oldData.append(asdict(data))

        try:
            with open(self.fullPath, "w") as jsonFile:
                json.dump(oldData, jsonFile, indent=4, default=str)
        except Exception as e:
            return e
        else:
            return data

    def add_list_of_expenses(self, dataList):
        """it add the list of expense model"""

        dataList = [asdict(d) for d in dataList]
        try:
            with open(self.fullPath, "w") as file:
                json.dump(dataList, file, indent=4, default=str)

        except (FileNotFoundError, json.JSONDecodeError):
            print("file error!")

    def delete_expense(self, id):
        """it first load the json and get and find the match and delete it"""
        expenseLists = self.load_expense()
        remainingList = []
        isDelete = 0

        for e in expenseLists:
            if e["id"] == id:
                isDelete += 1
            else:
                remainingList.append(e)

        try:
            with open(self.fullPath, "w") as file:
                json.dump(remainingList, file, indent=4, default=str)

        except (FileNotFoundError, json.JSONDecodeError):
            print("file error!")

        if isDelete == 0:
            return "X • item doesn't exist."

        elif isDelete > 0:
            return f"•ϡ {isDelete} items deleted."

    def show_list_of_expenses(self):
        expenseList = self.load_expense()
        return expenseList

    def search_expense(self, id):
        expense = self.load_expense()
        searchedExpenses = []

        if not expense:
            return False

        for e in expense:
            try:
                if e["id"] == int(id):
                    searchedExpenses.append(e)
            except (ValueError, AttributeError):
                pass
            try:
                if round(e["amount"], 0) == round(int(id), 0):
                    searchedExpenses.append(e)
            except (ValueError, AttributeError):
                pass
            try:
                if id.lower() in e["category"].lower():
                    searchedExpenses.append(e)
            except (ValueError, AttributeError):
                pass
            try:
                if id.lower() in e["description"].lower():
                    searchedExpenses.append(e)
            except Exception:
                pass
        return searchedExpenses

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

        self.parentPath.mkdir(parents=True, exist_ok=True)

        file = self.parentPath / f"{filename}.json"
        # print(expenses)
        try:
            with open(file, "w") as f:
                json.dump(expenses, f, indent=4, default=str)
            return True

        except Exception as e:
            print(f"\tError: {e}")
            return False
