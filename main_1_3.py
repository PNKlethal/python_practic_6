#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
#Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].

from timeit import timeit

result_list_1 = []
list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list_1.append(list[i]))
print("Исходный список: ", list)
print("Список, элементы которого больше предыдущего: ", result_list_1)


src_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# index
res_list = [src_list[i] for i in range(1, len(src_list)) if src_list[i] > src_list[i-1]]
assert (res_list == [12, 44, 4, 10, 78, 123])

# enumerate
res_list = [item for i, item in enumerate(src_list[1:]) if item > src_list[i]]
assert (res_list == [12, 44, 4, 10, 78, 123])

# zip
res_list = [y for x, y in zip(src_list[:-1], src_list[1:]) if y > x]
assert (res_list == [12, 44, 4, 10, 78, 123])


print('Source list: ', src_list)
print('Result list: ', res_list)

print(timeit("result_list_1",globals=globals() , number=100000))
"""0.0011854000040329993"""
print(timeit("res_list",globals=globals() , number=100000))
"""0.001237800024682656"""
"""Получается так, что в моих примерах 2 и 3, после оптимизации, время становится чуть больше, но я думаю это из-за того, что я изначально неправильно делал задание"""

