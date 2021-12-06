from sys import argv
from itertools import count

name, number = argv

number = int(number)

print("Указанное число: ", number)

for el in count(number):
    if el > number + 10:
        break
    else:
        print(el)
