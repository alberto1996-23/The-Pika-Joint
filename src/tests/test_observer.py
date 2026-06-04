from order import Order
from observer.customer_display import CustomerDisplay
from observer.kitchen_display import KitchenDisplay
from observer.cashier_display import CashierDisplay

def test_observers_are_notified_on_state_change(capsys):
    order = Order(1, "Dine-In")

    order.attach(CustomerDisplay(order))
    order.attach(KitchenDisplay(order))
    order.attach(CashierDisplay(order))

    order.submit_order()

    captured = capsys.readouterr()
    output = captured.out

    assert "[Customer Display]" in output
    assert "[Kitchen Display]" in output
    assert "[Cashier Display]" in output
    assert "Submitted" in output