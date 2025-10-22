import pytest

from src.order import Countable, Order
from src.product import LawnGrass, Product, Smartphone


def test_order_creation_with_fixture(order_with_single_product):
    """Тест создания заказа с использованием фикстуры"""
    order = order_with_single_product
    assert order.total_quantity == 2
    assert order.total_cost == 180000.0 * 2
    assert len(order.products) == 1


def test_order_multiple_products_fixture(order_with_multiple_products):
    """Тест заказа с несколькими продуктами используя фикстуру"""
    order = order_with_multiple_products
    assert order.total_quantity == 6  # 1 + 2 + 3
    expected_cost = (180000.0 * 1) + (210000.0 * 2) + (31000.0 * 3)
    assert order.total_cost == expected_cost
    assert len(order.products) == 3


def test_empty_order_fixture(empty_order):
    """Тест пустого заказа с использованием фикстуры"""
    order = empty_order
    assert order.total_quantity == 0
    assert order.total_cost == 0
    assert len(order.products) == 0
    assert str(order) == "Пустой заказ"


def test_order_add_product_with_fixtures(empty_order, first_product, second_product):
    """Тест добавления продуктов в заказ с фикстурами"""
    order = empty_order
    order.add_product(first_product, 2)
    order.add_product(second_product, 1)

    assert order.total_quantity == 3
    assert order.total_cost == (180000.0 * 2) + (210000.0 * 1)
    assert len(order.products) == 2


def test_order_inherits_countable():
    """Тест наследования Order от Countable"""
    assert issubclass(Order, Countable)


def test_order_implements_countable_abstract_methods():
    """Тест реализации абстрактных методов Countable в Order"""
    order = Order()

    # Проверяем наличие абстрактных методов
    assert hasattr(order, "add_product")
    assert hasattr(order, "total_quantity")
    assert callable(order.add_product)

    # Проверяем, что методы работают
    product = Product("Test", "Desc", 100, 5)
    order.add_product(product, 2)
    assert order.total_quantity == 2


def test_order_str_with_fixture(order_with_multiple_products):
    """Тест строкового представления заказа с фикстурой"""
    order_str = str(order_with_multiple_products)

    assert "Samsung Galaxy S23 Ultra" in order_str
    assert "Iphone 15" in order_str
    assert "Xiaomi Redmi Note 11" in order_str
    assert "Итого:" in order_str


def test_order_add_invalid_product(empty_order):
    """Тест добавления невалидного продукта"""
    with pytest.raises(TypeError):
        empty_order.add_product("not a product", 1)
    with pytest.raises(TypeError):
        empty_order.add_product(123, 1)


def test_order_add_product_invalid_quantity(empty_order, first_product):
    """Тест добавления продукта с невалидным количеством"""
    with pytest.raises(ValueError):
        empty_order.add_product(first_product, 0)
    with pytest.raises(ValueError):
        empty_order.add_product(first_product, -5)


def test_order_with_different_product_types(sample_smartphone, sample_lawn_grass):
    """Тест заказа с разными типами продуктов"""
    order = Order()
    order.add_product(sample_smartphone, 1)
    order.add_product(sample_lawn_grass, 10)

    assert order.total_quantity == 11
    assert len(order.products) == 2

    # Проверяем структуру данных в products
    for item in order.products:
        assert "product" in item
        assert "quantity" in item
        assert "total_cost" in item
        assert isinstance(item["product"], (Product, Smartphone, LawnGrass))


def test_order_total_quantity_calculation():
    """Тест расчета общего количества в заказе"""
    order = Order()
    product1 = Product("P1", "Desc", 100, 10)
    product2 = Product("P2", "Desc", 200, 20)

    order.add_product(product1, 3)
    order.add_product(product2, 5)

    assert order.total_quantity == 8


def test_order_total_cost_calculation():
    """Тест расчета общей стоимости заказа"""
    order = Order()
    product1 = Product("P1", "Desc", 100, 10)
    product2 = Product("P2", "Desc", 200, 20)

    order.add_product(product1, 2)  # 100 * 2 = 200
    order.add_product(product2, 3)  # 200 * 3 = 600

    assert order.total_cost == 800  # 200 + 600


def test_order_products_structure(order_with_single_product):
    """Тест структуры данных в order.products"""
    order = order_with_single_product
    assert len(order.products) == 1

    item = order.products[0]
    assert "product" in item
    assert "quantity" in item
    assert "total_cost" in item
    assert item["quantity"] == 2
    assert item["total_cost"] == 180000.0 * 2
    assert item["product"].name == "Samsung Galaxy S23 Ultra"
