from datetime import date
from models.expense_row import ExpenseRow
import db_connector

class ExpensesRepository:
    """A class responsible of interacting with Expenses-table (SQL database)
    """

    def __init__(self) -> None:
        """Constructor, database connector -object is called from db_connector.py-file
        """
        self.__connector = db_connector.get_db_connector()

    def delete_all(self):
        """Deletes all rows from Expenses-table
        """
        self.__connector.execute("DELETE FROM Expenses")

    def create(self, user_id: int, exp_date: date, amount: int, vat: int, desc: str):
        """Creates new row to Expenses-table

        Args:
            user_id (int): Id of the user this expense belongs
            exp_date (date): Date of event
            amount (int): Total amount of expense in cents, including vat
            vat (int): Vat percentage of the expense
            desc (str): Description of the expense
        """
        date_as_str = f"{exp_date.year:04d}-{exp_date.month:02d}-{exp_date.day:02d}"
        self.__connector.execute(
            "INSERT INTO Expenses (user_id, event_date, amount, vat, description)" +
            "VALUES (?,?,?,?,?)",
            [user_id, date_as_str, amount, vat, desc]
        )

    def get_expense_rows_from_range(self, user_id: int, start_date: date, end_date: date):
        """Returns expenses of an user from given range. If start and/or end date is missing
        (value == None), default values are set using self._dates_to_str function.

        Args:
            user_id (int): User ID
            start_date (date): Start date of range, can be None
            end_date (date): End date of range, can be None

        Returns:
            (list): A list of ExpenseRow-objects
        """
        start_date_as_str, end_date_as_str = self._dates_to_str(start_date, end_date)

        expense_rows = self.__connector.execute(
            "SELECT * " +
            "FROM Expenses " +
            "WHERE user_id = ? " +
            "AND event_date BETWEEN ? AND ?",
                [user_id, start_date_as_str, end_date_as_str]
            )
        return self._tuple_to_expense_row(expense_rows)

    def total_amount(self, user_id: int, start_date: date, end_date: date)-> int:
        """Returns total amount of expenses of an user from given range

        Args:
            user_id (int): User id
            start_date (date): Start date of range
            end_date (date): End date of range

        Returns:
            int: Total amount of expenses in cents, including vat (value added tax)
        """
        start_date_as_str, end_date_as_str = self._dates_to_str(start_date, end_date)

        total = self.__connector.execute(
            "SELECT SUM(Amount) " +
            "FROM Expenses " +
            "WHERE User_id = ? " +
            "AND event_date BETWEEN ? AND ?",
            [user_id, start_date_as_str, end_date_as_str]).fetchone()
        return total[0] if total[0] else 0

    def _dates_to_str(self, start_date: date, end_date: date)-> tuple:
        if start_date:
            start_date_as_str = f"{start_date.year:04d}-{start_date.month:02d}-{start_date.day:02d}"
        else:
            start_date_as_str = "0001-01-01"
        if end_date:
            end_date_as_str = f"{end_date.year:04d}-{end_date.month:02d}-{end_date.day:02d}"
        else:
            end_date_as_str ="9999-12-31"
        return (start_date_as_str, end_date_as_str)

    def _tuple_to_expense_row(self, expense_rows: list):
        output = []
        for expense_row in expense_rows:
            year, month, day = expense_row[2].split("-")
            event_date_as_date = date(int(year), int(month), int(day))
            output.append(ExpenseRow(
                expense_row[0], expense_row[1], event_date_as_date,
                expense_row[3], expense_row[4], expense_row[5]
            ))
        return output
