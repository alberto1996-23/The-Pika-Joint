from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_total(self, order: Order) -> float:
        pass
        
