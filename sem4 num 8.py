# Исходные два списка чисел
list_a = [1, 2, 3, 4, 5, 10, 15]
list_b = [4, 5, 6, 7, 8, 10, 20]

set_a = set(list_a)
set_b = set(list_b)

# 1. Уникальные для каждого списка (симметрическая разность: элементы, входящие ТОЛЬКО в A или ТОЛЬКО в B)
unique_each = set_a ^ set_b  # эквивалентно (set_a - set_b) | (set_b - set_a)

# 2. Уникальные для объединения этих списков (все элементы из двух списков без повторов)
unique_union = set_a | set_b

# 3. Содержащиеся в обоих списках (пересечение списков)
common_elements = set_a & set_b

print("Список A:", list_a)
print("Список B:", list_b)
print("-" * 40)
print("1. Уникальные для каждого списка (есть только в одном из них):", sorted(list(unique_each)))
print("2. Уникальные элементы объединения списков:", sorted(list(unique_union)))
print("3. Общие элементы (есть и в A, и в B):", sorted(list(common_elements)))