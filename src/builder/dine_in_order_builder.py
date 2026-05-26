from order import Order
from order_item import OrderItem
from menu_item import MenuItem
from builder.order_builder import OrderBuilder
from strategy.dine_in_strategy import DineInStrategy


class DineInOrderBuilder(OrderBuilder):
    def __init__(self):
        self.currentOrder = self._create_order()

    def _create_order(self) -> Order:
        order = Order(1, "Dine-In")
        order.set_pricing_strategy(DineInStrategy())
        return order

    def reset(self) -> None:
        self.currentOrder = self._create_order()

    def set_order_type(self, order_type: str) -> None:
        self.currentOrder.order_type = order_type

    def add_entree(self, item: MenuItem, quantity: int) -> None:
        self.currentOrder.add_item(OrderItem(item, quantity))

    def add_side(self, item: MenuItem, quantity: int) -> None:
        self.currentOrder.add_item(OrderItem(item, quantity))

    def add_drink(self, item: MenuItem, quantity: int) -> None:
        self.currentOrder.add_item(OrderItem(item, quantity))

    def add_dessert(self, item: MenuItem, quantity: int) -> None:
        self.currentOrder.add_item(OrderItem(item, quantity))

    def build(self) -> Order:
        built_order = self.currentOrder
        self.reset()
        return built_order
