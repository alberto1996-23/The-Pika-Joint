from backend.src.menu_item import MenuItem


class OrderItem:
    def __init__(
        self,
        menu_item: MenuItem,
        quantity: int,
        selected_size: str = "",
        special_instructions: str = ""
    ):
        self.__menu_item = menu_item
        self.__quantity = quantity
        self.__selected_size = selected_size
        self.__special_instructions = special_instructions

    @property
    def menu_item(self) -> MenuItem:
        return self.__menu_item

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def selected_size(self) -> str:
        return self.__selected_size

    @property
    def special_instructions(self) -> str:
        return self.__special_instructions

    def get_subtotal(self) -> float:
        return self.__menu_item.get_price() * self.__quantity

    def get_menu_item(self) -> MenuItem:
        return self.__menu_item

    def __str__(self) -> str:
        details = f"{self.__menu_item.name} x{self.__quantity}"
        if self.__selected_size:
            details += f" [{self.__selected_size}]"
        if self.__special_instructions:
            details += f" - Notes: {self.__special_instructions}"
        details += f" -> ${self.get_subtotal():.2f}"
        return details
