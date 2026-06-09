# create and store one Menu
# create and store one Kitchen
# create and store one RestaurantSystem
# store orders in a dictionary by id
# generate the next order id
from backend.src.menu import Menu
from backend.src.kitchen import Kitchen
from backend.src.restaurant_system import RestaurantSystem
from backend.src.order import Order

from backend.src.factory.breakfast_factory import BreakfastFactory
from backend.src.factory.lunch_factory import LunchFactory
from backend.src.factory.dinner_factory import DinnerFactory
from backend.src.factory.dessert_factory import DessertFactory


# Shared backend objects
menu = Menu()
kitchen = Kitchen()
restaurant_system = RestaurantSystem(menu, kitchen)

# In-memory order storage
orders_by_id: dict[int, Order] = {}
next_order_id = 1


def seed_menu() -> None:
    """
    Populate the shared menu one time using the factory classes.
    """
    factories = [
        BreakfastFactory(),
        LunchFactory(),
        DinnerFactory(),
        DessertFactory()
    ]

    for factory in factories:
        items = factory.create_items()
        for item in items:
            menu.add_item(item)


def get_menu() -> Menu:
    """
    Return the shared menu instance.
    """
    return menu


def get_kitchen() -> Kitchen:
    """
    Return the shared kitchen instance.
    """
    return kitchen


def get_restaurant_system() -> RestaurantSystem:
    """
    Return the shared restaurant system instance.
    """
    return restaurant_system


def generate_order_id() -> int:
    """
    Generate and return the next available order ID.
    """
    global next_order_id
    current_id = next_order_id
    next_order_id += 1
    return current_id


def save_order(order: Order) -> None:
    """
    Store an order in the in-memory order dictionary.
    """
    orders_by_id[order.get_order_id()] = order


def get_order(order_id: int) -> Order | None:
    """
    Return one order by ID, or None if it does not exist.
    """
    return orders_by_id.get(order_id)


def get_all_orders() -> list[Order]:
    """
    Return all saved orders.
    """
    return list(orders_by_id.values())

seed_menu()