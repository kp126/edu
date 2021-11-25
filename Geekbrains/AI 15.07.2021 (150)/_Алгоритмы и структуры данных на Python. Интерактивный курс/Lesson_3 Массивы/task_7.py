"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться."""

from random import randint as rnd

array = [rnd(1, 20) for _ in range(10)]

min_1 = array[0]
min_2 = array[0]

print(array)
for n in array[1:]:
    if min_1 > n:
        min_1 = n
        if min_1 > min_2:
            min_1 = min_2

print(min_1, min_2)
