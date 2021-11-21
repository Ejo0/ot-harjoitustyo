class SaleRow:

    def __init__(self, row_id : int, description: str, amount: int, user_id: int, vat: int) -> None:
        self._id = row_id
        self._description = description
        self._amount = amount
        self._user_id = user_id
        self._vat = vat

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def amount(self):
        return self._amount

    @property
    def user_id(self):
        return self._user_id

    @property
    def vat(self):
        return self._vat

    def __str__(self) -> str:
        amount_in_euros = self.amount / 100.0
        return f"{self.id}. {amount_in_euros:>10.2f} euroa {self.description:>10}"
