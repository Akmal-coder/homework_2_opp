from src.countable import Countable
from src.product import Product


class Order(Countable):
    """Класс заказа"""

    def __init__(self, product=None, quantity=1):
        super().__init__()
        self.products = []
        if product:
            self.add_product(product, quantity)

    def add_product(self, product, quantity=1):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product или его наследников"
            )

        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")

        self.products.append(
            {
                "product": product,
                "quantity": quantity,
                "total_cost": product.price * quantity,
            }
        )

    @property
    def total_quantity(self):
        return sum(item["quantity"] for item in self.products)

    @property
    def total_cost(self):
        return sum(item["total_cost"] for item in self.products)

    def __str__(self):
        if not self.products:
            return "Пустой заказ"

        items = []
        for item in self.products:
            items.append(
                f"{item['product'].name} - {item['quantity']} шт. = {item['total_cost']} руб."
            )

        return f"Заказ:\n" + "\n".join(items) + f"\nИтого: {self.total_cost} руб."
