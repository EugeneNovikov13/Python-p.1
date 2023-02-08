# import re
#
# text = 'Google, Gooogle, Goooooogle'
# match = re.findall(r'o{2, 5}', text)
#
# phone = '546144843678921'
# match = re.findall(r'8\d{10}', phone)
# print(type(match))

# lst = ['Moscow', 'Voronezh', 'Tver', 'Saint-Peterbourg', 'Kazan']
# lst1 = []
# lst2 = list()
#
# print(lst[0])
# print(lst[-1])
# print(lst[len(lst)-1])

# for city in lst:
#     print(city)

# lst[0] = 'Samara'
# print(lst)

# digs = [-1, 0, 5, 3, 2]
#
# for i in range(len(digs)):
#     digs[i] **= 2
# print(digs)

# digs = [0] * 100
# n = 0
# x = 0
# while x >= 0:
#     x = int(input('Enter number: '))
#     digs[n] = x
#     n += 1
# print(digs)
#
# _sum = 0
# for i in range(n):
#     _sum += digs[i]
# _sum = _sum / n

# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(A[1][2])
#
# A += ['Voronezh', 6]
# print(A)
#
# print(6 in A)

# lst = ['Moscow', 'Voronezh', 'Tver', 'Saint-Peterbourg', 'Kazan']
# digs = [-1, 0, 5, 3, 2]

# print(max(digs))
# print(min(digs))
# print(min(A))
# print(min(lst))

# print(sorted(digs))
# print(digs)
# print(sorted(digs, reverse=True))
#
# print([1, 2, 3] == [1, 2, 3])
#
# print(sum(digs))

# lst = [-1, 0, 5, 3, 2]
# for i in range(len(lst)):
#     lst[i] += 7.2
# print(lst)
#
# lst = []
# x = 1
# N = int(input('Enter N: '))
# for i in range(N):
#     x = input('Enter something: ')
#     lst += [x, x]
# print(lst)
#
# lst = []
# N = int(input('Enter N: '))
# for i in range(N):
#     x = input('Enter something: ')
#     lst += [x]
# if '5' in lst:
#     print('Yes')
# else:
#     print('No')

# lst = ['Moscow', 'Voronezh', 'Tver', 'Saint-Peterbourg', 'Kazan']
# print(lst[1:3])
# print(lst[-2:999])
# print(lst[::2])

# lst[1:3] = 'Novgorod', 'Sochi', 'Volgograd'
# print(lst)

# del lst[0]
# print(lst)

# lst = [1, -54, 3, 23, 43, -45, 0]
# lst.append(100)
# lst.append([1, 2, 3])
# x = 8
# lst.append(x)
# print(lst)

# lst.insert(3, -99)
# print(lst)

# lst.remove(1)

# x = lst.pop()
# y = lst.pop(2)
# print(lst, x, y)

# lst.clear()

# lst2 = lst.copy()
#
# print(lst2, lst == lst2, lst is lst2)

# x = lst.index(0)
# print(x)

# x = lst.index(43, 2, 5)
# print(x)

# lst.reverse()
# print(lst)

# lst.sort()
# lst.sort(reverse=True)
# print(lst)

# A = []
# N = 10
# for x in range(N+1):
#     A.append(x ** 2)
# print(A)

# list comprehension
# N = 10
# A = [x ** 2 for x in range(N+1)]
# B = [_ ** 2 for _ in range(N+1)]
# print(A, B)

# N = 10
# A = [x ** 2 for x in range(N) if x % 2 == 0]
# print(A)
#
# cities = ['Moscow', 'Voronezh', 'Tver', 'Saint-Peterbourg', 'Kazan']
# A = [city for city in cities if len(city) < 7]
# print(A)





