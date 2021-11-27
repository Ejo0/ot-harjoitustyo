import unittest
from datetime import date
from repositories.expenses_repository import ExpensesRepository

class TestExpensesRepository(unittest.TestCase):


    def setUp(self) -> None:
        self._expenses_repository = ExpensesRepository()
        self._expenses_repository.delete_all()
        self._expenses_repository.create(5, date(2000, 3, 3), 50000, 0, "Computer")
        self._expenses_repository.create(1, date(2000, 2, 2), 500, 10, "Busticket")

    def test_get_expense_uses_row_id_not_user_id(self):
        expense = self._expenses_repository.get_expense_row(1)
        self.assertEqual(expense.description, "Computer")

    def test_get_all_rows_without_id_gives_rows_from_each_user(self):
        expenses = self._expenses_repository.get_all_expense_rows()
        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0].user_id, 5)
        self.assertEqual(expenses[1].vat, 10)
        self.assertEqual(expenses[0].id, 1)
    
    def test_get_expense_row_date_type_is_datetime_date(self):
        expense = self._expenses_repository.get_expense_row(1)
        self.assertEqual(type(expense.date), date)
    