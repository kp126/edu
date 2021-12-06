"""9. Найти максимальный элемент среди минимальных
элементов столбцов матрицы."""


import random


array = [[random.randint(1,50) for _ in range(5)] for _ in range(5)]
print(*array, sep='\n')
c = []
b = -1
for el in range(5):
    a = array[0][el]
    for i in range(5):
        if array[i][el] < a:
            a = array[i][el]
    c.append(a)
    if a > b:
        b = a


print(f"Минимальные элементы столбцов {c}, максимальный из них {b}")
