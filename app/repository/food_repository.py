from abc import ABC, abstractmethod

from app.models.food import Food


class FoodRepositoryInterface(ABC):
    """An Interface to define methods used in Food Repository."""

    @abstractmethod
    def save_food_entry(self, food_entry: Food) -> str:
        pass
