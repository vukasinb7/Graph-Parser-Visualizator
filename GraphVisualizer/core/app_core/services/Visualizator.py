from abc import ABC, abstractmethod


class Visualizator(ABC):

    @abstractmethod
    def __init__(self, name, id):
        self.name = name
        self.id = id