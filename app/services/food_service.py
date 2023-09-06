from abc import ABC, abstractmethod

import app.models.http.food as foodHTTPModels


class FoodServiceInterface(ABC):
    """An Interface to define methods used in Food Service."""

    @abstractmethod
    def create_food_entry(self, payload: foodHTTPModels.CreateFoodEntryPayload) -> str:
        pass
