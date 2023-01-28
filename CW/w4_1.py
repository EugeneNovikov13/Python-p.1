# x = input('x: ')
# y = input('y: ')
#
# try:
#     x = int(x)
#     y = int(y)
#
#     res = x / y
# except ZeroDivisionError:
#     res = 'division on Zero'
# except ValueError:
#     res = 'not integer'
# # объединенный вариант
# except (ZeroDivisionError, ValueError):
#     res = 'error'
# finally:
#     print('All right!')
# print(res)
# import math

# try:
#     num1 = float(input('num1: '))
#     num2 = float(input('num2: '))
#     num3 = float(input('num3: '))
#
#     mid = (num1 + num2 + num3) / 3
#     res = str(mid)
#
# except ValueError:
#     res = 'value error'
# finally:
#     print(res)

# print('a')
# 1/0
# print('b')
#
# raise ZeroDivisionError('division on 0')
# e = ZeroDivisionError('Division on 0')
# raise e

# try:
#     x = int(input('x'))
#     y = int(input('y'))
#     res = x / y
#     print(res)
# except ValueError as v:
#     print(v)

# try:
#     f = open('abc.txt')
#     r = f.read(1)
#     f.close()
# except FileNotFoundError:
#     print('file not found')

# try:
#     a = float(input('a: '))
#     b = float(input('b: '))
#
#     if a * b < 0:
#         raise ValueError('One of number is negative')
#     else:
#         c = (a * b) ** 0.5
#     print(f'Middle geometric = {c}')
#
# except ValueError as err:
#     print(err)


