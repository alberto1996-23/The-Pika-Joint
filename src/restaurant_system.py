from menu import Menu
from kitchen import Kitchen
from order import Order

class RestaurantSystem:
    def __init__(self, menu: Menu, kitchen: Kitchen):
        self.__menu = menu
        self.__kitchen = kitchen
        self.__orders: list[Order] = []

    def place_order(self, order: Order) -> None:
        self.__orders.append(order)

    def send_to_kitchen(self, order: Order) -> None:
        self.__kitchen.receive_order(order)

    def track_order(self, order_id: int) -> Order | None:
        for order in self.__orders:
            if order.order_id == order_id:
                return order
        return None

    def display_menu(self) -> None:
        self.__menu.display_menu()