"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться."""

from random import randint as rnd

array = [rnd(1, 20) for _ in range(10)]

print(array)

for i in range(len(array)-1):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]


print(*array[:2])
