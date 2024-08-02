from knight import Knight, KnightV2
from archer import Archer
from abc import ABC, abstractmethod


class PlayerFactory(ABC):
    @abstractmethod
    def create_player(self):
        pass


class KnightFactory:
    def create_player(self):
        return KnightV2()


class ArcherFactory:
    def create_player(self):
        return Archer()
