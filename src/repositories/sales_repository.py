import db_connector
from models.sale_row import SaleRow


class SalesRepository:

    def __init__(self) -> None:
        self.__connector = db_connector.get_db_connector()

    def create(self, description: str, amount: int, user_id: int, vat: int):
        self.__connector.execute(
            "INSERT INTO Sales (description, amount, user_id, vat)" +
            "VALUES (?,?,?,?)",
            [description, amount, user_id, vat]
        )

    def get_sale_row(self, row_id: int):
        sale_row = self.__connector.execute(
            "SELECT * FROM Sales WHERE id = ?", [row_id]).fetchone()
        return SaleRow(sale_row[0], sale_row[1], sale_row[2], sale_row[3], sale_row[4])

    def get_all_sale_rows(self, user_id: int = None):
        if user_id:
            sale_rows = self.__connector.execute(
                "SELECT * FROM Sales WHERE User_id = ?", [user_id])
        else:
            sale_rows = self.__connector.execute("SELECT * FROM Sales")
        output = []
        for sale_row in sale_rows:
            output.append(SaleRow(sale_row[0], sale_row[1], sale_row[2], sale_row[3], sale_row[4]))
        return output

    def delete_all(self):
        self.__connector.execute("DELETE FROM Sales")

    def total_amount(self, user_id: int):
        total = self.__connector.execute(
            "SELECT SUM(Amount) FROM Sales WHERE User_id = ?", [user_id]).fetchone()
        return total[0] if total[0] else 0
