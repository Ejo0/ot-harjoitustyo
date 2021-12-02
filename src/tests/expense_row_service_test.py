import unittest
from datetime import date
from services.expense_row_service import ExpenseRowService


class TestExpenseRowService(unittest.TestCase):


    def setUp(self) -> None:
        self._expense_row_service = ExpenseRowService()
        self._expense_row_service.delete_all()
        self._expense_row_service.create_expense_row(3, date(2021, 3, 1), 10050, 24, "Phone")
        self._expense_row_service.create_expense_row(3, date(2021, 2, 2), 9000, 0, "Insurance")
        self._expense_row_service.create_expense_row(3, date(2021, 2, 5), 555, 0, "Busticket") 
        self._expense_row_service.create_expense_row(2, date(2021, 1, 1), 3000, 0, "Book")
    
    def test_rows_sorted_by_date_gives_correct_order(self):
        expenses = self._expense_row_service.rows_sorted_by_date(3)
        self.assertEqual(expenses[0].date, date(2021, 2, 2))
        self.assertEqual(expenses[1].amount, 555)
        self.assertEqual(expenses[2].description, "Phone")
    
    def test_rows_sorted_by_date_gives_correct_expenses(self):
        expenses = self._expense_row_service.rows_sorted_by_date(3)
        self.assertEqual(len(expenses), 3)
        self.assertEqual(expenses[0].amount, 9000)