from app.repository.food_repository import FoodRepositoryInterface
from app.services.food_service import FoodServiceInterface


def get_food_service() -> FoodServiceInterface:
    """Dependency injector for food service.

    Returns:
        FoodServiceInterface: An implementation of `FoodServiceInterface`.
    """
    from app.services.impl.food_service_impl import FoodServiceImpl

    return FoodServiceImpl()


def get_food_repository() -> FoodRepositoryInterface:
    """Dependency injector for food repository.

    Returns:
        FoodRepositoryInterface: An implementation of `FoodServiceInterface`.
    """
    from app.repository.impl.food_repository_impl import FoodRepositoryImpl

    return FoodRepositoryImpl()
