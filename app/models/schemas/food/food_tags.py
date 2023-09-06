from pydantic import BaseModel


class FoodTags(BaseModel):
    """The tags for a `FoodSchema`.

    Args:
        - brand : `int` - The food brand.
    """

    brand: str
