from strategy.pricing_strategy import PricingStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from order import Order

class TakeOutStrategy(PricingStrategy):
    def calculate_total(self, order: "Order") -> float:
        return sum(item.get_subtotal() for item in order.items)
