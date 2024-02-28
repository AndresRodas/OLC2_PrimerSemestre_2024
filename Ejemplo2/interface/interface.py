from abc import ABC, abstractmethod

class Persona(ABC):

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def caminar(self):
        pass
