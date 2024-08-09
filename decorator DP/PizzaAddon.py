from pizza import Pizza


class PizzaAddon(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def get_price(self):
        return self.pizza.get_price()
