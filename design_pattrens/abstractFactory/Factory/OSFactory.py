from design_pattrens.abstractFactory.Factory.AbstractAndroidFactory import AbstractAndroidFactory


class OSFactory:
    def decide(self, val):
        if val == "Android":
            return AbstractAndroidFactory()
