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
