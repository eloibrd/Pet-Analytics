from pydantic import BaseModel


class CreateFoodEntryPayload(BaseModel):
    """The fields required in a food entry creation payload.

    Args:
        - quantity : `int` - The food quantity for the entry.
    """

    quantity: int
    """The food quantity for the entry."""
