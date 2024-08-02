from FactoryAbc import Factory
from design_pattrens.abstractFactory.UiElement.IosButton import IosButton


class IosButtonFactory(Factory):

    def create(self):
        return IosButton()
