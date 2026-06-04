from menu import Menu
from kitchen import Kitchen
from restaurant_system import RestaurantSystem
from menu_item import MenuItem
from order_item import OrderItem
from order import Order

from command.order_controller import OrderController
from command.place_order_command import PlaceOrderCommand
from command.submit_order_command import SubmitOrderCommand
from command.send_to_kitchen_command import SendToKitchenCommand
from command.prepare_order_command import PrepareOrderCommand
from command.mark_order_ready_command import MarkOrderReadyCommand

from observer.customer_display import CustomerDisplay
from observer.kitchen_display import KitchenDisplay
from observer.cashier_display import CashierDisplay

def test_full_order_flow(capsys):
    menu = Menu()
    kitchen = Kitchen()
    system = RestaurantSystem(menu, kitchen)
    controller = OrderController()

    burger = MenuItem("Pika Patty", "Burger", "Lunch", 5.00)
    fries = MenuItem("Fries", "Side", "Side", 2.00)

    menu.add_item(burger)
    menu.add_item(fries)

    order = Order(1, "Dine-In")
    order.add_item(OrderItem(burger, 2))
    order.add_item(OrderItem(fries, 1))

    order.attach(CustomerDisplay(order))
    order.attach(KitchenDisplay(order))
    order.attach(CashierDisplay(order))

    controller.set_command(PlaceOrderCommand(system, order))
    controller.run_command()

    controller.set_command(SubmitOrderCommand(order))
    controller.run_command()

    controller.set_command(SendToKitchenCommand(system, order))
    controller.run_command()

    controller.set_command(PrepareOrderCommand(order))
    controller.run_command()

    controller.set_command(MarkOrderReadyCommand(order))
    controller.run_command()

    assert order.status == "Ready"
    assert system.track_order(1) == order
    assert order in kitchen.get_active_orders()

    output = capsys.readouterr().out
    assert "Submitted" in output
    assert "In Kitchen" in output
    assert "Preparing" in output
    assert "Ready" in output