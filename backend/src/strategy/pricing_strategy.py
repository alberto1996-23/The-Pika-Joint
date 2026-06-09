from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.src.order import Order

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_total(self, order: "Order") -> float:
        raise NotImplementedError
        
