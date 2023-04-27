import logging

from fastapi import APIRouter

import app.schemas.food as foodModels
from app.services.food_service import get_food_service


def get_food_controller() -> APIRouter:
    """Provides routes for managing food

    Returns:
        APIRouter: A router encapsulating food related operations
    """
    controller = APIRouter()

    @controller.post(
        "/",
        name="food:create food entry",
        summary="CREATE food entry",
        response_model=foodModels.CreateFoodEntryResponse,
    )
    async def create_food_entry():
        """Route to insert a food entry in database.

        Returns: \n
            HTTP response: 201 Created if succeed. \n
            HTTP response: 400 Bad Request if bad request payload. \n
            HTTP response: 401 Unauthorized if not authenticated TODO. \n
        """

        # TODO: make it work
        logging.info("Create a new food point in database")
        return foodModels.CreateFoodEntryResponse(
            message=get_food_service().create_food_entry()
        )

    return controller


controller: APIRouter = get_food_controller()
"""A router providing food related operations
"""
