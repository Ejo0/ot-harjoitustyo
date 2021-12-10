from datetime import date
from repositories.expenses_repository import ExpensesRepository
from repositories.sales_repository import SalesRepository


class AccountingService:
    """A service that is responsible of calculating different kind of values
    from bookkeeping-data.
    """

    def __init__(self) -> None:
        """Constructor, ExpensesRepository and SalesRepository are initialized,
        used by functions to get data from database.
        """
        self._expenses_repository = ExpensesRepository()
        self._sales_repository = SalesRepository()

    def vatless_amount(self, row) -> int:
        """Calculates vatless amount of a row. For example, if (total) amount of a row is
        124 and vat-percentage is 24%, the vatless amount is 100

        Args:
            row (type can be ExpenseRow or SaleRow): ExpenseRow or SaleRow

        Returns:
            int: Vatless amount of the row.
        """
        vatless_amount = row.amount / ((100 + row.vat) * 0.01)
        return int(round(vatless_amount, 0))

    def vat_amount(self, row) -> int:
        """Calculates vat amount of a row. Eg. total amount 124 and vat is 24%,
        the vat amount is 24

        Args:
            row (): ExpenseRow or SaleRow

        Returns:
            int: Vat amount of the row
        """
        vatless_amount = self.vatless_amount(row)
        return row.amount - vatless_amount

    def total_vatless_amount(self, rows: list) -> int:
        """Calculates total vatless amount of events in given list. (eg. list of 5 ExpenseRows).
        To avoid rounding problems, vatless amount is calculated from each row and results are added to output.

        Args:
            rows (list): list of SaleRows or ExpenseRows

        Returns:
            int: Total vatless amount of events in given list
        """
        total_vatless_amount = 0
        for row in rows:
            total_vatless_amount += self.vatless_amount(row)
        return total_vatless_amount

    def total_vat(self, rows: list) -> int:
        """Calculates total vat amount of events in given list.

        Args:
            rows (list): list of SaleRows or ExpenseRows

        Returns:
            int: Total vat amount of events in given list
        """
        total_vat = 0
        for row in rows:
            total_vat += self.vat_amount(row)
        return total_vat

    def vat_on_sales(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        """Calculates total vat of SaleRows of an user from given date-range.

        Args:
            user_id (int): Id of the user
            start_date (date, optional): Inclusive start date of the range. Defaults to None.
            end_date (date, optional): Inclusive end date of the range. Defaults to None.

        Returns:
            int: Total vat of SaleRows
        """
        sale_rows = self._sales_repository.get_sale_rows_from_range(
            user_id, start_date, end_date)
        return self.total_vat(sale_rows)

    def deductible_vat(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        """Calculates total vat of ExpenseRows of an user from given date-range.

        Args:
            user_id (int): User_id
            start_date (date, optional): Start date of range. Defaults to None.
            end_date (date, optional): End date of range. Defaults to None.

        Returns:
            int: Total vat of ExpenseRows
        """
        expense_rows = self._expenses_repository.get_expense_rows_from_range(
            user_id, start_date, end_date
        )
        return self.total_vat(expense_rows)

    def vat_payable(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        """Calculates vat amount of an user to be paid to Tax authority from given range.
        The amount is equal to 'vat on sales' - 'deductible vat'

        Args:
            user_id (int): User id
            start_date (date, optional): Start date of range. Defaults to None.
            end_date (date, optional): End date of range. Defaults to None.

        Returns:
            int: Vat payable to Tax authority
        """
        vat_on_sales_amount = self.vat_on_sales(user_id, start_date, end_date)
        deductible_vat_amount = self.deductible_vat(user_id, start_date, end_date)
        return vat_on_sales_amount - deductible_vat_amount

    def net_sales(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        """Calculates total sales (from accounting perspective) of an user from given range.
        That means the sum of the vatless amount of each sale.

        Args:
            user_id (int): User ID
            start_date (date, optional): Start date of range. Defaults to None.
            end_date (date, optional): End date of range. Defaults to None.

        Returns:
            int: Net (vatless) amount of sales
        """
        sale_rows = self._sales_repository.get_sale_rows_from_range(
            user_id, start_date, end_date)
        return self.total_vatless_amount(sale_rows)

    def net_expenses(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        """Calculates total expenses (vatless amount) of an user from given range.

        Args:
            user_id (int): User ID
            start_date (date, optional): Start date of range. Defaults to None.
            end_date (date, optional): End date of range. Defaults to None.

        Returns:
            int: Net (vatless) amount of expenses
        """
        expense_rows = self._expenses_repository.get_expense_rows_from_range(
            user_id, start_date, end_date)
        return self.total_vatless_amount(expense_rows)

    def net_result(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        """Calculates net result of user from given range.
        The amount is equal to 'turnover' - 'deductible vat' (vatless sales - vatless expenses)

        Args:
            user_id (int): User ID
            start_date (date, optional): Start date of range. Defaults to None.
            end_date (date, optional): End date of range. Defaults to None.

        Returns:
            int: Net result
        """
        net_sales_amount = self.net_sales(user_id, start_date, end_date)
        net_expenses_amount = self.net_expenses(user_id, start_date, end_date)
        return net_sales_amount - net_expenses_amount

    def total_sales_including_vat(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        """Returns total amount of sales including vat. Calculation is done by SalesRepository

        Args:
            user_id (int): User ID
            start_date (date, optional): Start date of range. Defaults to None.
            end_date (date, optional): End date of range. Defaults to None.

        Returns:
            int: Total amount of sales including vat
        """
        return self._sales_repository.total_amount(user_id, start_date, end_date)

    def total_expenses_including_vat(self, user_id: int, start_date: date = None, end_date: date = None) -> int:
        """Returns total amount of money spent on expenses (expenses including vat)

        Args:
            user_id (int): User ID
            start_date (date, optional): Start date of range. Defaults to None.
            end_date (date, optional): End date of range. Defaults to None.

        Returns:
            int: Total expenses including vat
        """
        return self._expenses_repository.total_amount(user_id, start_date, end_date)
