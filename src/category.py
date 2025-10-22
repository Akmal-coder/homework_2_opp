from abc import ABC, abstractmethod

from src.order import Countable
from src.product import Product


class Category(Countable):
    """Абстрактный класс для объектов, которые могут содержать продукты"""

    @abstractmethod
    def __init__(self):
        pass  # Не инициализируем атрибуты здесь

    @abstractmethod
    def add_product(self, product):
        pass

    @property
    @abstractmethod
    def total_quantity(self):
        pass


class Category(Countable):
    """Класс, относящий продукт к определенной категории"""

    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        super().__init__()  # Инициализация абстрактного класса
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    def __iter__(self):
        """Делает категорию итерируемой через генератор"""
        for product in self.products_in_list:
            yield product

    @property
    def products(self):
        """Property для строкового представления продуктов"""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_in_list(self):
        """Property для доступа к списку продуктов"""
        return self.__products

    @property
    def total_quantity(self):
        """Общее количество товаров в категории"""
        return sum(product.quantity for product in self.__products)
