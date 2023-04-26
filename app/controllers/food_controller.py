from fastapi import APIRouter

from app.models.food.responses.get_food_response import GetFoodResponse
from app.services.food_service import get_food_service


def get_food_controller() -> APIRouter:
    """Provides routes for managing food

    Returns:
        APIRouter: A router encapsulating food related operations
    """
    controller = APIRouter()

    @controller.get(
        "/",
        name="food:get food",
        summary="GET food",
        response_model=GetFoodResponse,
    )
    async def get_food():
        return {"message": get_food_service().get_food()}

    return controller


controller: APIRouter = get_food_controller()
"""A router providing food related operations
"""
