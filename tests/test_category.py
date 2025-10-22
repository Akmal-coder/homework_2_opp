from src.category import Category


def test_category_init(category, first_product, second_product, third_product):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category.products_in_list == [first_product, second_product, third_product]
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_init_tv(category_tv, fourth_product):
    assert category_tv.name == "Телевизоры"
    assert (
        category_tv.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_tv.products_in_list == [fourth_product]
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_category_products_property(category):
    products_str = category.products
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in products_str
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in products_str
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт." in products_str


def test_category_products_setter(category, first_product):
    assert len(category.products_in_list) == 3
    category.add_product(first_product)
    assert len(category.products_in_list) == 4


def test_category_iterator(category_iterator):
    products = list(category_iterator)
    assert len(products) == 2
    assert products[0].name == "iPhone"
    assert products[1].name == "Samsung"


def test_category_iter_empty(category):
    """Тест итерации по пустой категории"""
    category = Category("Пустая категория", "Описание")

    # Должен работать цикл for без ошибок
    products = []
    for product in category:
        products.append(product)

    assert products == []
    assert len(products) == 0


def test_category_str_empty(category):
    """Тест пустой категории"""
    category = Category("Электроника", "Технические товары")
    result = str(category)
    expected = "Электроника, количество продуктов: 0 шт."
    assert result == expected


def test_category_str_single_product(first_product):
    """Тест категории с одним продуктом"""
    category = Category("Смартфоны", "Мобильные устройства", [first_product])

    result = str(category)
    expected = (
        "Смартфоны, количество продуктов: 5 шт."  # если first_product.quantity = 5
    )
    assert result == expected


def test_add_multiple_products_with_fixtures(sample_product, sample_product_2):
    """Тест с несколькими фикстурами продуктов"""
    category = Category("Категория", "Описание")

    category.add_product(sample_product)
    category.add_product(sample_product_2)

    assert len(category.products_in_list) == 2
    product_names = [p.name for p in category.products_in_list]
    assert "iPhone" in product_names
    assert "Samsung" in product_names


def test_category_inherits_countable():
    """Тест, что Category наследует абстрактный класс Countable"""
    from src.order import Countable

    assert issubclass(Category, Countable)


def test_category_has_total_quantity(category):
    """Тест, что Category имеет свойство total_quantity от Countable"""
    assert hasattr(category, "total_quantity")
    # 5 (Samsung) + 8 (iPhone) + 14 (Xiaomi) = 27
    assert category.total_quantity == 27


def test_category_total_quantity_empty():
    """Тест total_quantity для пустой категории"""
    empty_category = Category("Пустая", "Описание")
    assert empty_category.total_quantity == 0


def test_category_implements_countable_abstract_methods():
    """Тест, что Category реализует все абстрактные методы Countable"""
    from abc import ABC

    assert issubclass(Category, ABC)

    # Проверяем, что есть обязательные методы
    category = Category("Тест", "Описание")
    assert hasattr(category, "add_product")
    assert hasattr(category, "total_quantity")
    assert callable(category.add_product)


def test_category_countable_interface(first_product):
    """Тест интерфейса Countable в Category"""
    category = Category("Тест", "Описание")

    # Проверяем добавление продукта
    category.add_product(first_product)
    assert len(category.products_in_list) == 1
    assert category.total_quantity == 5  # first_product.quantity = 5

    # Проверяем обновление total_quantity после добавления
    from src.product import Product

    another_product = Product("Другой", "Описание", 100, 3)
    category.add_product(another_product)
    assert category.total_quantity == 8  # 5 + 3


def test_category_countable_with_multiple_products(sample_products):
    """Тест Countable с несколькими продуктами из фикстуры"""
    category = Category("Тест", "Описание", sample_products)

    # sample_products: iPhone (quantity=5) + Samsung (quantity=3)
    assert category.total_quantity == 8


def test_category_countable_after_removal(first_product, second_product):
    """Тест обновления total_quantity (если бы было удаление)"""
    category = Category("Тест", "Описание", [first_product, second_product])

    # first_product.quantity = 5, second_product.quantity = 8
    initial_total = category.total_quantity
    assert initial_total == 13

    # Симулируем изменение quantity продукта
    first_product.quantity = 2
    assert category.total_quantity == 10  #
