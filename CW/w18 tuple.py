from typing import Optional, Any, Union, List, Callable, Tuple, Set

# КОРТЕЖИ

# a = 1, 2
# b = (1, 3, 2, True)
# c = (1,)
# d = len(b)
# e = b[3]
# f = b[1:3]
# g = b[:]  # создает тот же самый кортеж
# print(a, b, c, d, e, f, g, sep='\n')
# b[1] = 66  нельзя изменять элементы
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(lst.__sizeof__())
# print(tup.__sizeof__())
# a = ()
# b = tuple()
# # print(id(a), id(b))
# a = a + (1,)
# a = a + (1,)
# a += (('wqrerw', 'refre'),)
# print(a)
# t = tuple(lst)
# s = tuple(['a', 'b', 'c'])
# r = tuple('Hello world')
# print(t, s, r)
# a = (True, [1, 3, 4], 'hello', 5, {'red': 'красный'})
# a[1].append(5)
# print(a)
# del b  #удаляет кортеж b

# print(a.count('hello'))  #считает количество совпадений в кортеже
# print(a.index(5, 2, 4))  #ищет индекс первого совпадающего элемента кортежа с поз.2 по поз.4

# numbers_1: Tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# for i in range(len(numbers_1)):
#     print(numbers_1[i])
#
# for num in numbers_1:
#     print(num)

# print(*numbers_1)

# not_sorted_tuple: Tuple[int, ...] = (34, 1, 5, 6, 231, -1, 0, 43)
# print(not_sorted_tuple)
#
# sorted_tuple = tuple(sorted(not_sorted_tuple))
# print(sorted_tuple)

# notes: Tuple[str, ...] = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
# string1: str = ''.join(notes)
# string2: str = ', '.join(notes)
#
# print(string1)
# print(string2)

# letters: str = 'dasfghjkl'
# tpl: tuple = tuple(letters)
# print(tpl)


# ////////////////////////////////////////
# city = ('Voronezh', 'Sochi', 'Tula', 'Belgorod')
#
#
# def add_city(t: Tuple[str, ...], new_elem: str) -> None:
#     if new_elem not in t:
#         t += (new_elem,)
#         t = (new_elem,) + t
#         print(*t)
#
#
# add_city(city, 'Moscow')

# /////////////////////////////////////////

# t2 = (34, 1, 0, 5, 6, 231, -1, 0, 1, 43)
#
#
# def uniq_tuple(t: Tuple[int, ...]) -> None:
#     uniq_t: tuple = ()
#     for i in t:
#         if i not in uniq_t:
#             uniq_t += (i,)
#     print(*uniq_t)
#
#
# uniq_tuple(t2)

# /////////////////////////////////////////

# tup1 = ((1, 0, 0, 0, 0),
#         (0, 1, 0, 0, 0),
#         (0, 0, 1, 0, 0),
#         (0, 0, 0, 1, 0),
#         (0, 0, 0, 0, 1))
#
#
# def cut_tuple(t: Tuple[int, ...], n: int) -> None:

# /////////////////////////////////////////

# МНОЖЕСТВА

# a = {1, 2, 3, 'hello'}
# print(a)
# a = {1, 2, 3, 'hello', 1, 2, 3}  # повторяющиеся значения отбрасываются
# print(a)

# b = set()  # создание пустого множества
# c = set('qwertyqwerty')
# print(c)

# d = set(range(1, 12))
# print(d)
#
# lst = [1, 1, 2, 2, 2, 3, 4, 5, 6]
# e = list(set(lst))
# print(e)

# for i in d:
#     print(i, end='')

# d[0] нельзя так назначать

# d.add(20)
# print(d)

# d.update('w', (22, 37))  #добавление иттерируемых последовательностей
# print(d)
#
# d.discard('w')  #не вызывает ошибку при повторном удалении
# print(d)
#
# d.remove(1)  #вызывает ошибку при повторном удалении
# print(d)

# a = d.pop()  #удаляет случайный элемент множества
# print(a)
#
# d.clear()  #очищает множество
# print(d)


# ПЕРЕСЕЧЕНИЕ МНОЖЕСТВ
# set_a: Set[int] = {1, 2, 3, 4}
# set_b: Set[int] = {3, 4, 5, 6, 7}

# res_1: set = set_a & set_b
# res_2: set = set_a.intersection(set_b)
#
# print(res_1, res_2)

# ОБЪЕДИНЕНИЕ МНОЖЕСТВ
# res_3: set = set_a | set_b
# res_4: set = set_a.union(set_b)
#
# print(res_3, res_4)

# ВЫЧИТАНИЕ МНОЖЕСТВ
# res_5: set = set_a - set_b
# res_6: set = set_b - set_a
#
# print(res_5, res_6)

# СИММЕТРИЧНАЯ РАЗНИЦА (ВСЕ КРОМЕ ПОВТОРЯЮЩИХСЯ)
# res_7: set = set_b ^ set_a
#
# print(res_7)

# print({1, 2, 3} == {1, 3, 2})
# print({1, 2, 3} == {3, 3, 2})
# print({1, 2, 3, 4} > {3, 1, 2})  #если все эл-ты одного множества содержат элементы второго, то первое больше второго
# print({1, 2, 3, 4} > {3, 1, 2, 5})
# print({1, 2, 3, 4} < {3, 1, 2, 5, 7})

# lst = [1, 3, 5]
# tpl = (3, 4, 5)
# str1 = 'abcde'
#
# my_set = {1, 2, 3, 4, 5}
#
# print(my_set.union(str1))
# print(my_set.intersection(lst))
# print(my_set.difference(tpl))
# print(my_set.symmetric_difference(lst))


# digits: Set[int] = set()
#
# for c in input():
#     digits.add(int(c))
#
# digits = {int(c) for c in input()}

#НЕИЗМЕНЯЕМЫЕ МНОЖЕСТВА FROZENSET

a: set = set('Python')
b: frozenset = frozenset('Python')
print(a == b)
print(type(a))
print(type(b))

