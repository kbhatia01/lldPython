from design_pattrens.prototype.Monstor import Monstor
import copy


class Sword:
    pass


class Zombie(Monstor):

    def __init__(self, health):
        self.health = health


    def attack(self):
        print("attacking..")

    def clone(self):
        return copy.deepcopy(self)
