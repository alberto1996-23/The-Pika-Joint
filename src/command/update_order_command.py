from command.command import Command
from order import Order

class UpdateOrderStatusCommand(Command):
    def __init__(self, order: Order, new_status: str):
        self.__order = order
        self.__new_status = new_status

    def execute(self) -> None:
        self.__order.update_status(self.__new_status)