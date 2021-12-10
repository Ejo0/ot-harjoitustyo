from datetime import date
from repositories.expenses_repository import ExpensesRepository


class ExpenseRowService:
    """An interface for GUI to add and get data from ExpensesRepository
    """

    def __init__(self) -> None:
        """Constructor where ExpensesRepository is initialized
        """
        self._expenses_repository = ExpensesRepository()

    def rows_sorted_by_date(self, user_id: int, start_date: date = None, end_date: date = None, is_reverse=False):
        """Returns expense rows of an user from given date range, ordered by date.

        Args:
            user_id (int): User ID
            start_date (date, optional): Start date of range. Defaults to None.
            end_date (date, optional): End date of range. Defaults to None.
            is_reverse (bool, optional): Order of events. Defaults to False, which means the event with smallest date is first.

        Returns:
            [list]: A list of ExpenseRow-instances, ordered by date
        """
        expense_rows = self._expenses_repository.get_expense_rows_from_range(user_id, start_date, end_date)
        return sorted(expense_rows, key=lambda row: row.date, reverse=is_reverse)

    def create_expense_row(self, user_id: int, event_date: date,
                            amount: int, vat: int, description: str):
        """Creates an expense to database.

        Args:
            user_id (int): User ID
            event_date (date): Date of the event
            amount (int): Amount of the event, in cents, includes vat
            vat (int): Vat percentage of event
            description (str): Description of the expense
        """

        self._expenses_repository.create(
            user_id, event_date, amount, vat, description)

    def delete_all(self):
        """Deletes all expenses from database.
        """
        self._expenses_repository.delete_all()

    def get_expense_row(self, row_id: int):
        """Returns single ExpenseRow

        Args:
            row_id (int): Id of the expense

        Returns:
            [type]: ExpenseRow
        """
        return self._expenses_repository.get_expense_row(row_id)
