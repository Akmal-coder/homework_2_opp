from src.category import Category
from src.order import Countable, Order  # Добавил импорт Countable
from src.product import LawnGrass, Product, Smartphone

if __name__ == "__main__":
    # Тестирование старой функциональности
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products_in_list))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products_in_list))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # ТЕСТИРОВАНИЕ НОВОЙ ФУНКЦИОНАЛЬНОСТИ
    print("\n" + "=" * 50)
    print("ТЕСТИРОВАНИЕ НОВОЙ ФУНКЦИОНАЛЬНОСТИ")
    print("=" * 50)

    # Тестирование заказов
    print("\n1. Тестирование заказов:")
    order1 = Order(product1, 2)
    print(order1)

    order2 = Order()
    order2.add_product(product2, 1)
    print("\n2. Заказ с iPhone:")
    print(order2)

    # Тестирование с разными типами продуктов
    smartphone = Smartphone(
        "Xiaomi", "Хороший телефон", 30000.0, 10, "Высокая", "Note11", "128GB", "Синий"
    )
    grass = LawnGrass(
        "Трава", "Зеленая трава", 500.0, 100, "Россия", "30 дней", "Зеленый"
    )

    order3 = Order()
    order3.add_product(smartphone, 1)
    order3.add_product(grass, 5)
    print("\n3. Смешанный заказ:")
    print(order3)

    # Тестирование абстрактных классов
    print("\n4. Проверка наследования:")
    print(f"Category наследует Countable: {issubclass(Category, Countable)}")
    print(f"Order наследует Countable: {issubclass(Order, Countable)}")

    # Тестирование общей функциональности
    print("\n5. Общая функциональность (Countable):")
    print(f"Количество товаров в категории 'Смартфоны': {category1.total_quantity} шт.")
    print(f"Количество товаров в заказе 1: {order1.total_quantity} шт.")
    print(f"Количество товаров в заказе 3: {order3.total_quantity} шт.")
