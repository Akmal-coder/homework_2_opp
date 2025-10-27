import pytest

from src.category import Category
from src.order import Countable, Order
from src.product import BaseProduct, LawnGrass, Product, Smartphone


def test_product_init(first_product, second_product, third_product, fourth_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8

    assert third_product.name == "Xiaomi Redmi Note 11"
    assert third_product.description == "1024GB, Синий"
    assert third_product.price == 31000.0
    assert third_product.quantity == 14

    assert fourth_product.name == '55" QLED 4K'
    assert fourth_product.description == "Фоновая подсветка"
    assert fourth_product.price == 123000.0
    assert fourth_product.quantity == 7


def test_product_str(first_product, second_product, third_product, fourth_product):
    assert (
        str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )
    assert str(second_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(third_product) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    assert str(fourth_product) == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'


def test_product_add(first_product, second_product, third_product, fourth_product):
    assert (first_product + second_product) + (third_product + fourth_product)


def test_sample_products_fixture_returns_list(sample_products):
    """Тест что фикстура возвращает список"""
    assert isinstance(sample_products, list)
    assert len(sample_products) == 2


def test_sample_products_names(sample_products):
    """Тест имен продуктов в фикстуре"""
    product_names = [product.name for product in sample_products]
    expected_names = ["iPhone", "Samsung"]
    assert product_names == expected_names


def test_sample_products_quantities(sample_products):
    """Тест количеств продуктов в фикстуре"""
    assert sample_products[0].quantity == 5  # iPhone
    assert sample_products[1].quantity == 3


def test_add_same_products():
    phone1 = Smartphone("Phone1", "Desc", 100, 2, "High", "X", 128, "Black")
    phone2 = Smartphone("Phone2", "Desc", 200, 3, "High", "Y", 256, "White")
    result = phone1 + phone2
    assert result == (100 * 2 + 200 * 3)


def test_add_different_products():
    phone = Smartphone("Phone", "Desc", 100, 2, "High", "X", 128, "Black")
    grass = LawnGrass("Grass", "Desc", 50, 5, "Russia", "7 days", "Green")
    with pytest.raises(TypeError):
        phone + grass


def test_add_product_to_category():
    category = Category("Test", "Test desc")
    phone = Smartphone("Phone", "Desc", 100, 2, "High", "X", 128, "Black")
    category.add_product(phone)
    assert len(category.products_in_list) == 1


def test_add_wrong_type_to_category():
    category = Category("Test", "Test desc")
    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_base_product_abstract():
    """Тест, что BaseProduct является абстрактным классом"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100, 5)


def test_repr_mixin_logging(capsys):
    """Тест, что миксин логирует создание объектов"""
    product = Product("Test", "Desc", 100, 5)
    captured = capsys.readouterr()
    assert "Создан объект Product" in captured.out
    assert "name=Test" in captured.out


def test_order_creation(first_product):
    """Тест создания заказа"""
    order = Order(first_product, 2)
    assert order.total_quantity == 2
    assert order.total_cost == 180000.0 * 2


def test_order_add_product(first_product):
    """Тест добавления продукта в заказ"""
    order = Order()
    order.add_product(first_product, 3)
    assert order.total_quantity == 3
    assert len(order.products) == 1


def test_order_str(first_product):
    """Тест строкового представления заказа"""
    from src.order import Order

    order = Order(first_product, 2)
    order_str = str(order)
    assert "Samsung Galaxy S23 Ultra" in order_str
    assert "2 шт." in order_str


def test_countable_abstract():
    """Тест, что Countable является абстрактным классом"""
    with pytest.raises(TypeError):
        Countable()


def test_category_inherits_countable():
    """Тест, что Category наследует Countable"""
    assert issubclass(Category, Countable)


def test_category_has_total_quantity():
    """Тест, что Category имеет свойство total_quantity"""
    from src.category import Category
    from src.product import Product

    product = Product("Test", "Desc", 100, 5)
    category = Category("Test", "Desc", [product])
    assert hasattr(category, "total_quantity")
    assert category.total_quantity == 5


def test_product_inherits_base_product_and_repr_mixin():
    """Тест, что Product наследует BaseProduct и ReprMixin"""
    from src.product import BaseProduct, Product, ReprMixin

    assert issubclass(Product, BaseProduct)
    assert issubclass(Product, ReprMixin)


def test_product_mro_correct():
    """Тест правильного порядка разрешения методов (MRO)"""
    mro = Product.__mro__
    assert mro[0] == Product
    assert mro[1].__name__ == "ReprMixin"
    assert mro[2].__name__ == "BaseProduct"


def test_smartphone_inheritance():
    """Тест наследования Smartphone"""
    assert issubclass(Smartphone, Product)
    smartphone = Smartphone("Phone", "Desc", 100, 2, "High", "X", "128GB", "Black")
    assert isinstance(smartphone, Product)


def test_lawn_grass_inheritance():
    """Тест наследования LawnGrass"""
    assert issubclass(LawnGrass, Product)
    grass = LawnGrass("Grass", "Desc", 50, 5, "Russia", "7 days", "Green")
    assert isinstance(grass, Product)


def test_repr_mixin_representation(first_product):
    """Тест метода __repr__ миксина"""
    repr_str = first_product.__repr__()
    assert "name=Samsung Galaxy S23 Ultra" in repr_str
    assert "description=256GB, Серый цвет, 200MP камера" in repr_str
    assert "quantity=5" in repr_str


def test_product_new_product_method():
    """Тест классового метода new_product"""
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100.0,
        "quantity": 10,
    }
    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price_setter_valid(first_product):
    """Тест валидного изменения цены через сеттер"""
    first_product.price = 150000.0  # Уменьшение цены
    assert first_product.price == 150000.0


def test_product_price_setter_invalid(first_product):
    """Тест невалидного изменения цены через сеттер"""
    with pytest.raises(ValueError):
        first_product.price = 0  # Нулевая цена
    with pytest.raises(ValueError):
        first_product.price = -100  # Отрицательная цена


def test_product_price_setter_increase_requires_confirmation(first_product):
    """Тест увеличения цены требует подтверждения"""
    with pytest.raises(PermissionError):
        first_product.price = 200000.0  # Увеличение цены


def test_order_with_smartphone(sample_smartphone):
    """Тест заказа со смартфоном"""
    order = Order(sample_smartphone, 1)
    assert order.total_cost == 150000.0  # sample_smartphone.price
    assert order.total_quantity == 1


def test_order_with_lawn_grass(sample_lawn_grass):
    """Тест заказа с газонной травой"""
    from src.order import Order

    order = Order(sample_lawn_grass, 10)
    assert order.total_cost == 5000.0  # 500 * 10
    assert order.total_quantity == 10


def test_order_mixed_products(sample_smartphone, sample_lawn_grass):
    """Тест заказа с разными типами продуктов"""
    order = Order()
    order.add_product(sample_smartphone, 2)
    order.add_product(sample_lawn_grass, 5)
    assert order.total_quantity == 7
    assert order.total_cost == (150000.0 * 2) + (500.0 * 5)


def test_countable_interface_consistency():
    """Тест согласованности Countable интерфейса в Category и Order"""
    category_methods = {
        method for method in dir(Category) if not method.startswith("_")
    }
    order_methods = {method for method in dir(Order) if not method.startswith("_")}

    common_methods = category_methods.intersection(order_methods)
    assert "add_product" in common_methods
    assert "total_quantity" in common_methods


def test_abstract_base_product_methods():
    """Тест, что BaseProduct требует реализации абстрактных методов"""
    assert hasattr(BaseProduct, "__abstractmethods__")
    abstract_methods = BaseProduct.__abstractmethods__
    expected_methods = {"__str__", "__add__", "new_product"}
    assert expected_methods.issubset(abstract_methods)


def test_product_zero_quantity():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Телефон", "Хороший", 50000.0, 0)


def test_smartphone_zero_quantity():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Smartphone("iPhone", "Новый", 100000.0, 0, "Высокая", "15", "256GB", "Black")


def test_lawn_grass_zero_quantity():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        LawnGrass("Трава", "Зеленая", 1000.0, 0, "Россия", "30 дней", "Зеленый")


def test_product_positive_quantity():
    product = Product("Телефон", "Хороший", 50000.0, 5)
    assert product.quantity == 5


def test_product_negative_quantity():
    product = Product("Товар", "Описание", 1000.0, -1)
    assert product.quantity == -1
