# Задание 1
# Написать рекурсивную функцию нахождения степени числа.

# def func_rec(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * func_rec(x, n - 1)
#
#
# print(func_rec(int(input('Enter number: ')), int(input('Enter degree: '))))

# Задание 2
# Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b. Пользователь вводит a и b.
# Проиллюстрируйте работу функции примером.

# def sum_rec(a, b):
#     if a > b:
#         a, b = b, a
#
#     return b if a == b else a + sum_rec(a + 1, b)
#
#
# print(sum_rec(int(input('Enter number 1: ')), int(input('Enter number 2: '))))

# Задание 3
# Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает пользователь.
# Проиллюстрируйте работу функции примером.

# def func_rec(n):
#     if n == 0:
#         return
#     else:
#         print('*', end='')
#         func_rec(n-1)
#
#
# func_rec(int(input('Enter N: ')))

# Задание 4*
# Напишите рекурсивную функцию, которая принимает список из 100 целых чисел, полученных случайным образом,
# и находит позицию, с которой начинается последовательность из 10 чисел, сумма которых минимальна.

# использую рекурсию
import random


def func(num_list):
    pos = 0

    def func_rec(lst, start_pos=0):
        nonlocal pos
        if len(lst) == 5:
            pos = len(lst) - 5
            return sum(lst)
        sum1 = sum(lst[start_pos:5])
        sum2 = func_rec(lst[start_pos + 1:])
        if sum1 < sum2:
            pos = 20 - len(lst) - 1
            return sum1
        else:
            return sum2

    func_rec(num_list)
    return pos


lst1 = [random.randint(0, 20) for x in range(20)]
print(lst1, func(lst1))

# нерекурсивная функция
# import random
#
#
# def func(lst):
#     pos = 0
#     min_sum = sum(lst[0:5])
#     for i in range(1, len(lst)-5):
#         if sum(lst[i:i+5]) < min_sum:
#             pos = i
#             min_sum = sum(lst[i:i+5])
#     return pos
#
#
# lst1 = [random.randint(0, 20) for x in range(20)]
# print(lst1, func(lst1), sep='\n')

# Задание 5**
# Написать функцию, которая принимает две даты (т.е. функция принимает шесть параметров) и вычисляет разность
# в днях между этими датами. Для решения этой задачи необходимо также написать функцию, которая определяет,
# является ли год високосным.
