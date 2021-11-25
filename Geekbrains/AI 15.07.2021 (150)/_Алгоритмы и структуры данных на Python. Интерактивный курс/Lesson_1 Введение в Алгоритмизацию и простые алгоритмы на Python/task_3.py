# 3. Написать программу, которая генерирует в указанных пользователем границах
# ●	случайное целое число,
# ●	случайное вещественное число,
# ●	случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся
# эти символы. Программа должна вывести на экран любой символ алфавита
# от 'a' до 'f' включительно.

import random


def randchar(a, b):
    return chr(random.randint(ord(a), ord(b))) if a < b else chr\
        (random.randint(ord(b), ord(a)))


def randint(a, b):
    return random.randint(a, b) if a < b else random.randint(b, a)


def randuni(a, b):
    return random.uniform(a, b) if a < b else random.uniform(b, a)


def bounds(str):
    num_list = str.split(',')
    a = int(num_list[0])
    b = int(num_list[1])
    return a, b


choise = int(input('Введите номер действия\n'
                   '1. Вывод случайного целого числа\n'
                   '2. Вывод случайного вещественного числа\n'
                   '3. Вывод случайного символа\n'))
if choise != 1 and choise != 2 and choise != 3:
    exit('Введен неверный номер действия')

if choise == 1:
    d1 = input('Введите диапазон для случайного целого числа '
               '(2 цифры через запятую)')
    a, b = bounds(d1)
    print(randint(a, b))

if choise == 2:
    d1 = input('Введите диапазон для случайного вещественного числа '
               '(2 цифры через запятую)')
    a, b = bounds(d1)
    print(randuni(a, b))

if choise == 3:
    d1 = input('Введите диапазон для случайной буквы (2 буквы через запятую)')
    char_list = d1.split(',')
    a = char_list[0]
    b = char_list[1]
    print(randchar(a, b))