class ExpenseRow:

    def __init__(self, exp_id: int, user_id: int, exp_date, amount: int, vat: int, desc: int, exp_type: str):
        self._id = exp_id
        self._user_id = user_id
        self._date = exp_date # type: datetime.date
        self._amount = amount
        self._vat = vat
        self._description = desc
        self._expense_type = exp_type

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

    @property
    def expense_type(self):
        return self._expense_type
