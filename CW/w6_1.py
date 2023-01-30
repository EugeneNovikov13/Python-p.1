# num = 1
# summa = 0
#
# while num != 0:
#     num = int(input('Enter number: '))
#     summa += num
#
# print(summa)

# num = int(input('Enter number: '))
#
# summa = 0
#
# while num > 0:
#     summa += 1 / num
#     num -= 1
#
# print(round(summa, 3))

# try:
#     deposit = float(input('Enter deposit: '))
#     percent = float(input('Enter percent: '))
#     years = int(input('Enter years: '))
#
#     if deposit < 0 or years < 0:
#         raise ValueError('Only positive numbers')
#
#     while years > 0:
#         deposit += deposit * percent / 100
#         years -= 1
#
#     print(round(deposit, 2))
#
# except ValueError as err:
#     print(err)

# num = 1
# res = 1
#
# while num != 0:
#     num = float(input('Enter number: '))
#     if num > 0:
#         res *= num
#
# print(res)

# num2 = int(input('Enter number: '))
#
# n = 1
#
# while num2 >= n**2:
#     n += 1
#
# print(n)

# num_a = int(input('Enter number: '))
#
# for i in range(1, num_a + 1):
#     if num_a % i == 0:
#         print(i)

# num_n = int(input('Enter number: '))
#
# for i in range(2, num_n):
#     if num_n % i == 0:
#         print('Number is not simple')
#         break
#
# else:
#     print('Number is simple')

num_x = int(input('Enter number: '))

res = 0

for i in range(3, num_x):
    if i % 3 == 0 or i % 5 == 0:
        res += i

print(res)

