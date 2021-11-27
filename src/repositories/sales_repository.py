from datetime import date
from models.sale_row import SaleRow
import db_connector


class SalesRepository:

    def __init__(self) -> None:
        self.__connector = db_connector.get_db_connector()

    def create(self, user_id: int, event_date: date, amount: int, vat: int, description: str):
        date_as_str = f"{event_date.year}-{event_date.month:02d}-{event_date.day:02d}"
        self.__connector.execute(
            "INSERT INTO Sales (user_id, event_date, amount, vat, description)" +
            "VALUES (?,?,?,?,?)",
            [user_id, date_as_str, amount, vat, description]
        )

    def get_sale_row(self, row_id: int):
        sale_row = self.__connector.execute(
            "SELECT * FROM Sales WHERE id = ?", [row_id]).fetchone()
        year, month, day = sale_row[2].split("-")
        event_date_as_date = date(int(year), int(month), int(day))
        return SaleRow(
            sale_row[0], sale_row[1], event_date_as_date,
            sale_row[3], sale_row[4], sale_row[5]
        )

    def get_all_sale_rows(self, user_id: int = None):
        if user_id:
            sale_rows = self.__connector.execute(
                "SELECT * FROM Sales WHERE User_id = ?", [user_id])
        else:
            sale_rows = self.__connector.execute("SELECT * FROM Sales")
        output = []
        for sale_row in sale_rows:
            year, month, day = sale_row[2].split("-")
            event_date_as_date = date(int(year), int(month), int(day))
            output.append(SaleRow(
                sale_row[0], sale_row[1], event_date_as_date,
                sale_row[3], sale_row[4], sale_row[5]
            ))
        return output

    def delete_all(self):
        self.__connector.execute("DELETE FROM Sales")

    def total_amount(self, user_id: int):
        total = self.__connector.execute(
            "SELECT SUM(Amount) FROM Sales WHERE User_id = ?", [user_id]).fetchone()
        return total[0] if total[0] else 0
