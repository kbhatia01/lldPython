from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def work(self):
        pass


class EatableWorker(ABC):

    @abstractmethod
    def eat(self):
        pass


class Human(Worker, EatableWorker):
    def eat(self):
        print('eat')

    def work(self):
        print('work')


class Robot(Worker):
    def work(self):
        print('work')

