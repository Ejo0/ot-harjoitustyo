from datetime import date
from repositories.expenses_repository import ExpensesRepository


class ExpenseRowService:

    def __init__(self) -> None:
        self._expenses_repository = ExpensesRepository()

    def rows_sorted_by_date(self, user_id: int, is_reverse=False):
        expense_rows = self._expenses_repository.get_all_expense_rows(user_id)
        return sorted(expense_rows, key=lambda row: row.date, reverse=is_reverse)

    def create_expense_row(self, user_id: int, event_date: date,
                            amount: int, vat: int, description: str):

        self._expenses_repository.create(
            user_id, event_date, amount, vat, description)

    def total_amount(self, user_id: int):
        return self._expenses_repository.total_amount(user_id)

    def delete_all(self):
        self._expenses_repository.delete_all()
