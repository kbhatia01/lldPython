from PizzaAddon import PizzaAddon

class Mushroom(PizzaAddon):

    def get_price(self):
        return self.pizza.get_price() + 20
