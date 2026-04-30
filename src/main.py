from factory.breakfast_factory import BreakfastFactory
from factory.lunch_factory import LunchFactory
from factory.dinner_factory import DinnerFactory
from factory.dessert_factory import DessertFactory


def print_category(title: str, items):
    print(f"\n{title}")
    print("-" * len(title))
    for item in items:
        print(item)


def main():
    breakfast_factory = BreakfastFactory()
    lunch_factory = LunchFactory()
    dinner_factory = DinnerFactory()
    dessert_factory = DessertFactory()

    breakfast_items = breakfast_factory.create_items()
    lunch_items = lunch_factory.create_items()
    dinner_items = dinner_factory.create_items()
    dessert_items = dessert_factory.create_items()

    print_category("Breakfast Menu", breakfast_items)
    print_category("Lunch Menu", lunch_items)
    print_category("Dinner Menu", dinner_items)
    print_category("Dessert Menu", dessert_items)


if __name__ == "__main__":
    main()