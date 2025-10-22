from abc import ABC, abstractmethod


class Countable(ABC):
    """Абстрактный класс для объектов, которые могут содержать продукты"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_product(self, product):
        pass

    @property
    @abstractmethod
    def total_quantity(self):
        pass
