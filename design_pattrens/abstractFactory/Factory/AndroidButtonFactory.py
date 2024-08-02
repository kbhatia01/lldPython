from FactoryAbc import Factory
from design_pattrens.abstractFactory.UiElement.androidButton import AndroidButton


class AndroidButtonFactory(Factory):
    def create(self):
        return AndroidButton()
