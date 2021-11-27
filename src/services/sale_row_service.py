from datetime import date
from repositories.sales_repository import SalesRepository


class SaleRowService:

    def __init__(self) -> None:
        self._sales_repository = SalesRepository()

    def rows_sorted_by_date(self, user_id: int, is_reverse=False):
        sale_rows = self._sales_repository.get_all_sale_rows(user_id)
        return sorted(sale_rows, key=lambda row: row.date, reverse=is_reverse)

    def create_sale_row(self, user_id: int, event_date: date,
                        amount: int, vat: int, description: str):

        self._sales_repository.create(
            user_id, event_date, amount, vat, description)

    def total_amount(self, user_id: int):
        return self._sales_repository.total_amount(user_id)

    def delete_all(self):
        self._sales_repository.delete_all()
