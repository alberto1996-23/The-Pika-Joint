from factory.breakfast_factory import BreakfastFactory
from factory.lunch_factory import LunchFactory
from factory.dinner_factory import DinnerFactory
from factory.dessert_factory import DessertFactory
from menu_item import MenuItem

def test_breakfast_factory_creates_breakfast_items():
    factory = BreakfastFactory()
    items = factory.create_items()

    assert len(items) > 0
    assert all(isinstance(item, MenuItem) for item in items)
    assert all(item.category == "Breakfast" for item in items)

def test_lunch_factory_creates_lunch_items():
    factory = LunchFactory()
    items = factory.create_items()

    assert len(items) > 0
    assert all(item.category == "Lunch" for item in items)