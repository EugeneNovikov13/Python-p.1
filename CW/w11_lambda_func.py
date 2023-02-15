# def show_elements(lst1, func):
#     for i in lst1:
#         if func(i):
#             print(i)
#
#
# # def __odd(x):
# #     return True if x % 2 != 0 else False
#
#
# a = [1, 2, 3, 4, 5, 6, 7]
# # show_elements(a, __odd)
#
#
# # r = lambda a, b: a + b
# # print(r(1, 2))
# l_1 = lambda x: x % 2 == 0
#
# show_elements(a, l_1)
# ///////////////////////
# get_sq = lambda a: a**2
#
# print(get_sq(2))
# ///////////////////////
# div_func = lambda a, b: a / b if b != 0 else None
#
# print(div_func(10, 0))
# ///////////////////////
# abs_func = lambda a: a if a > 0 else -a
#
# print(abs_func(-5))
# ///////////////////////
# name = 'Tom'
#
#
# def say_hi():
#     print('Hello', name)
#
#
# def say_bye():
#     name = 'Bob'
#     print('Good bye', name)
#
#
# say_hi()
# say_bye()
# print(name)
# ///////////////////////
# x = 0
#
#
# def outer():
#     x = 1
#     def inner():
#         # nonlocal x
#         # global x
#         x = 2
#         print('inner', x)
#     inner()
#     print('outer', x)
#
#
# outer()
#
# print('global', x)
# ///////////////////////
# //РЕКУРСИЯ//
# def func_rec(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * func_rec(x, n - 1)
#
#
# print(func_rec(2, 3))
# ///////////////////////
# def func_rec(n):
#     if n > 1:
#         func_rec(n - 1)
#     print(n)
#
#
# func_rec(10)
# ///////////////////////
# def func_rec(n):
#     if n == 1:
#         return 1
#     else:
#         return n * func_rec(n-1)
#
#
# print(func_rec(5))
# ///////////////////////
# lst1 = '6 3 -5 16 2'.split()
#
#
# def func_rec(str):
#     if len(str):
#         return 0
#     else:
#         return int(str.pop()) + func_rec(str)
#
#
# print(func_rec(lst1))
# ///////////////////////
