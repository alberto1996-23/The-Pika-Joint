class MenuItem:
    def __init__(self, name: str, description: str, category: str, base_price: float):
        self.__name = name
        self.__description = description
        self.__category = category
        self.__base_price = base_price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def category(self) -> str:
        return self.__category

    @property
    def base_price(self) -> float:
        return self.__base_price

    def get_price(self) -> float:
        return self.__base_price

    def get_description(self) -> str:
        return self.__description

    def __str__(self) -> str:
        return f"{self.__name} ({self.__category}) - ${self.__base_price:.2f}"