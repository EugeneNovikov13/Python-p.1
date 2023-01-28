# Имеется фрагмент программы
# При его выполнении возникает ошибка FileNotFoundError.
# Запишите конструкцию try / except, чтобы отображалось сообщение "File Not Found",
# если файл не удается открыть.

# try:
#     f = open('abc.txt')
#     r = f.read(1)
#     f.close()
# except FileNotFoundError:
#     print('file not found')

# Программа написана верно, однако содержат места потенциальных ошибок.
# ⦁	найдите потенциальные источники ошибок (укажите номера строк в строке документации);
# ⦁	используя конструкцию try добавьте в код обработку соответствующих исключений.

# try:
#     """User can enter not a number (string 19, 20)"""
#     a = float(input('a: '))
#     b = float(input('b: '))
#
#     if a * b < 0:
#         raise ValueError('One of number is negative')
#     else:
#         """Getting the square root of a negative number is impossible (string 26)"""
#         c = (a * b) ** 0.5
#     print(f'Middle geometric = {c}')
#
# except ValueError as err:
#     print(err)
