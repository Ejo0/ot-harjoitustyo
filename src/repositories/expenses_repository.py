from datetime import date
from models.expense_row import ExpenseRow
import db_connector

class ExpensesRepository:

    def __init__(self) -> None:
        self.__connector = db_connector.get_db_connector()

    def create(self, user_id: int, exp_date: date, amount: int, vat: int, desc: str, exp_type = None):
        if not exp_type :
            exp_type = "other_deductible"
        date_as_str = f"{exp_date.year}-{exp_date.month:02d}-{exp_date.day:02d}"
        self.__connector.execute(
            "INSERT INTO Expenses (user_id, event_date, amount, vat, description, type)" +
            "VALUES (?,?,?,?,?,?)",
            [user_id, date_as_str, amount, vat, desc, exp_type]
        )

    def get_expense_row(self, row_id: int):
        expense_row = self.__connector.execute(
            "SELECT * FROM Expenses WHERE id = ?", [row_id]).fetchone()
        year, month, day = expense_row[2].split("-")
        event_date_as_date = date(int(year), int(month), int(day))
        return ExpenseRow(
            expense_row[0], expense_row[1], event_date_as_date,
            expense_row[3], expense_row[4], expense_row[5], expense_row[6]
        )

    def get_all_expense_rows(self, user_id: int = None):
        if user_id:
            expense_rows = self.__connector.execute(
                "SELECT * FROM Expenses WHERE User_id = ?", [user_id])
        else:
            expense_rows = self.__connector.execute("SELECT * FROM Expenses")
        output = []
        for expense_row in expense_rows:
            year, month, day = expense_row[2].split("-")
            event_date_as_date = date(int(year), int(month), int(day))
            output.append(ExpenseRow(
                expense_row[0], expense_row[1], event_date_as_date,
                expense_row[3], expense_row[4], expense_row[5], expense_row[6]
            ))
        return output

    def delete_all(self):
        self.__connector.execute("DELETE FROM Expenses")

    def total_amount(self, user_id: int):
        total = self.__connector.execute(
            "SELECT SUM(Amount) FROM Expenses WHERE User_id = ?", [user_id]).fetchone()
        return total[0] if total[0] else 0
