from typing import List
from menu_item import MenuItem
from factory.menu_factory import MenuFactory


class DinnerFactory(MenuFactory):
    def create_items(self) -> List[MenuItem]:
        return [
            MenuItem(
                "Krabby Legs",
                "Crab legs served with butter and lemon.",
                "Dinner",
                6.00
            ),
            MenuItem(
                "Combusken Pesto Pasta",
                "Penne with pesto and chicken breast.",
                "Dinner",
                8.00
            ),
            MenuItem(
                "Peking Psyduck",
                "Chopped Psyduck with soy sauce and honey, served with ranch.",
                "Dinner",
                9.00
            ),
        ]