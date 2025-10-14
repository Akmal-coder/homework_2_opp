import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture
def third_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def fourth_product():
    return Product(
        name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7
    )


@pytest.fixture
def category(first_product, second_product, third_product):
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
        ),
        products=[first_product, second_product, third_product],
    )


@pytest.fixture
def category_tv(fourth_product):
    return Category(
        name="Телевизоры",
        description=(
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
        ),
        products=[fourth_product],
    )


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта"""
    return Product("iPhone", "Смартфон", 100000, 5)


@pytest.fixture
def sample_product_2():
    """Фикстура для создания второго тестового продукта"""
    return Product("Samsung", "Смартфон", 80000, 3)


@pytest.fixture
def sample_products(sample_product, sample_product_2):
    """Фикстура для списка продуктов"""
    return [sample_product, sample_product_2]


@pytest.fixture
def empty_category():
    """Фикстура для пустой категории"""
    return Category("Смартфоны", "Мобильные устройства")


@pytest.fixture
def category_with_products(sample_products):
    """Фикстура для категории с продуктами"""
    return Category("Смартфоны", "Мобильные устройства", sample_products)


@pytest.fixture
def category_iterator(category_with_products):
    """Фикстура для итератора категории"""
    return iter(category_with_products)
