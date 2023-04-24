from abc import ABC, abstractmethod


class FoodService(ABC):
    @abstractmethod
    def get_food(self):
        pass
