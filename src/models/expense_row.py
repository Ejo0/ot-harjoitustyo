class ExpenseRow:
    """An instance of an ExpenseRow represents one expense event in bookkeeping.
    """

    def __init__(self, exp_id: int, user_id: int, exp_date, amount: int, vat: int, desc: int, exp_type: str):
        """Constuctor of ExpenseRow, all values to attributes are set based on args.

        Args:
            exp_id (int): Individual id of SQL row this instance represesnts
            user_id (int): Id of the user this event belongs
            exp_date ([type]): Date of event
            amount (int): Amount of event in cents
            vat (int): Vat percentage of the row. Eg. value for 24% vat is 24
            desc (int): Description of the expense event. Eg. 'Work laptop'
            exp_type (str): Type of the expense, eg. 'other_deductible'
        """
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
