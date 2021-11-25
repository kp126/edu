"""3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы."""

import random


array = [random.randint(0, 100) for _ in range(10)]

print(array)

"""т.к. неизвестно максимальное и минимальное случайное число в массиве
назначаю и минимум и максимум первым элементом массива"""
n_max = array[0]
n_min = array[0]
i_min = 0
i_max = 0
for i, n in enumerate(array):
    if n > n_max:
        n_max = n
        i_max = i
    if n < n_min:
        n_min = n
        i_max = i

# меняю местами
array[i_min], array[i_max] = array[i_max], array[i_min]
print(array)
