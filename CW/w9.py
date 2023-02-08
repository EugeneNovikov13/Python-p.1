# a, z = input('Enter letters: ').split()
#
# print(f'Codes: {a} = {ord(a)}, {z} = {ord(z)}')
# /////////////////////////
# str1 = input('Enter slag: ')
# str2 = str1.replace('---', '-').replace('--', '-')
#
# print(str2)
#/////////////////////////
# fill = '0'
#
# for i in input('Enter numbers: ').split():
#     print(f'{i.rjust(3, fill)}', sep='\n')

# [print(i.rjust(3, '0')) for i in input('Enter numbers: ').split()]
# ///////////////////////
# name = 'Master'
# author = 'Bulgackov'
# page = 233
# price = 435.45
# book = [name, author, page, float(price)]
# print(book)
# book[1] = 'Pushkin'
# book[3] = book[3] * 2
# del book[2]
# print(book)
# ///////////////////////
# lst = [int(i) for i in input('Enter numbers: ').split()]
# print(max(lst), min(lst), sum(lst))
# ///////////////////////
x, *y, z = 'I want in IT!'
print(y)

# a = [1, 2]
# print(*a)

a = [1, 8]
# range(*a)
# print(list(range(*a)))
# print([*range(*a)])

# d = [10, 20]
# print([*range(*a), *['I am cool'], *d])
# ///////////////////////
# phone = list(input('Enter phone-number: '))
# del phone[0:2]
# phone.insert(0, '8')
# lst1 = ''.join(phone).replace('-', '')
# print(''.join(lst1))
#
# print(input().replace('+7', '8').replace('-', ''))
# ///////////////////////


