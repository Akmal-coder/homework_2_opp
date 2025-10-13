class Product:
    """Класс, описывающий продукт"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Можно складывать только объекты класса Product")

    @classmethod
    def new_product(cls, product_dict):
        return cls(**product_dict)

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
            # Для тестирования лучше использовать исключения или возвращать статус
            # Вместо input() можно использовать конфигурацию или флаги
            raise PermissionError("Требуется подтверждение для увеличения цены")
