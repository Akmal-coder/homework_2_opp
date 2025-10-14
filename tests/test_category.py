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
    assert category.products == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"


def test_category_products_setter(category, first_product):
    assert len(category.products_in_list) == 3
    category.products_in_list = first_product
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
