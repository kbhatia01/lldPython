from PizzaAddon import PizzaAddon


class Cheese(PizzaAddon):

    def get_price(self):
        return self.pizza.get_price() + 30
