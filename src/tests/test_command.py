from menu import Menu
from kitchen import Kitchen
from restaurant_system import RestaurantSystem
from order import Order
from command.order_controller import OrderController
from command.place_order_command import PlaceOrderCommand
from command.submit_order_command import SubmitOrderCommand

def test_submit_order_command_changes_status():
    order = Order(1, "Dine-In")
    controller = OrderController()

    controller.set_command(SubmitOrderCommand(order))
    controller.run_command()

    assert order.status == "Submitted"

def test_place_order_command_adds_order_to_system():
    menu = Menu()
    kitchen = Kitchen()
    system = RestaurantSystem(menu, kitchen)
    order = Order(1, "Dine-In")
    controller = OrderController()

    controller.set_command(PlaceOrderCommand(system, order))
    controller.run_command()

    assert system.track_order(1) == order