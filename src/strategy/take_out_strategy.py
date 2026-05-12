from strategy.pricing_strategy import PricingStrategy

class TakeOutStrategy(PricingStrategy):
    def calculate_total(self, order: Order) -> float:
        total = 0.0
        for item in order.items:
            total += item.get_subtotal()
        return total
