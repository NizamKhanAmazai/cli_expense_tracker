import unittest
from expense_tracker.storage import Storage
from expense_tracker.models import Expense
from datetime import date 
from dataclasses import asdict 
from pathlib import Path

class Storage_Test(unittest.TestCase):
    """testing the storage class"""
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)

    def setUp(self):
        self.store = Storage()
        self.expense = Expense(5, 50000, 'Test', 'Monthly Shoping', date.today())
        self.forDeleteExpense = Expense(10, 500, 'Delete', 'Monthly Shoping', date.today()) 
        self.parentPath = Path(__file__).parent.parent / "data"
        self.filename = 'test'


    def expense_to_dect(self,expense):
        data = asdict(expense)
        data['date'] = expense.date.isoformat()
        return data

    def test_check(self):
        self.assertEqual('hello','hello')

 
    def test_add_expense(self):
        result = self.store.add_expense(self.expense) 
        self.assertEqual(result, self.expense)


    def test_load_expense(self):
        result = self.store.load_expense() 
        result = [dict(expense) for expense in result] 
        self.assertIn(self.expense_to_dect(self.expense), result)


    def test_delete_expense(self):
        result = self.store.delete_expense(self.forDeleteExpense.id)
        self.assertIn(result, ["X • item doesn't exist.", "•ϡ 1 items deleted."])


    def test_show_list_of_expenses(self):
        result = self.store.show_list_of_expenses()
        result = [dict(expense) for expense in result] 
        self.assertIn(self.expense_to_dect(self.expense), result)


    def test_search_expense(self):
        expense = self.expense_to_dect(self.expense)
        result = self.store.search_expense(self.expense.id)
        result = [dict(expense) for expense in result] 
        self.assertIn(expense, result)


    def test_show_categories(self):
        result = self.store.show_categories()
        category = self.expense_to_dect(self.expense)
        self.assertIn(category['category'], result)


    def test_statistics(self):
        result = self.store.statistics() 
        result = [dict(expense) for expense in result] 
        self.assertIn(self.expense_to_dect(self.expense), result)

    def test_save_to_json(self): 
        data = self.store.save_to_json(self.filename) 
        self.assertEqual(data, True)
        
    def test_zzz_delete_test_file(self):
        file = self.parentPath / str(self.filename + '.json')
        delTestFile = None
        try:
            delTestFile = Path(file).unlink()
        except FileNotFoundError:
            pass
        self.assertEqual(delTestFile, delTestFile)

    def test_zzz_cleanup(self):
        result = self.store.delete_expense(self.expense.id)
        self.assertIn(result, ["X • item doesn't exist.", "•ϡ 1 item deleted."])
