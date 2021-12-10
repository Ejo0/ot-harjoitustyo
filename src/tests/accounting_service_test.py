from unittest import TestCase
from datetime import date
from services.accounting_service import AccountingService
from services.expense_row_service import ExpenseRowService
from services.sale_row_service import SaleRowService


class TestAccountingService(TestCase):


    def setUp(self) -> None:
        self._accounting_service = AccountingService()
        self._expense_row_service = ExpenseRowService()
        self._sale_row_service = SaleRowService()

        self._expense_row_service.delete_all()
        self._sale_row_service.delete_all()
        self._sale_row_service.create_sale_row(5, date(2000, 5, 5), 10000, 0, "Job 1")
        self._sale_row_service.create_sale_row(3, date(2000, 4, 5), 5000, 0, "Job 2")
        self._sale_row_service.create_sale_row(5, date(2000, 5, 10), 2000, 24, "Job 3")
        self._sale_row_service.create_sale_row(5, date(2000, 1, 1), 10000, 24, "Job 4")
        self._expense_row_service.create_expense_row(5, date(2000, 4, 5), 1000, 24, "Expense 1")
        self._expense_row_service.create_expense_row(5, date(2001, 1, 1), 110, 10, "Expense 2")

    def test_vatless_amount_rounds_vat_correctly(self):
        sale_row = self._sale_row_service.get_sale_row(3)
        vatless_amount = self._accounting_service.vatless_amount(sale_row)
        self.assertEqual(vatless_amount, 1613)
    
    def test_vat_amount_rounds_vat_as_intented(self):
        sale_row = self._sale_row_service.get_sale_row(4)
        vat_amount = self._accounting_service.vat_amount(sale_row)
        self.assertEqual(vat_amount, 1935)
    
    def test_vat_and_vatless_amount_total_is_same_as_amount(self):
        sale_row = self._sale_row_service.get_sale_row(4)
        vatless_amount = self._accounting_service.vatless_amount(sale_row)
        vat_amount = self._accounting_service.vat_amount(sale_row)
        total_sum = vat_amount + vatless_amount
        self.assertEqual(total_sum, 10000)
    
    def test_net_result_includes_both_sales_and_expenses(self):
        net_result = self._accounting_service.net_result(5)
        self.assertEqual(net_result, 18772)
    
    def test_total_sales_including_vat_calculates_correctly(self):
        total_sales = self._accounting_service.total_sales_including_vat(5)
        self.assertEqual(total_sales, 22000)
    
    def test_date_range_includes_events_from_start_date_and_end_date(self):
        net_result = self._accounting_service.net_result(5, date(2000, 4, 5), date(2000, 5, 5))
        self.assertEqual(net_result, 9194)
    
    def test_total_expenses_including_vat_counts_vat_correctly(self):
        total_amount = self._accounting_service.total_expenses_including_vat(5, None, date(2001, 1, 1))
        self.assertEqual(total_amount, 1110)
    
    def test_vat_payable_gives_correct_amount_from_range(self):
        vat_payable = self._accounting_service.vat_payable(5, None, date(2000, 5, 5))
        self.assertEqual(vat_payable, 1741)
