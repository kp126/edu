"""1. Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему."""

import cProfile
import random
import numpy as np

"""Урок 3. Массивы.
Задача 5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве."""

"""Для использования cProfile нужно снять комментарий ниже"""
# array1 = [random.randint(-100, 5) for _ in range(50)]
# array2 = [random.randint(-1000, 50) for _ in range(500)]
# array3 = [random.randint(-10000, 500) for _ in range(5000)]
# array4 = [random.randint(-100000, 5000) for _ in range(50000)]
# array5 = [random.randint(-1000000, 50000) for _ in range(500000)]
#
# arrays = [array1, array2, array3, array4, array5]


"""Для генерации новых списков для теста timeit
Нужно снять комментарий выше и ниже и выполнить код"""
# for i, array in enumerate(arrays):
#     with open(f'array{i}.txt',
#     'w+', encoding='UTF-8') as file:
#         file.write(str(array))

def max_negative_number(array):
    with open(f'{array}.txt', 'r', encoding='utf-8') as file:
        array = file.readline().strip('[').strip(']').split(', ')
        array = np.array(array, dtype='int')
    mnn = 0  # maximum negative number
    for index, el in enumerate(array):
        if el < 0:
            mnn = el
            break
    for i in array[index + 1:]:
        if mnn < i < 0:
            mnn = i
            if mnn == 1:
                break
    return mnn

max_negative_number('array0')

"""Для запуска нужно снять комментарий в верхнем блоке генерации списков
Ниже есть результаты"""
# for array in arrays:
#     cProfile.run(f'max_negative_number({array})')


#cProfile
#   ncalls tottime  percall  cumtime  percall    filename:lineno(function)
# 1:  1     0.001    0.001    0.001    0.001  {built-in method builtins.exec}
# 2:  1     0.001    0.001    0.002    0.002  {built-in method builtins.exec}
# 3:  1     0.015    0.015    0.015    0.015  {built-in method builtins.exec}
# 4:  1     0.167    0.167    0.174    0.174  {built-in method builtins.exec}
# 5:  1     4.403    4.403    4.473    4.473  {built-in method builtins.exec}

"""Команды для терминала"""
# python -m timeit -n 1000 -s "import task_1" "task_1.max_negative_number('array0')"
# python -m timeit -n 1000 -s "import task_1" "task_1.max_negative_number('array1')"
# python -m timeit -n 1000 -s "import task_1" "task_1.max_negative_number('array2')"
# python -m timeit -n 1000 -s "import task_1" "task_1.max_negative_number('array3')"
# python -m timeit -n 1000 -s "import task_1" "task_1.max_negative_number('array4')"

"""Первые результаты"""
# "task_1.max_negative_number('array0')"
# len 50:     1000 loops, best of 5:  380   usec per loop
# len 500:    1000 loops, best of 5:  149   usec per loop
# len 5000:   1000 loops, best of 5:  2.36  msec per loop
# len 50000:  1000 loops, best of 5:  23.9  msec per loop - долго
# len 500000: 1000 loops, best of 5:  257   msec per loop - очень-очень долго

