from FactoryAbc import Factory
from design_pattrens.abstractFactory.UiElement.AndroidCheckbox import  Checkbox


class AndroidCheckboxFactory(Factory):
    def create(self):
        return Checkbox()
