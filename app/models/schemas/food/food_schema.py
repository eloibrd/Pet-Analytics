from datetime import datetime

from pydantic import BaseModel

from app.models.schemas.food.food_fields import FoodFields
from app.models.schemas.food.food_tags import FoodTags


class FoodSchema(BaseModel):
    """The schema to insert food in the influx database.
    TODO: JSONable interface

    Args:
        - measurement: str - const value "Food"
        - tags: `FoodTags` - the tags to apply to the entry
        - time: datetime - const value datetime.now()
        - fields: `FoodFields` - the entry fields
    """

    measurement: str = "Food"
    tags: FoodTags
    time: datetime = datetime.now()
    fields: FoodFields

    def __init__(self, brand: str, quantity: int):
        self.tags = FoodTags(brand=brand)
        self.fields = FoodFields(quantity=quantity)
