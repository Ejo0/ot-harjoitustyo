from datetime import date
from models.expense_row import ExpenseRow
import db_connector

class ExpensesRepository:

    def __init__(self) -> None:
        self.__connector = db_connector.get_db_connector()

    def delete_all(self):
        self.__connector.execute("DELETE FROM Expenses")

    def create(self, user_id: int, exp_date: date, amount: int, vat: int, desc: str, exp_type = None):
        if not exp_type :
            exp_type = "other_deductible"
        date_as_str = f"{exp_date.year:04d}-{exp_date.month:02d}-{exp_date.day:02d}"
        self.__connector.execute(
            "INSERT INTO Expenses (user_id, event_date, amount, vat, description, type)" +
            "VALUES (?,?,?,?,?,?)",
            [user_id, date_as_str, amount, vat, desc, exp_type]
        )

    def get_expense_row(self, row_id: int):
        expense_row = self.__connector.execute(
            "SELECT * FROM Expenses WHERE id = ?", [row_id]).fetchall()
        return self._tuple_to_expense_row(expense_row)[0]

    def get_expense_rows_from_range(self, user_id: int, start_date: date, end_date: date):
        start_date_as_str, end_date_as_str = self._dates_to_str(start_date, end_date)

        expense_rows = self.__connector.execute(
            "SELECT * " +
            "FROM Expenses " +
            "WHERE user_id = ? " +
            "AND event_date BETWEEN ? AND ?",
                [user_id, start_date_as_str, end_date_as_str]
            )
        return self._tuple_to_expense_row(expense_rows)

    def total_amount(self, user_id: int, start_date: date, end_date: date):
        start_date_as_str, end_date_as_str = self._dates_to_str(start_date, end_date)

        total = self.__connector.execute(
            "SELECT SUM(Amount) " +
            "FROM Expenses " +
            "WHERE User_id = ? " +
            "AND event_date BETWEEN ? AND ?",
            [user_id, start_date_as_str, end_date_as_str]).fetchone()
        return total[0] if total[0] else 0

    def _dates_to_str(self, start_date, end_date)-> tuple:
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
                expense_row[3], expense_row[4], expense_row[5], expense_row[6]
            ))
        return output
