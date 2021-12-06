"""
Сортировка пузырьком

Сложность: O(n**2)
Устойчивость (стабильность): Устойчивая
Тип (категория): Обменная
Потребление памяти: Не требует доп. памяти
"""
import random

print('\nСотрировка пузырьком')
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

n = 1
while n < len(array):
    for i in range(len(array) - n):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    n += 1
    # print(array)

print(array)

"""
Сортировка выбором

Сложность: O(n**2)
Устойчивость (стабильность): Устойчивая/неустойчивая
Тип (категория): Выбором
Потребление памяти: Не требует доп. памяти
"""
print('\nСотрировка выбором')
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def selection_sort(array):
    for i in range(len(array)):
        ind_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[ind_min]:
                ind_min = j

        array[ind_min], array[i] = array[i], array[ind_min]
        # print(array)


selection_sort(array)
print(array)

"""
Сортировка вставками

Сложность: O(n**2) / лучшее время O(n)
Устойчивость (стабильность): Устойчивая
Тип (категория): Вставками
Потребление памяти: Не требует доп. памяти
"""
print('\nСотрировка вставками')
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1

        array[j] = spam
        # print(array)


insertion_sort(array)
print(array)

"""
Сортировка Шелла

Сложность: O(n**2) / O(n (log n)**2) или O(n**3/2)
Устойчивость (стабильность): Неустойчивая
Тип (категория): Вставками
Потребление памяти: Не требует доп. памяти
"""
print('\nСотрировка Шелла')
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def shell_sort(array):
    assert len(array) < 4000, 'Массив слишком большой. Используйте другую ' \
                              'сортировку'

    def new_increment(array):

        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

        while len(array) <= inc[-1]:
            inc.pop()

        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                # print(array)


shell_sort(array)
print(array)

"""
Быстрая сортировка. Сортировка Хоара.

Сложность: O(n**2) / O(n log n)
Устойчивость (стабильность): Неустойчивая
Тип (категория): Обменная
Потребление памяти: O(n) / Не требует доп. памяти
"""
print('\nБыстрая сортировка. Сортировка Хоара.')
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []

    for item in array:

        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('Случилось непредвиденное')

    print(s_ar, m_ar, l_ar)
    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)


array_new = quick_sort(array)
print(array_new)

print('\nБыстрая сортировка. Сортировка Хоара. Без доп. памяти')
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def quick_sort_no_memory(array, fst, lst):
    if fst >= lst:
        return

    # print(array)

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)


quick_sort_no_memory(array, 0, len(array) - 1)
print(array)

"""
Разворот массива
"""
print('\nРазворот массива')
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def reverse(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - 1 - i] = array[len(array) - 1 - i], array[
            i]


reverse(array)
print(array)

array.reverse()
print(array)

array.sort()
print(array)

array.sort(reverse=True)
print(array)

print('*' * 50)
t = tuple(random.randint(0, 100) for _ in range(size))
print(t)

# t.sort()
t = tuple(sorted(t, reverse=True))
print(t)

"""
Алгоритм сортировки Timsort

Сложность: O(n log n)
Устойчивость (стабильность): Устойчивая
Тип (категория): Гибридная (Вставками + Слиянием)
Потребление памяти: O(n)

!Самостоятельное извучение
"""

"""
Сортировка сложных структур с использованием ключа
"""
from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', 'name age')

p_1 = Person('Vasya', 25)
p_2 = Person('Kolya', 30)
p_3 = Person('Olya', 23)

people = [p_1, p_2, p_3]


def by_age(person):
    return person.age


result = sorted(people, key=by_age)
print(result)

result_2 = sorted(people, key=attrgetter('age'))
print(result_2)
