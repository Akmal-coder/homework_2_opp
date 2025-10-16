from src.product import Product


class Category:
    """Класс, относящий продукт к определенной категории"""

    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
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
        products_str = ""
        for product in self.__products:
            products_str = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @products.setter
    def products(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_in_list(self):
        return self.__products

    @products_in_list.setter
    def products_in_list(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1
