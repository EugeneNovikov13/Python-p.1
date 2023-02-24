# def name_func():
#     print('hello')


# name_func()

# print(type(name_func))
#
# F = name_func
# F()
# print(F)
# ////////////////////////
# def abs_num(x):
#     # print(-x) if (x < 0) else print(x)
#     x = -x if (x < 0) else x
#     return x
#
#
# F = abs_num
# print(F(-5))
#
# q = -9
# print(F(q))
# ////////////////////////
# def is_positive(x):
#     # if x >= 0:
#     #     return True
#     # else:
#     #     return False
#     return x >= 0
#
#
# p = []
# for i in range(-5, 11):
#     if is_positive(i):
#         p.append(i)
#
# print(p)
# ////////////////////////
# def get_sq(a, b):
#     return 2 * (a + b)
#
#
# s = get_sq(20, 10)
#
# print(s)

# def get_sq(a: int, b: int) -> int:
#     return 2 * (a + b)
#
#
# s = get_sq('34', '15')
# print(s)
# ////////////////////////
# Значения по умолчанию:
# def say_hello(msg, end='!'):
#     print(msg + end)
#
#
# say_hello('hello')
# ////////////////////////
def per_and_sq(w, h):
    return 2 * (w + h), w * h


r = per_and_sq(3, 5)
per, sq = per_and_sq(4, 6)
print(r)
print(per, sq)
# ////////////////////////
# def pr_hello():
#     print('hello')
#
#
# def pr_hello():
#     print('---------hello----------')
#
#
# pr_hello()
# ////////////////////////
# TYPE_FUNC = False
#
# if TYPE_FUNC:
#     def say_hello():
#         print('hello')
# else:
#     def say_hello(msg):
#         print(msg)
#
#
# say_hello('Hi')
# ////////////////////////
# def max2(a, b):
#     if a > b:
#         return a
#     return b
#
#
# print(max2(2, -3))
#
#
# def max3(a, b, c):
#     return max2(a, max2(b, c))
#
#
# print(max(2, -3, 5))
# ////////////////////////
# import random
#
# lst1 = [random.randint(-50, 50) for x in range(6)]
# print(lst1)
#
#
# def mms(lst):
#     return min(lst), max(lst), sum(lst)
#
#
# mini, maxi, summ = mms(lst1)
#
# print(f'min={mini}, max={maxi}, sum={summ}')
# ////////////////////////
# def per(w, h):
#     print(f'perimetr: {2 * (int(w) + int(h))}')
#
#
# sides = input('Enter width and height: ').split(' ')
# per(sides[0], sides[1])
# ////////////////////////
# def is_triangle(a, b, c):
#     lst1 = [a, b, c]
#     lst1.sort()
#     return True if lst1[0] + lst1[1] > lst1[2] else False
#
#
# print(is_triangle(4, 5, 6))
# //////////////////////////
# def filt_city(city):
#     return len(city) >= 6
#
#
# lst1 = input('Enter cities: ').split(' ')
#
# lst1 = [i for i in lst1 if filt_city(i)]
# print(*lst1)



