from datetime import date
from repositories.expenses_repository import ExpensesRepository


class ExpenseRowService:

    def __init__(self) -> None:
        self._expenses_repository = ExpensesRepository()

    def rows_sorted_by_date(self, user_id: int, start_date: date = None, end_date: date = None, is_reverse=False):
        expense_rows = self._expenses_repository.get_expense_rows_from_range(user_id, start_date, end_date)
        return sorted(expense_rows, key=lambda row: row.date, reverse=is_reverse)

    def create_expense_row(self, user_id: int, event_date: date,
                            amount: int, vat: int, description: str):

        self._expenses_repository.create(
            user_id, event_date, amount, vat, description)

    def delete_all(self):
        self._expenses_repository.delete_all()

    def get_expense_row(self, row_id: int):
        return self._expenses_repository.get_expense_row(row_id)
