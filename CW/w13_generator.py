import sys
import math

# print(sys.builtin_module_names)

# number = 8.55
# округляет по правилам математического округления
# print(math.ceil(number))
# округляет до целого (убирает цифры после запятой)
# print(math.floor(number))
# делает тоже самое без math
# print(int(number))
# модуль числа
# print(math.fabs(number))
# факториал фисла
# print(math.factorial(number))
# остаток от деления. который работает с числами float
# print(math.fmod(number, 3))

# math.exp(number)
# math.log(number)
# возведение в степень
# print(math.pow(number, 2))
# извлечение квадратного корня
# print(math.sqrt(number))

# ГЕНЕРАТОРЫ
# iter_1 = [x**2 for x in range(11)]
# print(iter_1)

# iter_1 = (x**2 for x in range(11))
# print(iter_1)

# Итерируемый объект -> Итератор -> Генератор

# lst1 = [1, 2, 3]
# a = iter(lst1)
# print(next(a))

# iter_1 = (x**2 for x in range(11))
# print(next(iter_1))
# for i in iter_1:
#     print(i)
# # второй цикл уже не сработает
# for i in iter_1:
#     print(i)

# print(sum(iter_1))
# print(min(iter_1))
# print(max(iter_1))

# эта операция считает сразу
# print(list(range(100000000)))

# а эта считает в процессе
# lst1 = (x for x in range(100000000))
#
# for i in lst1:
#     print(i, end='-')
#     if i > 100000000:
#         break

# функция-генератор


# обычная функция
# def f():
#     return list(range(10))
#
#
# print(f())


# функция-генератор
# def f():
#     for x in range(10):
#         yield x
#
#
# s = f()
# print(next(s))
# print(next(s))


# def get_all_average(n):
#     avs = []
#     count = 0
#     res = 0
#     for i in range(1, n + 1):
#         count += 1
#         res += i
#         avs.append(res / count)
#     return avs
#
#
# def gen_get_all_average(n):
#     count = 0
#     res = 0
#     for i in range(1, n + 1):
#         count += 1
#         res += i
#         yield res / count
#
#
# it = gen_get_all_average(10000)
# print(get_all_average(10000))
# print(get_all_average(10000).__sizeof__())
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it).__sizeof__())

# //////////////////////////////////

# lst = ['Moscow', 'Voronezh', 'Sochi', 'Samara']
# it = iter(lst)
# for i in range(2):
#     print(next(it))

# //////////////////////////////////

# a, b = map(int, input().split())
#
# gen = (x**2 for x in range(a, b+1))
#
# print(list(gen))

# //////////////////////////////////

# a, b = map(int, input().split())
#
# gen = (abs(x) for x in range(a, b+1))
#
# for i in range(5):
#     print(next(gen))

# //////////////////////////////////

lst = ['Moscow', 'Voronezh', 'Sochi', 'Samara', 'Tula']

gen1 = (city for x in range(1000001) for city in lst)

print(*list(gen1)[:20])

