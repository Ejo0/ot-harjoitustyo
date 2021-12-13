import unittest
from datetime import date
from repositories.expenses_repository import ExpensesRepository
from models.expense_row import ExpenseRow

class TestExpensesRepository(unittest.TestCase):


    def setUp(self) -> None:
        self._expenses_repository = ExpensesRepository()
        self._expenses_repository.delete_all()
        self._expenses_repository.create(5, date(2000, 3, 3), 50000, 0, "Computer")
        self._expenses_repository.create(1, date(2000, 2, 2), 500, 10, "Busticket")

    def test_get_expense_rows_from_range_uses_user_id_not_row_id(self):
        expense = self._expenses_repository.get_expense_rows_from_range(1, None, None)[0]
        self.assertEqual(expense.description, "Busticket")
    
    def test_get_expense_rows_from_range_returns_list_of_expense_rows(self):
        expenses = self._expenses_repository.get_expense_rows_from_range(5, None, None)
        self.assertEqual(type(expenses), list)
        self.assertEqual(type(expenses[0]), ExpenseRow)
