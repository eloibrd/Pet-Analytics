from app.services.food_service import FoodServiceInterface


class FoodServiceImpl(FoodServiceInterface):
    """An Implementation of `FoodServiceInterface`.
    Provides methods to interact with food.
    """

    def get_food(self) -> str:
        """Fetch food

        Returns:
            str: food representation
        """
        return "Food str"
