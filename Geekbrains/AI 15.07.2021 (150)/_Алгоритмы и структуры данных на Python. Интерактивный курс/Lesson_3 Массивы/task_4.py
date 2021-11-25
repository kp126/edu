"""Определить, какое число в массиве встречается чаще всего."""


import random


array = [random.randint(0,9) for _ in range(30)]

print(array)

n = 0
max_count = 0
for i in set(array):
    if max_count < array.count(i):
        max_count = array.count(i)
        n = i

print(f'{n} встречается чаще всего! {max_count = }')