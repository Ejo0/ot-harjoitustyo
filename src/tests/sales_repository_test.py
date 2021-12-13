import unittest
from datetime import date
from repositories.sales_repository import SalesRepository


class TestSalesRepository(unittest.TestCase):

    def setUp(self) -> None:
        self._sales_repository = SalesRepository()
        self._sales_repository.delete_all()
        self._sales_repository.create(1, date(2021, 1, 3), 10000, 0, "Phone")
        self._sales_repository.create(1, date(2021, 2, 2), 25050, 24, "Computer")

    def test_create(self):
        self._sales_repository.create(4, date(2021, 12, 30), 7000, 0, "Tools")
        sale_row = self._sales_repository.get_sale_rows_from_range(4, None, None)[0]
        self.assertEqual(sale_row.user_id, 4)
        self.assertEqual(sale_row.id, 3)

    def test_get_sale_rows_from_range_returns_sales_with_correct_values(self):
        sale_row = self._sales_repository.get_sale_rows_from_range(1, None, None)[0]
        self.assertEqual(sale_row.id, 1)
        self.assertEqual(sale_row.user_id, 1)
        self.assertEqual(sale_row.date.day, 3)
        self.assertEqual(sale_row.amount, 10000)
        self.assertEqual(sale_row.vat, 0)
        self.assertEqual(sale_row.description, "Phone")

    def test_get_sale_rows_without_range(self):
        sale_rows = self._sales_repository.get_sale_rows_from_range(1, None, None)
        self.assertEqual(len(sale_rows), 2)
        self.assertEqual(sale_rows[1].amount, 25050)

    def test_total_amount(self):
        total = self._sales_repository.total_amount(1, None, None)
        self.assertEqual(total, 35050)

    def test_delete_all(self):
        self._sales_repository.delete_all()
        sale_rows = self._sales_repository.get_sale_rows_from_range(1, None, None)
        self.assertEqual(len(sale_rows), 0)
