from backend.src.command.command import Command
from backend.src.order import Order

class SubmitOrderCommand(Command):
    def __init__(self, order: Order):
        self.__order = order

    def execute(self) -> None:
        self.__order.submit_order()