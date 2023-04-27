from app.services.food_service import FoodServiceInterface


class FoodServiceImpl(FoodServiceInterface):
    """An Implementation of `FoodServiceInterface`.
    Provides methods to interact with food.
    """

    def create_food_entry(self) -> str:
        """Insert an entry for food in database.

        Returns:\n
            str: created food representation
        """
        return "Food str"
