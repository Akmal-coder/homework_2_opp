from src.order import Countable
from src.product import Product


class Category(Countable):
    """Класс, относящий продукт к определенной категории"""

    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        super().__init__()
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
        for product in self.products_in_list:
            yield product

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_in_list(self):
        return self.__products

    @property
    def total_quantity(self):
        return sum(product.quantity for product in self.__products)

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0
