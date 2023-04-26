from pydantic import BaseModel


class GetFoodResponse(BaseModel):
    """Response model for GET /api/food route.
    Implements pydantic for data validation.
    """

    message: str
    """The message to send in the payload.
    """
