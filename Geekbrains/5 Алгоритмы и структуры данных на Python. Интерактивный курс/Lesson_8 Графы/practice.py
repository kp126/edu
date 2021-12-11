from collections import namedtuple

# Представление графов

# Матрицы смежности
# Простой граф
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]
print(*graph, sep='\n')
print('*' * 50)

# Направленный граф
graph = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]
print(*graph, sep='\n')
print('*' * 50)
'''Если разделить из левого верхнего угла в правый нижний,
то такая линия не будет линией симметрии.

!Отсутствие такой симметрии говорит что в матрице смежности хранится
направленный граф!'''

# Взвешанный граф

# graph[0][1:3] = [2,3]
# graph[1][2] = 2
# graph[2][1] = 2

graph = [
    [0, 2, 3, 0],
    [0, 0, 2, 1],
    [0, 2, 0, 0],
    [0, 0, 0, 0]
]
print(*graph, sep='\n')
print('*' * 50)

##########
# Списки смежности
# Простой граф
graph = []

graph.append([1, 2])
graph.append([0, 2, 3])
graph.append([0, 1])
graph.append([1])

print(*graph, sep='\n')
print('*' * 50)

# 2
graph_2 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1},
}

print(graph_2)
print('*' * 50)

# Направленный граф
Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph_3 = []

graph.append([Vertex(1, 2), Vertex(2, 3)])
graph.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph.append([Vertex(0, 3), Vertex(1, 2)])
graph.append([Vertex(1, 1)])

print(*graph_3, sep='\n')
print('*' * 50)


class Graph:
    def __init__(self, vertex, edge, spam):
        self.vertex = vertex
        self.edge = edge
        self.spam = spam


# Список рёбер
graph = [(0, 1), (0, 2), (1, 2), (2, 1), (1, 3)]
# добаляем 3-ий элемент если граф взвешанный
print(*graph, sep='\n')
print('*' * 50)

'''Поиск кратчайшего пути в ширину
Breadth-First Search'''

from collections import deque

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]


def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:

        curent = deq.pop()

        if curent == finish:
            # return parent
            break
        for i, vertex in enumerate(graph[curent]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = curent
                deq.appendleft(i)
    else:
        return f'Изв вершины {start} нельзя попасть в вершину {finish}'

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f'Кратчайший путь {list(way)} длинною в {cost} условных единиц'


print(bfs(g, 2, 5))

'''Алгоритм Дейкстры
для поиска кратчайшего пути на взвешенном графе (вес положительное число)'''
g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]
