from design_pattrens.observerDp.observers.observer import Observer


class Zomato(Observer):

    def update(self, temp, hum):
        if hum > 20:
            print("Zomato updated price of delivery..")

        if hum <=20:
            print("Zomato updated price increased already increase of delivery..")
