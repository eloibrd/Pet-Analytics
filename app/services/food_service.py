from abc import ABC, abstractmethod


class FoodServiceInterface(ABC):
    """An Interface to define methods used in Food Service."""

    @abstractmethod
    def create_food_entry(self) -> str:
        pass


def get_food_service() -> FoodServiceInterface:
    """Returns a functionnal food service.

    Returns:
        FoodServiceInterface: An implementation of `FoodServiceInterface`.
    """
    from app.services.impl.food_service_impl import FoodServiceImpl

    return FoodServiceImpl()
