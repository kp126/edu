

print('Привет! Сегодня не особо интересная реализация:\n'
      'я решил больше уделять внимания CodeWars в свободное время.\n'
      'Воть туть я: https://www.codewars.com/users/K.Peremyshlev\n\n'
      'Приступим!\n')

print('1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.\n'
      'Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.\n')


def division(a, b):
    while True:
        try:
            return a / b
        except ZeroDivisionError:
            try:
                b = int(input('На 0 делить нельзя, введи другое число: '))
            except ValueError:
                while True:
                    try:
                        b = int(input('Anti-duracheck! Введи число: '))
                        break
                    except ValueError:
                        continue


print('Сейчас нужно будет ввести два числа.\nПервое будет разделено на второе!\n')
while True:
    try:
        a, b = int(input('Введи число A: ')), int(input('Введи число B: '))
        break
    except ValueError:
        print('Нужно ввести числа! Попробуй ещё раз!')
print('\n', division(a, b), '- это результат работы функции\n\n')

print('Дополнительно написал через lambda, но не нашел как в неё заталкать исключения...\n'
      'Так что играем по правилам: никаких B == 0, а также не используй буквы/символы\n')
print((lambda a, b: a / b)(a=int(input('Введи A: ')), b=int(input('Введи B: '))), '- это результат lamdba-func\n')

print('2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:\n'
      'имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать\n'
      'параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.\n')


def customer_data(*args):
    return f'Имя: {name.capitalize()}, Фамилия: {surname.capitalize()}, Год рождения: {birthday}, ' \
           f'Город проживания: {current_city.capitalize()}, Email: {email}, Номер телефона: {phone}'


name, surname, birthday, current_city, email, phone = input('Введи имя: '), input('Введи фамилию: '), input(
    'Введи год рождения: '), input('Введи город проживания: '), input('Введи email: '), input('Введи телефон: ')
data = name, surname, birthday, current_city, email, phone
print('\n\n', customer_data(data), '\n')

print('3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,\n'
      'и возвращает сумму наибольших двух аргументов.\n')


def my_func(a, b, c):
    q = (a, b, c)
    q = sorted(q)
    return f'Самое большое число {q[2]}\nВторое по величине {q[1]}\nИх сумма {q[1] + q[2]}'


while True:
    try:
        a, b, c = int(input('Введи первое число: ')), int(input('Введи второе число: ')), int(
            input('Введи третье число: '))
        break
    except ValueError:
        print('Нужно ввести цифры! Попробуй ещё раз!\n')
print(my_func(a, b, c), '\n')

print('4. Программа принимает действительное положительное число x и целое отрицательное число y.\n'
      'Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать\n'
      'в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной\n'
      'функции возведения числа в степень.\n\n'
      'Подсказка: попробуйте решить задачу двумя способами.\n'
      'Первый — возведение в степень с помощью оператора **.\n'
      'Второй — более сложная реализация без оператора **, предусматривающая использование цикла.\n')


def my_func(x, y):
    return x ** y


def my_func2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


while True:
    try:
        x, y = int(input('Введи x: ')), int(input('Введи y: '))
        if x <= 0:
            print('Число "x" должно быть больше 0! Попробуй ещё раз!')
            continue
        if y >= 0:
            print('Число "y" должно быть меньше 0! Попробуй ещё раз!')
            continue
        break
    except ValueError:
        print('Нужно ввести цифры! Попробуй ещё раз!\n')

print(my_func(x, y), '- это результат my_func')
print(my_func2(x, y), '- это результат my_func2')

print('5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.\n'
      'При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить\n'
      'ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел\n'
      'будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный\n'
      'символ, выполнение программы завершается. Если специальный символ введен после\n'
      'нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее\n'
      'сумме и после этого завершить программу.\n')


def customer_sum():
    sum_now = 0
    ex = False
    while ex == False:
        result = 0
        print('\nЕсли ввести не число, то програма завершится!')
        number = input('Введи числа через пробел: ').split()
        for el in range(len(number)):
            if number[el] is str:
                ex = True
                break
            else:
                try:
                    result += int(number[el])
                except ValueError:
                    ex = True
                    break
        sum_now += result
        print(f'Сейчас сумма = {sum_now}')
    return print(f'Итого, {sum_now}', '\n')


customer_sum()

print('6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв\n'
      'и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.\n'
      'Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.\n'
      'Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,\n'
      'но каждое слово должно начинаться с заглавной буквы. Необходимо использовать\n'
      'написанную ранее функцию int_func().\n')


def int_func(*args):
    return args[1].title()


while True:
    print('Для выхода из программы введи %%%')
    my_str = input('Введи слово или слова с маленькой буквы через пробел: ')
    if my_str == '%%%':
        break
    print(int_func(my_str, '\n'))
