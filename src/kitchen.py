from order import Order

class Kitchen:
    def __init__(self):
        self.__active_orders: list[Order] = []

    def get_active_orders(self) -> list[Order]:
        return self.__active_orders

    def receive_order(self, order: Order) -> None:
        self.__active_orders.append(order)
        order.update_status("In Kitchen")

    def prepare_order(self, order: Order) -> None:
        order.update_status("Preparing")

    def mark_order_ready(self, order: Order) -> None:
        order.update_status("Ready")