from pydantic import BaseModel


class CreateFoodEntryResponse(BaseModel):
    """Response model for GET /api/food route.
    Implements pydantic for data validation.
    """

    message: str
    """The message to send in the payload.
    """
