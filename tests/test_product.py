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
