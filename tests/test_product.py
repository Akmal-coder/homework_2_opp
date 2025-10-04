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
