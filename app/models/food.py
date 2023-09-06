from datetime import datetime


class Food:
    """The generic class to represent a food entry.

    Args:
        - quantity : `int` - The food quantity for the entry.
        - date : `DateTime` - The date of the input.
    """

    quantity: int
    date: datetime

    def __init__(self, quantity: int, date: datetime):
        self.quantity = quantity
        self.date = date
