from src.category import Category


def test_category_init(category, first_product, second_product, third_product):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category.products == [first_product, second_product, third_product]
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_init_tv(category_tv, fourth_product):
    assert category_tv.name == "Телевизоры"
    assert (
        category_tv.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_tv.products == [fourth_product]
    assert Category.category_count == 2
    assert Category.product_count == 1
