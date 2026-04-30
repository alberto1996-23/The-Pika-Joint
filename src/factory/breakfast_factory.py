from typing import List
from menu_item import MenuItem
from factory.menu_factory import MenuFactory


class BreakfastFactory(MenuFactory):
    def create_items(self) -> List[MenuItem]:
        return [
            MenuItem(
                "Exeggcute Sandwich",
                "A muffin sandwich with 2 eggs, sausage, and cheese.",
                "Breakfast",
                3.00
            ),
            MenuItem(
                "Cherubi Pancakes",
                "4 pancakes topped with whipped cream, blueberries, and cherries.",
                "Breakfast",
                4.00
            ),
        ]