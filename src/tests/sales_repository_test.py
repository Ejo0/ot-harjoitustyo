import unittest
from models.sale_row import SaleRow
from repositories.sales_repository import SalesRepository


class TestSalesRepository(unittest.TestCase):

    def setUp(self) -> None:
        self._sales_repository = SalesRepository()
        self._sales_repository.delete_all()

    def test_create(self):
        self._sales_repository.create("Phone", 100, 1, 0)
        sale_row = self._sales_repository.get_sale_row(1)
        self.assertEqual(sale_row.id, 1)
        self.assertEqual(sale_row.description, "Phone")
        self.assertEqual(sale_row.amount, 100)
        self.assertEqual(sale_row.user_id, 1)
        self.assertEqual(sale_row.vat, 0)
