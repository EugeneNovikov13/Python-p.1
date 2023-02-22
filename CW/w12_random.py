# import random
#
# from random import randint, random, randrange
#
# print(randint(-10, 10))
#
# print(randrange(2))
#
# верхняя граница не входит в диапазон
# print(randrange(1, 40))
#
# 3 цифра шаг
# print(randrange(1, 40, 5))
#
# возвращает float число от 0 до 1
# print(random())
#
# str1 = 'qwertyuiop'
# lst1 = [1, 2, 3, 4, True]
#
# print(random.choice(str1))
# print(random.choice(lst1))
#
# //////////////////////////////////////
# print(randrange(6, 12, 2))
# print(randrange(5, 100, 5))
# //////////////////////////////////////
# num1 = float(input('Enter number 1: '))
# num2 = float(input('Enter number 2: '))
# type_num = input('Enter type of num INT or FLOAT: ')
#
# if type_num == 'INT':
#     print(randint(num1, num2))
# elif type_num == 'FLOAT':
#     print(randrange(num1, num2) + random())
# //////////////////////////////////////
# str1 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#
# password = ''
#
# for i in range(6):
#     password += random.choice(str1)
#
# print(password)
# //////////////////////////////////////
#
# Функция map
#
# lst1 = [1, 2, 3, 4, 5]
#
#
# def sq(x):
#     return x**2
#
#
# b = list(map(sq, lst1))
# print(b)
# //////////////////////////////////////
# lst2 = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x: x+1, lst2)))
# //////////////////////////////////////
# lst3 = ['Moscow', 'Voronezh', 'Sochi']
# b = map(len, lst3)
# print(list(b))
#
# c = map(str.upper, lst3)
# print(list(c))
#
# c = map(str.upper, lst3)
# d = map(lambda x: x[::-1], c)
# print(list(d))
# //////////////////////////////////////
# a = list(map(int, input().split()))
#
# print(a)
# //////////////////////////////////////

# filter~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def odd(x):
#     return x % 2
#
#
# b = list(filter(odd, lst1))
# print(b)
# #
# b = list(filter(lambda x: x % 2, lst1))
# print(b)
# //////////////////////////////////////
# lst2 = ['Moscow', 'Ryazan1', 'Smolensk', 'Tver', 'Voronezh45']
# b = filter(str.isalpha, lst2)

# способ вывода иттерируемого объекта с помощью цикла
# for x in b:
#     print(x, end=' ')
# способ вывода иттерируемого объекта с помощью распаковки
# print(*b)

# reduce~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from functools import reduce
#
# items = [1, 2, 3, 4, 5]
#
# sum_all = reduce(lambda x, y: x + y, items)
# print(sum_all)

# zip~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# it = zip(a, b)
# # print(list(it))
#
# # словарь
# print(dict(it))
# //////////////////////////////////////
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# c = 'abrakadabra'
# it = zip(a, b, c)
# print(list(it))

# словарь
# print(dict(it))

# //////////////////////////////////////
# lst1 = list(map(int, input("Enter str of num: ").split()))

# print(*(map(abs, map(int, input("Enter str of num: ").split()))))
# //////////////////////////////////////
# Moscow Ryazan Smolensk Tver Voronezh Ufa
# lst2 = list(input("Enter str of cities: ").split())

# print(*(map(lambda x: x if len(x) > 5 else '-', input("Enter str of cities: ").split())))
# //////////////////////////////////////
# -45 2 5654 12 0 54
# print(*(filter(lambda x: 9 < abs(x) < 100, map(int, input('Enter str of num: ').split()))))
# //////////////////////////////////////
# lst1 = [-7, 8, 11, -1, 3]
# lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(*map(lambda x: x[0] * x[1], zip(lst1, lst2)))

