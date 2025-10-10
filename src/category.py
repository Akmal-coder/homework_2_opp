from src.product import Product


class Category:
    """Класс, относящий продукт к определенной категории"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

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
