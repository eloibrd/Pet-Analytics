from fastapi import APIRouter

from app.controllers import food_controller


def get_base_controller() -> APIRouter:
    """Provides all controller in a single `APIRouter`

    Returns:
        `APIRouter`: A router encapsulating all controllers
    """
    controller = APIRouter()
    # Include food controller and define the prefix
    controller.include_router(food_controller.controller, tags=["food"], prefix="/food")
    return controller


controller: APIRouter = get_base_controller()
"""An APIRouter providing all the application controllers
"""
