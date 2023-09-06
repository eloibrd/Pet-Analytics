from datetime import datetime

from fastapi import HTTPException

import app.models.http.food as foodHTTPModels
from app.core.deps import get_food_repository
from app.models.food import Food
from app.services.food_service import FoodServiceInterface


class FoodServiceImpl(FoodServiceInterface):
    """An Implementation of `FoodServiceInterface`.
    Provides methods to interact with food.
    """

    def create_food_entry(self, payload: foodHTTPModels.CreateFoodEntryPayload):
        """Insert an entry for food in database.

        Given:
            - quantity: fetched from the payload
            - date: assuming the entry is to be set now
        """

        food_entry: Food = Food(quantity=payload.quantity, date=datetime.now())

        try:
            get_food_repository().save_food_entry(food_entry=food_entry)
        except:
            HTTPException(status_code=500, detail="Insert in database failed.")
