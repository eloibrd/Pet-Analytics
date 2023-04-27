from pydantic import BaseModel


class FoodTags(BaseModel):
    """The tags for a `FoodSchema`.
    TODO: JSONable interface

    Args:
        - brand : `int` - The food brand.
    """

    brand: str
