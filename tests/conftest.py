import pytest

from src.category import Category
from src.order import Order
from src.product import LawnGrass, Product, Smartphone


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


@pytest.fixture
def sample_smartphone():
    """Фикстура для создания смартфона"""
    return Smartphone(
        name="iPhone 15 Pro",
        description="256GB, Titanium",
        price=150000.0,
        quantity=10,
        efficiency="High",
        model="15 Pro",
        memory="256GB",
        color="Titanium",
    )


@pytest.fixture
def sample_lawn_grass():
    """Фикстура для создания газонной травы"""
    return LawnGrass(
        name="Premium Grass",
        description="Высококачественная газонная трава",
        price=500.0,
        quantity=100,
        country="Russia",
        germination_period="30 дней",
        color="Green",
    )


@pytest.fixture
def mixed_products(sample_product, sample_smartphone, sample_lawn_grass):
    """Фикстура для смешанных продуктов разных типов"""
    return [sample_product, sample_smartphone, sample_lawn_grass]


@pytest.fixture
def order_with_single_product(first_product):
    """Фикстура для заказа с одним продуктом"""
    return Order(first_product, 2)


@pytest.fixture
def order_with_multiple_products(first_product, second_product, third_product):
    """Фикстура для заказа с несколькими продуктами"""
    order = Order()
    order.add_product(first_product, 1)  # Samsung, 180000 * 1
    order.add_product(second_product, 2)  # iPhone, 210000 * 2
    order.add_product(third_product, 3)  # Xiaomi, 31000 * 3
    return order


@pytest.fixture
def empty_order():
    """Фикстура для пустого заказа"""
    return Order()


@pytest.fixture
def countable_category_with_products(sample_products):
    """Фикстура для тестирования Countable функциональности в Category"""
    return Category("Test Category", "Description", sample_products)


@pytest.fixture
def countable_empty_category():
    """Фикстура для пустой категории с Countable"""
    return Category("Empty Category", "No products")


@pytest.fixture
def order_for_countable_test(first_product, second_product):
    """Фикстура для тестирования Countable в Order"""
    order = Order()
    order.add_product(first_product, 2)
    order.add_product(second_product, 1)
    return order
