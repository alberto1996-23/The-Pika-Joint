from abc import ABC, abstractmethod
from typing import List
from menu_item import MenuItem


class MenuCategoryFactory(ABC):
    @abstractmethod
    def create_items(self) -> List[MenuItem]:
        pass
