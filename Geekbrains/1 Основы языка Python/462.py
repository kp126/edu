from sys import argv
from itertools import cycle

name, number = argv

number = int(number)

print("Указанное число: ", number)

с = 1
for el in cycle("ABC"):
    if с > number:
        break
    print(с, el)
    с += 1


