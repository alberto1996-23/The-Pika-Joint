from command.command import Command
from order import Order
from restaurant_system import RestaurantSystem


class SendToKitchenCommand(Command):
    def __init__(self, restaurant_system: RestaurantSystem, order: Order):
        self.__restaurant_system = restaurant_system
        self.__order = order

    def execute(self) -> None:
        self.__restaurant_system.send_to_kitchen(self.__order)