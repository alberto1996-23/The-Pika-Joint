from menu_item import MenuItem
from order_item import OrderItem
from order import Order
from strategy.dine_in_strategy import DineInStrategy
from strategy.take_out_strategy import TakeOutStrategy
from strategy.delivery_strategy import DeliveryStrategy


def main():
    burger = MenuItem("Pika Patty", "Burger with toppings", "Lunch", 5.00)
    fries = MenuItem("Fries", "Crispy fries", "Side", 2.00)

    order = Order(1, "Delivery")
    order.add_item(OrderItem(burger, 2))
    order.add_item(OrderItem(fries, 1))

    order.set_pricing_strategy(DeliveryStrategy())
    print(order)

    order.set_pricing_strategy(DineInStrategy())
    print("\nDine-In Total:")
    print(f"${order.calculate_total():.2f}")

    order.set_pricing_strategy(TakeOutStrategy())
    print("\nTakeout Total:")
    print(f"${order.calculate_total():.2f}")


if __name__ == "__main__":
    main()
