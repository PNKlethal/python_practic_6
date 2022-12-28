#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
from timeit import timeit

name = input('введите имя: ')
surname = input('введите фамилию: ')
year = str(input('введите год рождения: '))
city = input('введите город проживания: ')
email = input('введите почту: ')
telephone = input('введите номер телефона ')


def my_func(name, surname, year, city, email, telephone):
    return ','.join([name, surname, year, city, email, telephone])


print(my_func(name, surname, year, city, email, telephone))

print(timeit("my_func",globals=globals() , number=10000))

"""Первый код впринципе работал не правильно, время выполнения- 0.00010439998004585505"""


def my_func_2(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func_2(surname='Игнатов', name='Сергей', year='1999', city='Омск',email='seregaa99@bk.ru', telephone='8-800-555-35-35'))

print(timeit("my_func_2",globals=globals() , number=10000))

"""Второй код не принёс быстродействия, но была сделана оптимизация кода под условие задачи, время выполнения- 0.00012680000509135425"""



