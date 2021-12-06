"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный
массив, заданный случайными числами на промежутке [0; 50). Выведите на экран
исходный и отсортированный массивы.
"""
from random import randint
import timeit
import random

N = 50
array = []

for i in range(N):
    array.append(randint(0, 50))

for i in array:
    print(i, end=' ')


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


orig_list = [random.randint(0, 50) for _ in range(10)]
print('Одномерный вещественный массив:')
# замеры 10
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1))
print('----------------------------------------------------------')
orig_list = [random.randint(0, 50) for _ in range(100)]

# замеры 100
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1))
print('----------------------------------------------------------')
orig_list = [random.randint(0, 50) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1))

print('Сортировка слияния:')