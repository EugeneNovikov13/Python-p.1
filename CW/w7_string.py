# str1 = 'Hello '
# str2 = "world"
# str3 = '''Hello
#   people and
#     everybody'''
# print(str3)

# msg1 = str1 + str2
# print(msg)

# msg2 = str1 * 5
# print(msg2)

# N = len(msg2)
# print(N)

# str4 = 'abcdefg57896'
# print('abc' in str4)
# print('0' in str4)
# print('87' in str4)

# print('asd' == 'asd')
# print('asd' == 'Asd')

# print(ord('a'))

# msg = 'Hello world!'
# print(msg[6:11])
# print(msg[:5])
# print(msg[6:])
# print(msg[:])
#
# print(msg[::2])
# print(msg[:5:2])
# print(msg[6::2])
# print(msg[1:6:2])
# print(msg[::-1])
#
# msg1 = msg[0]

# str1 = 'hello '
# str2 = 'python '
#
# res = str1 * 2 + str2 * 3
# print(res)
# ///////////////////
# str3 = 'I love Python'
#
# L = len(str3)
# res = str3[::L-1]
#
# print(res)
# ///////////////////
# str1 = 'Krivov'
#
# res = str1[1::2]
#
# print(res)
# ///////////////////

# str2 = 'Hello'
# str3 = 'Krivov'
#
# L = len(str2)
# res = str3[:L]
#
# print(res)
# ///////////////////
# str1 = 'hello'
# str2 = str1.upper()
# print(str2)
# res = str1.count('l')
# print(res)
# str3 = 'abrakadabra'
# res = str3.count('a', 2, 7)
# print(res)
# res = str3.find('d')
# print(res)
# res = str3.replace('a', '22')
# print(res)
# res = str3.rjust(20, '_')
# print(res)
# str4 = '1, 2,3,4 ,5'
# res = (str4.replace(' ', '')).split(',')
# print(res)

# ///////////////////
# str1 = '2+3+6.7 + 83 + 5.7 +1'
# str1 = str1.replace(' ', '')
# str1 = str1.replace('+', '-')
# print(str1)
# ///////////////////
# str1 = '0'
# str2 = '-100'
# str3 = '5.6'
# str4 = '-3'
# res1 = str1.rjust(10, ' ')
# res2 = str2.rjust(13, ' ')
# res3 = str3.rjust(12, ' ')
# res4 = str4.rjust(11, ' ')
# print(res1, res2, res3, res4, sep='\n')
# ///////////////////
# str1 = 'raabrakadabrahjghjrahjhkjra'
# str2 = 'ra'
#
# ind = 0
# while ind < len(str1):
#     res = str1.find(str2, ind)
#     ind = res + len(str2)
#     print(res)
# ///////////////////
# import string
# import random
#
# userLogin = ''.join(random.sample(string.ascii_lowercase, 6))
# userPass = ''.join(random.sample(string.ascii_letters + string.digits, 8))
#
# print(userLogin, userPass, sep='\n')

