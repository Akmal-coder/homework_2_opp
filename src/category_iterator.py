# class CategoryIterator:
#     """Класс-итератор для перебора товаров категории"""
#
#     def __init__(self, category):
#         self.category = category
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.category.products_in_list):
#             product = self.category.products_in_list[self.index]
#             self.index += 1
#             return product
#         else:
#             raise StopIteration
