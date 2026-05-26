from strategy.pricing_strategy import PricingStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from order import Order

class DeliveryStrategy(PricingStrategy):
    def calculate_total(self, order: "Order") -> float:
        total = sum(item.get_subtotal() for item in order.items)
        delivery_fee = 3.50
        return total + delivery_fee
