class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer
        bank        the name of the bank
        acnt        the account identifier
        limit       credit limit
        """
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0


    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        """Return name of the bank"""
        return self._bank

    def get_account(self):
        """Return the account identifier"""
        return self._acnt

    def get_limit(self):
        """Return the credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def _set_balance(self, amt):
        """Sets the balance"""
        self._balance = amt

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed, False if denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._set_balance(self._balance+price)
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        self._set_balance(self._balance - amount)


# Child class
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees"""

    _count = 0

    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer
        bank        the name of the bank
        acnt        the account identifier
        limit       credit limit
        apr         annual percentage rate
        """

        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if denied.
        """
        PredatoryCreditCard._count += 1

        if PredatoryCreditCard._count > 10:
            success = super().charge(price+1)
            if not success:
                self._set_balance(self.get_balance() - 6)
            return success
        else:
            success = super().charge(price)
            if not success:
                self._set_balance(self.get_balance() - 5)
            return success

    def process_month(self):
        """Assess monthly interest on outstanding balance"""

        # if positive balance, convert APR to monthly multiplicative factor
        if self.get_balance() > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._set_balance(self.get_balance() * monthly_factor)


my_card = PredatoryCreditCard("John","ABC Bank","234567891010",50000,5)
for i in range(12):
    print('Charge no : ' , i + 1)
    my_card.charge(100)
    print(my_card.get_balance())
