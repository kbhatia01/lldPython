from abc import ABC, abstractmethod

from design_pattrens.observerDp.subject.subject import Subject


class Observer(ABC):

    @abstractmethod
    def update(self, temp, humidity):
        pass

    def registerSubject(self, subject: Subject):
        subject.register(self)

    def unregisterSubject(self, subject):
        subject.unregister(self)
