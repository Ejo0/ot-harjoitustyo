from datetime import date
from repositories.expenses_repository import ExpensesRepository
from repositories.sales_repository import SalesRepository


class AccountingService:

    def __init__(self) -> None:
        self._expenses_repository = ExpensesRepository()
        self._sales_repository = SalesRepository()

    def vatless_amount(self, row) -> int:
        vatless_amount = row.amount / ((100 + row.vat) * 0.01)
        return int(round(vatless_amount, 0))

    def vat_amount(self, row) -> int:
        vatless_amount = self.vatless_amount(row)
        return row.amount - vatless_amount

    def total_vatless_amount(self, rows: list) -> int:
        total_vatless_amount = 0
        for row in rows:
            total_vatless_amount += self.vatless_amount(row)
        return total_vatless_amount

    def total_vat(self, rows: list) -> int:
        total_vat = 0
        for row in rows:
            total_vat += self.vat_amount(row)
        return total_vat

    def vat_on_sales(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        sale_rows = self._sales_repository.get_sale_rows_from_range(
            user_id, start_date, end_date)
        return self.total_vat(sale_rows)

    def deductible_vat(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        expense_rows = self._expenses_repository.get_expense_rows_from_range(
            user_id, start_date, end_date
        )
        return self.total_vat(expense_rows)

    def vat_payable(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        vat_on_sales_amount = self.vat_on_sales(user_id, start_date, end_date)
        deductible_vat_amount = self.deductible_vat(user_id, start_date, end_date)
        return vat_on_sales_amount - deductible_vat_amount

    def net_sales(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        sale_rows = self._sales_repository.get_sale_rows_from_range(
            user_id, start_date, end_date)
        return self.total_vatless_amount(sale_rows)

    def net_expenses(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        expense_rows = self._expenses_repository.get_expense_rows_from_range(
            user_id, start_date, end_date)
        return self.total_vatless_amount(expense_rows)

    def net_result(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        net_sales_amount = self.net_sales(user_id, start_date, end_date)
        net_expenses_amount = self.net_expenses(user_id, start_date, end_date)
        return net_sales_amount - net_expenses_amount

    def total_sales_including_vat(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        return self._sales_repository.total_amount(user_id, start_date, end_date)

    def total_expenses_including_vat(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        return self._expenses_repository.total_amount(user_id, start_date, end_date)
