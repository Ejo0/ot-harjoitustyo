from datetime import date
from repositories.sales_repository import SalesRepository


class SaleRowService:
    """Interface for GUI to interact with Sales-table (SQL-database)
    """

    def __init__(self) -> None:
        """Constructor, SalesRepository-object (that actually communicates with the database) is initialized
        """
        self._sales_repository = SalesRepository()

    def rows_sorted_by_date(self, user_id: int, start_date: date = None, end_date: date = None, is_reverse=False):
        """Returns sales of an user from given range, ordered by date

        Args:
            user_id (int): ID of user
            start_date (date, optional): Start date of range. Defaults to None.
            end_date (date, optional): End date of range. Defaults to None.
            is_reverse (bool, optional): If true, reversed order is used. Defaults to False.

        Returns:
            [type]: A list of SaleRow-objects
        """
        sale_rows = self._sales_repository.get_sale_rows_from_range(user_id, start_date, end_date)
        return sorted(sale_rows, key=lambda row: row.date, reverse=is_reverse)

    def create_sale_row(self, user_id: int, event_date: date,
                        amount: int, vat: int, description: str):
        """Creates new sale event to Sales-table

        Args:
            user_id (int): Id of user
            event_date (date): Date of the sale event
            amount (int): Total amount of sale in cents, vat included
            vat (int): Vat percentage of sale
            description (str): Description of sale event
        """

        self._sales_repository.create(
            user_id, event_date, amount, vat, description)

    def delete_all(self):
        """Deletes all rows from Sales table
        """
        self._sales_repository.delete_all()
