# def mult(a, b):
#     print(a + b)
#
#
# mult(4, 2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def summ(*elements):
#     result = 0
#     print(elements)
#     for elem in elements:
#         result += elem
#
#     return result


# print(summ(1, 2, 3))
# print(summ(1, 2, 3, 6, 12, -10, 0))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def func(*args):
#     print(args[0])
#
#     print(args)
#
#
# func('Python', 'C++', 'Java')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def print_scores(student, *args):
#     print(f'Student name: {student}')
#
#     for score in args:
#         print(score)
#
#
# print_scores('Dmitrii', 100, 95, 88, 92, 99)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def pet_names(owner, **pets):
#     print(owner)
#
#     for pet, name in pets.items():
#         print(f'{pet}: {name}')
#
#
# pet_names('Dmitrii', dog='Rex', cats=['Murzik', 'Barsik', 'Vaska'], snake='Python')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def outer():
#     n = 5
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(n)
#
#     return inner
#
#
# fn = outer()
# fn()
# fn()
# fn()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def multiply(n):
#
#     def inner(m):
#         return n * m
#     return inner
#
#
# fn = multiply(5)
# print(fn(5))
# print(fn(6))
# print(fn(7))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def multiply(n):
#     return lambda m: n * m
#
#
# fn = multiply(5)
# print(fn(5))
# print(fn(6))
# print(fn(7))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def counter(start=0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#
#     return step
#
#
# c1 = counter(10)
# c2 = counter()
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def strip_str(strip_chars=' '):
#     def do_strip(str1):
#         return str1.strip(strip_chars)
#
#     return do_strip
#
#
# strip1 = strip_str()
# strip2 = strip_str(' !&,.;')
#
# print(strip1(' hello python!.. '))
# print(strip2(' hello python!.. '))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import time
#
#
# def get_nod(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a


# print(get_nod(12, 8))


# def test_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time() - start
#         print(f'Work time: {stop} sec')
#     return wrapper


# test1 = test_time(get_nod)
# test1(100000000, 8)


# def get_fast_nod(a, b):
#     if a < b:
#         a, b = b, a
#         while b:
#             a, b = b, a % b
#         return a
#
#
# test1 = test_time(get_nod)
# test2 = test_time(get_fast_nod)
# test1(100000000, 2)
# test2(100000000, 2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import time
#
#
# def test_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time() - start
#         print(f'Work time: {stop} sec')
#     return wrapper
#
#
# @test_time
# def get_fast_nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b:
#         a, b = b, a % b
#     return a
#
#
# get_fast_nod(100, 2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def print_str(func):
#     def wrapper(*args):
#         print(f'Square: {func(*args)}')
#     return wrapper
#
#
# @print_str
# def get_sq(width, height):
#     return width * height
#
#
# get_sq(10, 3)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def sort_list(func):
#     def wrapper(*args):
#         return sorted(func(*args))
#     return wrapper
#
#
# @sort_list
# def string_to_list():
#     return list(map(int, input('Enter string: ').split()))
#
#
# print(*string_to_list())
