"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным
и максимальным элементами. Сами минимальный и максимальный элементы в сумму
не включать."""

import random

array = [random.randint(0, 100) for _ in range(10)]

print(array)

n_min = array[0]
n_max = array[0]
i_min = 0
i_max = 0

for i, n in enumerate(array):
    if n_min > n:
        n_min = n
        i_min = i
    elif n_max < n:
        n_max = n
        i_max = i

if i_min > i_max:
    i_min, i_max = i_max, i_min
summa = sum(array[i_min + 1:i_max])

print(summa)
