from app.models.food import Food
from app.repository.food_repository import FoodRepositoryInterface


class FoodRepositoryImpl(FoodRepositoryInterface):
    """An Implementation of `FoodRepositoryInterface`.
    Provides methods to interact with the database concerning Food.
    """

    def save_food_entry(self, food_entry: Food):
        """Insert an entry for food in database.

        Given:
            - quantity: fetched from the payload
            - date: assuming the entry is to be set now
        """
        # @todo
