from typing import List
from menu_item import MenuItem
from factory.menu_factory import MenuFactory


class LunchFactory(MenuFactory):
    def create_items(self) -> List[MenuItem]:
        return [
            MenuItem(
                "Pika Patty",
                "A Pikachu-themed burger with cheese, onions, lettuce, tomatoes, and condiments.",
                "Lunch",
                5.00
            ),
            MenuItem(
                "Farfetch’d Leek Salad",
                "A salad with cucumbers, chopped leek, and choice of fruits and veggies.",
                "Lunch",
                4.00
            ),
            MenuItem(
                "Fried Magikarp Strips",
                "Fish strips served with chips and a drink choice.",
                "Lunch",
                7.50
            ),
        ]