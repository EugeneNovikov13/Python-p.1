# Задание 1
# Пользователь вводит с клавиатуры целое шестизначное число. Написать программу, которая определяет,
# является ли введенное число — счастливым (Счастливым считается шестизначное число, у которого сумма первых 3 цифр
# равна сумме вторых трех цифр).
# Например, 123321 — счастливое число, так как 1+2+3 = 3+2+1.
# С другой стороны 378423 несчастливое число, так как 3+7+8 != 4+2+3.
# Если пользователь ввел не шестизначное число требуется вывести сообщение об ошибке ввода.

# num = int(input('Enter 6-digit number: '))
#
# if num // 1e6 > 0 or num // 1e5 < 1:
#     print('Please enter SIX-DIGIT number!!!')
# else:
#     part1 = num // 1000
#     part2 = num % 1000
#     if part1 // 100 + (part1 // 10) % 10 + part1 % 10 == part2 // 100 + (part2 // 10) % 10 + part2 % 10:
#         print('It is a HAPPY NUMBER!')
#     else:
#         print('Sorry, try again.')

# Задание 2
# Пользователь вводит шестизначное число. Необходимо поменять в этом числе первую и шестую цифры,
# а также вторую и пятую цифры.
# Например, 723895 должно превратиться в 593827.
# Если пользователь ввел не шестизначное число требуется вывести сообщение об ошибке ввода.

# num = int(input('Enter 6-digit number: '))
#
# if num // 1e6 > 0 or num // 1e5 < 1:
#     print('Please enter SIX-DIGIT number!!!')
# else:
#     dig1 = num // 100000
#     dig2 = (num // 10000) % 10
#     dig3 = (num // 1000) % 10
#     dig4 = (num // 100) % 10
#     dig5 = (num // 10) % 10
#     dig6 = num % 10
#     if dig6 == 0:
#         print('String result: ', dig6, dig5, dig3, dig4, dig2, dig1, sep='')
#     # на случай, если последней цифрой в введенном числе будет 0
#     else:
#         math_res = dig6 * 100000 + dig5 * 10000 + dig3 * 1000 + dig4 * 100 + dig2 * 10 + dig1
#         print('Integer result:', math_res)

# Задание 3
# Пользователь вводит с клавиатуры номер месяца (от 1 до 12). В зависимости от полученного номера месяца программа
# выводит на экран надпись: Winter (если введено значение 1,2 или 12), Spring (если введено значение от 3 до 5),
# Summer (если введено значение от 6 до 8), Autumn (если введено значение от 9 до 11).
# Если пользователь ввел значение не в диапазоне от 1 до 12 требуется вывести сообщение об ошибке.

# month = int(input('Enter number of month: '))
#
# if not 1 <= month <= 12:
#     print('There are only 12 month in the year!')
# elif 3 <= month <= 5:
#     print('It is spring')
# elif 6 <= month <= 8:
#     print('It is summer!!!')
# elif 9 <= month <= 11:
#     print('It is autumn')
# else:
#     print('It is winter :^(')

# Задание 4
# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без остатка) нужно
# вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести Fizz Buzz.
# Если число не кратно не 3 и 5 нужно вывести само число.
# Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.

# num = int(input('Enter number [1-100]: '))
#
# res = num
#
# if num < 1 or num > 100:
#     res = 'Enter number from 1 to 100!'
#
# else:
#     fizz = 1 if num % 3 == 0 else 0
#     buzz = 1 if num % 5 == 0 else 0
#     if fizz == 1 and buzz == 0:
#         res = 'Fizz'
#     elif fizz == 0 and buzz == 1:
#         res = 'Buzz'
#     elif fizz == 1 and buzz == 1:
#         res = 'Fizz Buzz'
#
# print(res)

# Задание 6
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%.
# Пользователь вводит с клавиатуры уровень продаж для трех менеджеров. Определить их зарплату, определить
# лучшего менеджера, начислить ему премию 200$, вывести итоги на экран.

# man1_sales = float(input('Enter sales amount of manager 1: '))
# man2_sales = float(input('Enter sales amount of manager 2: '))
# man3_sales = float(input('Enter sales amount of manager 3: '))
#
# salary = bonus = 200
#
# if man1_sales <= 500:
#     man1_salary = salary + man1_sales * 3 / 100
# else:
#     if 500 < man1_sales <= 1000:
#         man1_salary = salary + man1_sales * 5 / 100
#     else:
#         man1_salary = salary + man1_sales * 8 / 100
#
# if man2_sales <= 500:
#     man2_salary = salary + man2_sales * 3 / 100
# else:
#     if 500 < man2_sales <= 1000:
#         man2_salary = salary + man2_sales * 5 / 100
#     else:
#         man2_salary = salary + man2_sales * 8 / 100
#
# if man3_sales <= 500:
#     man3_salary = salary + man3_sales * 3 / 100
# else:
#     if 500 < man1_sales <= 1000:
#         man3_salary = salary + man3_sales * 5 / 100
#     else:
#         man3_salary = salary + man3_sales * 8 / 100
#
# if man1_sales > man2_sales and man1_sales > man3_sales:
#     sales_max = 'Manager 1'
#     man1_salary += bonus
# else:
#     if man2_sales > man1_sales and man2_sales > man3_sales:
#         sales_max = 'Manager 2'
#         man2_salary += bonus
#     else:
#         sales_max = 'Manager 3'
#         man3_salary += bonus
#
# print('The best seller of the month is', sales_max)
# print('Salary of manager:', '\n'
#       'Manager 1:', man1_salary, '\n'
#       'Manager 2:', man2_salary, '\n'
#       'Manager 3:', man3_salary)

# Задание*
# Вводится целое число k (1 <= k <= 365). Определить, каким днем недели (понедельник, вторник, среда, четверг, пятница,
# суббота или воскресенье) является k-й день не високосного года, в котором 1 января является понедельником.

# year_day = int(input('Enter number of year\'s day: '))
#
# week_day_number = year_day % 7
#
# if week_day_number == 1:
#     week_day = 'Monday'
# elif week_day_number == 2:
#     week_day = 'Tuesday'
# elif week_day_number == 3:
#     week_day = 'Wednesday'
# elif week_day_number == 4:
#     week_day = 'Thursday'
# elif week_day_number == 5:
#     week_day = 'Friday'
# elif week_day_number == 6:
#     week_day = 'Saturday'
# else:
#     week_day = 'Sunday'
#
# print(week_day)

# Задание**
# Работа светофора для пешеходов запрограммирована следующим образом: в начале каждого часа в течение трех минут горит
# зеленый сигнал, затем в течение двух минут – красный, в течение трех минут – опять зеленый и т. д.
# Дано вещественное число t, означающее время в минутах, прошедшее с начала очередного часа.
# Определить, сигнал какого цвета горит для пешеходов в этот момент.
# На экран вывести сообщение (без кавычек) "green" - для зеленого и "red" - для красного.

# t = float(input('Enter time in minutes since the beginning of the hour [0-60]: '))
#
# time_of_period = t % 5
#
# if 0 < time_of_period < 3:
#     res = 'green'
# elif 3 < time_of_period < 5:
#     res = 'red'
# else:
#     res = 'traffic light switches'
#
# print(res)
