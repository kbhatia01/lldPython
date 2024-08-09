from PizzaAddon import PizzaAddon


class Panner(PizzaAddon):

    def get_price(self):
        return self.pizza.get_price() +50