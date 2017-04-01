class Flower:
    """Class representing features of a flower"""

    def __init__(self, name = 'rose', petals = '6', price = '100.00'):
        """
        Create an instance of Flower

        name:       name of the flower
        petals:     number of petals
        price:      price of the flower
        """
        self._name = name
        self._petals = petals
        self._price = price

    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price

    def set_name(self):
        return self._name

    def set_petals(self):
        return self._petals

    def set_price(self):
        return self._price

