from order_item import OrderItem
from strategy.pricing_strategy import PricingStrategy
from strategy.dine_in_strategy import DineInStrategy


class Order:
    def __init__(self, order_id: int, order_type: str, status: str = "New"):
        self.order_id = order_id
        self.order_type = order_type
        self.items: list[OrderItem] = []
        self.status = status
        self.pricing_strategy: PricingStrategy = DineInStrategy()

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    def remove_item(self, item: OrderItem) -> None:
        if item in self.items:
            self.items.remove(item)

    def set_pricing_strategy(self, strategy: PricingStrategy) -> None:
        self.pricing_strategy = strategy

    def calculate_total(self) -> float:
        return self.pricing_strategy.calculate_total(self)

    def submit_order(self) -> None:
        self.status = "Submitted"

    def update_status(self, status: str) -> None:
        self.status = status

    def __str__(self) -> str:
        item_lines = "\n".join(str(item) for item in self.items)
        return (
            f"Order ID: {self.order_id}\n"
            f"Order Type: {self.order_type}\n"
            f"Status: {self.status}\n"
            f"Items:\n{item_lines}\n"
            f"Total: ${self.calculate_total():.2f}"
        )
