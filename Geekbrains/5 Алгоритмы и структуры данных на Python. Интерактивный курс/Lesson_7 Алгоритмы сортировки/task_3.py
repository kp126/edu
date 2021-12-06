"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным
образом. Найдите в массиве медиану. Медианой называется элемент ряда,
делящий его на две равные части: в одной находятся элементы, которые не
меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если
это слишком сложно, используйте метод сортировки, который не рассматривался
на уроках (сортировка слиянием также недопустима).
"""
import random
import time


def find_median(list_, n=0):
    random_index = random.randint(0, len(list_) - 1)
    list_a, list_b, list_c = [], [], []
    num = list_[random_index]
    for x in list_:
        if x < num:
            list_a.append(x)
        elif x > num:
            list_b.append(x)
        else:
            list_c.append(x)
    if len(list_c) > 1:
        while len(list_c) != 1:
            append = list_a if len(list_c) % 2 == 0 else list_b
            append.append(list_c.pop())
    if len(list_a) + n == len(list_b):
        return list_[random_index]
    elif len(list_a) + n > len(list_b):
        n -= len(list_b) + 1
        return find_median(list_a, n)
    elif len(list_b) > len(list_a) + n:
        n += len(list_a) + 1
        return find_median(list_b, n)


random.seed(42)
some_list = [random.randint(-100, 100) for _ in
             range(random.randint(5, 50000) * 2 + 1)]
start = time.time()

print('median result', find_median(some_list), round((time.time() - start), 4))
start = time.time()

print('sorted result', sorted(some_list)[len(some_list) // 2],
      round((time.time() - start), 4))