from datetime import date
from models.sale_row import SaleRow
import db_connector


class SalesRepository:

    def __init__(self) -> None:
        self.__connector = db_connector.get_db_connector()

    def delete_all(self):
        self.__connector.execute("DELETE FROM Sales")

    def create(self, user_id: int, event_date: date, amount: int, vat: int, description: str):
        date_as_str = f"{event_date.year:04d}-{event_date.month:02d}-{event_date.day:02d}"
        self.__connector.execute(
            "INSERT INTO Sales (user_id, event_date, amount, vat, description)" +
            "VALUES (?,?,?,?,?)",
            [user_id, date_as_str, amount, vat, description]
        )

    def get_sale_row(self, row_id: int):
        sale_row = self.__connector.execute(
            "SELECT * FROM Sales WHERE id = ?", [row_id]).fetchall()
        return self._tuple_to_sale_row(sale_row)[0]

    def get_sale_rows_from_range(self, user_id: int, start_date: date, end_date: date):
        start_date_as_str, end_date_as_str = self._dates_to_str(start_date, end_date)

        sale_rows = self.__connector.execute(
            "SELECT * " +
            "FROM Sales " +
            "WHERE user_id = ? " +
            "AND event_date BETWEEN ? AND ?",
            [user_id, start_date_as_str, end_date_as_str]
            )
        return self._tuple_to_sale_row(sale_rows)

    def total_amount(self, user_id: int, start_date: date, end_date: date):
        start_date_as_str, end_date_as_str = self._dates_to_str(start_date, end_date)

        total = self.__connector.execute(
            "SELECT SUM(Amount) " +
            "FROM Sales " +
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

    def _tuple_to_sale_row(self, sale_rows: list):
        output = []
        for sale_row in sale_rows:
            year, month, day = sale_row[2].split("-")
            event_date_as_date = date(int(year), int(month), int(day))
            output.append(SaleRow(
                sale_row[0], sale_row[1], event_date_as_date,
                sale_row[3], sale_row[4], sale_row[5]
            ))
        return output
