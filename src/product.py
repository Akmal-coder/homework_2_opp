from abc import ABC, abstractmethod


class ReprMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        # Сначала вызываем следующий класс в цепочке MRO
        super().__init__(*args, **kwargs)
        # После инициализации логируем создание объекта
        print(f"Создан объект {self.__class__.__name__}{self.__repr__()}")

    def __repr__(self):
        """Магический метод для представления объекта"""
        attributes = []
        for attr, value in self.__dict__.items():
            # Показываем только публичные атрибуты (без _ и __)
            if not attr.startswith("_"):
                attributes.append(f"{attr}={value}")
        return f"({', '.join(attributes)})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_dict):
        pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        elif self.__price >= new_price:
            self.__price = new_price
        else:
            raise PermissionError("Требуется подтверждение для увеличения цены")


class Product(ReprMixin, BaseProduct):
    """Класс, описывающий продукт"""

    def __init__(self, name, description, price, quantity):
        # Используем super() который пройдет по MRO: ReprMixin -> BaseProduct
        super().__init__(
            name=name, description=description, price=price, quantity=quantity
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_dict):
        return cls(**product_dict)


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
