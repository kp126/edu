"""5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве."""

import random

array = [random.randint(-100, 5) for _ in range(30)]

print(array)

mnn = 0  # maximum negative number

for index, el in enumerate(array):
    if el < 0:
        mnn = el
        break

for i in array[index+1:]:
    if mnn < i < 0:
        mnn = i

print(mnn)
