from pydantic import BaseModel


class FoodFields(BaseModel):
    """The fields for a `FoodSchema`.
    TODO: JSONable interface

    Args:
        - quantity : `int` - The food quantity for the entry.
    """

    quantity: int
