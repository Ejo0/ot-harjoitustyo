import unittest
from datetime import date
from services.sale_row_service import SaleRowService

class TestSaleRowService(unittest.TestCase):

    def setUp(self) -> None:
        self._sale_row_service = SaleRowService()
        self._sale_row_service.delete_all()
        self._sale_row_service.create_sale_row(5, date(2000, 5, 5), 10000, 0, "Phone")
        self._sale_row_service.create_sale_row(3, date(2000, 4, 5), 5000, 0, "Book")
        self._sale_row_service.create_sale_row(5, date(2000, 5, 10), 2000, 24, "Ticket")
        self._sale_row_service.create_sale_row(5, date(2000, 1, 1), 10000, 24, "Computer")
    
    def test_rows_sorted_by_date_reversed_gives_correct_order(self):
        sales = self._sale_row_service.rows_sorted_by_date(5, True)
        self.assertEqual(sales[0].description, "Ticket")
        self.assertEqual(sales[1].amount, 10000)
    
    def test_delete_all_deletes_all(self):
        self._sale_row_service.delete_all()
        all_sales = self._sale_row_service.rows_sorted_by_date(3)
        all_sales += self._sale_row_service.rows_sorted_by_date(5)
        self.assertEqual(len(all_sales), 0)