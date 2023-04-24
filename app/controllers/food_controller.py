from fastapi import APIRouter


def get_food_controller() -> APIRouter:
    """Provides routes for managing food

    Returns:
        APIRouter: A router encapsulating food related operations
    """
    controller = APIRouter()

    @controller.get("/")
    async def get():
        return {"message": "hello world"}

    return controller


controller: APIRouter = get_food_controller()
"""A router providing food related operations
"""
