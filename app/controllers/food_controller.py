import logging

from fastapi import APIRouter, Response, status

import app.models.http.food as foodHTTPModels
from app.core.deps import get_food_service


def get_food_controller() -> APIRouter:
    """Provides routes for managing food

    Returns:
        APIRouter: A router encapsulating food related operations
    """
    controller = APIRouter()

    @controller.post(
        "/",
        summary="CREATE food entry",
        status_code=status.HTTP_201_CREATED,
    )
    async def create_food_entry(payload: foodHTTPModels.CreateFoodEntryPayload):
        """Route to insert a food entry in database.

        Returns: \n
            HTTP response: 201 Created if succeed. \n
            HTTP response: 422 Unproccessable Entity if bad request payload. \n
            HTTP response: 401 Unauthorized if not authenticated. @todo \n
            HTTP response: 500 Server Error if failed to save entry in database. @todo
        """

        # Log service call
        logging.info("Create a new food point in database")
        # Call to food service to handle the request
        get_food_service().create_food_entry(payload=payload)
        return Response(status_code=status.HTTP_201_CREATED)

    return controller


controller: APIRouter = get_food_controller()
"""A router providing food related operations
"""
