from repositories.expenses_repository import ExpensesRepository
from repositories.sales_repository import SalesRepository

class AccountingService:

    def __init__(self) -> None:
        self._expenses_repository = ExpensesRepository()
        self._sales_repository = SalesRepository()

    def vatless_amount(self, row)-> int:
        vat_amount =  row.amount / ((100 + row.vat)* 0.01)
        return int(round(vat_amount, 0))

    def vat_amount(self, row)-> int:
        vatless_amount = self.vatless_amount(row)
        return row.amount - vatless_amount

    def total_vatless_amount(self, rows: list)-> int:
        total_vatless_amount = 0
        for row in rows:
            total_vatless_amount += self.vatless_amount(row)
        return total_vatless_amount

    def total_vat(self, rows: list)-> int:
        total_vat = 0
        for row in rows:
            total_vat += self.vat_amount(row)
        return total_vat

    def vat_on_sales(self, user_id: int)-> int:
        sale_rows = self._sales_repository.get_all_sale_rows(user_id)
        return self.total_vat(sale_rows)

    def deductible_vat(self, user_id: int)-> int:
        expense_rows = self._expenses_repository.get_all_expense_rows(user_id)
        return self.total_vat(expense_rows)

    def vat_payable(self, user_id: int) -> int:
        return self.vat_on_sales(user_id) - self.deductible_vat(user_id)

    def net_sales(self, user_id: int)-> int:
        sale_rows = self._sales_repository.get_all_sale_rows(user_id)
        return self.total_vatless_amount(sale_rows)

    def net_expenses(self, user_id: int)-> int:
        expense_rows = self._expenses_repository.get_all_expense_rows(user_id)
        return self.total_vatless_amount(expense_rows)

    def net_result(self, user_id: int)-> int:
        return self.net_sales(user_id) - self.net_expenses(user_id)

    def total_sales_including_vat(self, user_id: int)-> int:
        sale_rows = self._sales_repository.get_all_sale_rows(user_id)
        return self.total_amount_including_vat(sale_rows)

    def total_expenses_including_vat(self, user_id: int)-> int:
        expense_rows = self._expenses_repository.get_all_expense_rows(user_id)
        return self.total_amount_including_vat(expense_rows)

    def total_amount_including_vat(self, rows: list)-> int:
        total_amount = 0
        for row in rows:
            total_amount += row.amount
        return total_amount
