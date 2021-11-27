class SaleRow:

    def __init__(self, event_id: int, user_id: int, event_date, amount: int, vat: int, desc: int):
        self._id = event_id
        self._user_id = user_id
        self._date = event_date # type: datetime.date
        self._amount = amount
        self._vat = vat
        self._description = desc

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._user_id

    @property
    def date(self):
        return self._date

    @property
    def amount(self):
        return self._amount

    @property
    def vat(self):
        return self._vat

    @property
    def description(self):
        return self._description
