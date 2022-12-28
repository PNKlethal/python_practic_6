#Тест первый вариант
from timeit import timeit

list = [1, 2, -30, 'string', True, 3.5]

def my_type(element):
    for element in range(len(list)):
        print(type(list[element]))
    return


my_type(list)

print(timeit("my_type",globals=globals() , number=10000))

"0.00010750000365078449"

list = [1, 2, -30, 'string', True, 3.5]

"""Здесь я просто последовал вашему замечанию про то, что бесмысленно усложнил код, после правок, время уменьшилось"""
def my_type_optimizmed(el):
    for el in list:
        print(type(list))
    return


my_type(list)

print(timeit("my_type",globals=globals() , number=10000))

"0.00010410000686533749"




