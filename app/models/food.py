from datetime import datetime


class Food:
    """The generic class to represent a food entry.

    Args:
        - quantity : `int` - The food quantity for the entry.
        - date : `DateTime` - The date of the input.
        - brand : `str` - The food brand for the input.
    """

    quantity: int
    date: datetime
    brand: str
