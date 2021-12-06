from collections import Counter

a = Counter()
b = Counter('abracadarba')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b, c, d, sep='\n')

print(b['z'])
b['z'] = 0
print(b)

'''.elements() возвращает набор итерируемых элементов.
выводит элементы с положительным значением'''
print(list(b.elements()))

'''.most_common(n) возвращает n самых популярных элементов'''
print(b.most_common(2))

'''a.subtract(b) вычитает из коллекции а коллекцию b'''
g = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)
g.subtract(f)
print(g)

#############

from collections import deque

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

b = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)
print(b, c, sep='\n')

d = deque([i for i in range(5)], maxlen=7)
# добавить элемент в конец очереди
d.append(5)
# добавить элемент в начало очереди
d.appendleft(6)
print(d)

# добавить несколько элементов в конец очереди
d.extend([7, 8, 9])
# добавить несколько элементов в начало очереди
d.extendleft([10, 11, 12])  # 12 станет первым, 11 вторым, 10 третьим в очереди
print(d)

f = deque([i for i in range(5)], maxlen=7)
x = f.pop()  # взять справа элемент из очереди
y = f.popleft()  # взять слева элемент из очереди
print(f'{f=}', x, y, sep='\n')

# кол-во вхождений в очередь
g = deque([i for i in range(5)], maxlen=7)
print(g.count(2))
print(g.index(3))
g.insert(2, 6)
print(g)

# развернет очередь
g.reverse()
print(g)

# перенесет n элементов из правой в левую или наоборот, если n отрицательное
g.rotate(3)
print(g)

#############

from collections import defaultdict

a = defaultdict()
print(a)

s = 'adskflnasdfklkjfadsgkjahdjgkfdsfkladsjgeLKDS'
b = defaultdict(int)
for i in s:
    b[i] += 1
print(b)

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)
print(c)

list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1),
          ('cat', 2), ('dog', 5), ('cat', 1), ('mouse', 2), ('mouse', 1)]
d = defaultdict(set)
for k, v in list_2:
    d[k].add(v)
print(d)

f = defaultdict(lambda: 'unknown')
f.update(rex='dog', tomas='cat')
print(f)
print(f['rex'])
print(f['jerry'])

#############

from collections import OrderedDict

a = {'cat': 5, 'dog': 2, 'mouse': 4}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)

a = {'cat': 5, 'dog': 2, 'mouse': 4}
new_b = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
print(new_b)

print(new_b == new_a)

new_b.move_to_end('mouse', last=False)
print(new_b)

new_b.popitem(last=False)

new_b['cow'] = 1

#############

hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)


class Person:

    def __init__(self, name, race, health, mana, strength):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strength = strength
