from menu import Menu
from kitchen import Kitchen
from restaurant_system import RestaurantSystem
from menu_item import MenuItem
from order_item import OrderItem
from order import Order


def main():
    menu = Menu()
    kitchen = Kitchen()
    restaurant_system = RestaurantSystem(menu, kitchen)

    burger = MenuItem("Pika Patty", "Burger with toppings", "Lunch", 5.00)
    fries = MenuItem("Fries", "Crispy fries", "Side", 2.00)

    menu.add_item(burger)
    menu.add_item(fries)

    order = Order(1, "Dine-In")
    order.add_item(OrderItem(burger, 2))
    order.add_item(OrderItem(fries, 1))

    restaurant_system.place_order(order)
    restaurant_system.send_to_kitchen(order)

    print(order)
    print("\nKitchen Orders:")
    for kitchen_order in kitchen.get_active_orders():
        print(f"Order {kitchen_order.order_id} - {kitchen_order.status}")


if __name__ == "__main__":
    main()
