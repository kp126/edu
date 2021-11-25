from abc import ABC, abstractmethod


class Matrix:
    """
    1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
    принимать данные (список списков) для формирования матрицы.
    Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
    Примеры матриц вы найдете в методичке.
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
    класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
    Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
    складываем с первым элементом первой строки второй матрицы и т.д.
    """

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_str = []
        matrix_str1 = []
        for el in self.matrix:
            matrix_str.append(str(el))

        for el in matrix_str:
            el = el.strip('[').strip(']').replace(', ', '\t')
            matrix_str1.append(el)

        matrix_str = '\n'.join(matrix_str1)
        return matrix_str

    def __add__(self, other):
        copy_matrix = self.matrix
        for el, o in enumerate(other.matrix):
            for ii, oo in enumerate(o):
                self.matrix[el][ii] += oo
        return copy_matrix


matrix1 = Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(matrix1)

matrix2 = Matrix(matrix1 + matrix1)
# matrix2 = matrix1 + matrix1
print(type(matrix2))
print(matrix2)

matrix3 = matrix1 + matrix2
print(type(matrix3))
print(matrix3)

print('*' * 50)
print(matrix1)

print(matrix2)

print(matrix3)


class Clothes(ABC):
    """
    2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
    К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
    размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
    для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def calculate(self):
        return


class Costume(Clothes):
    def calculate(self):
        return 2 * self.size + 0.3


class Coat(Clothes):
    def calculate(self):
        return self.size / 6.5 + 0.5


id0 = Costume('Costume name 1', 168)
id1 = Costume('Costume name 2', 173)
id2 = Costume('Costume name 3', 187)
id3 = Costume('Costume name 4', 182)
id4 = Costume('Costume name 5', 196)
id5 = Coat('Coat name 1', 38)
id6 = Coat('Coat name 2', 42)
id7 = Coat('Coat name 3', 44)
id8 = Coat('Coat name 4', 48)
id9 = Coat('Coat name 5', 54)

order_list = [id0, id1, id2, id3, id4, id5, id6, id7, id8, id9]

for i in order_list:
    print(f'Для {i.name} необходимо {i.calculate()} ткани')


class Cell:
    """
    3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
    В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
    В классе должны быть реализованы методы перегрузки арифметических операторов:
    сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
    Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
    и обычное (не целочисленное) деление клеток, соответственно.
    В методе деления должно осуществляться округление значения до целого числа.
    Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме
    ячеек исходных двух клеток.
    Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
    двух клеток больше нуля, иначе выводить соответствующее сообщение.
    Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
    количества ячеек этих двух клеток.
    Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
    количества ячеек этих двух клеток.
    В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
    Данный метод позволяет организовать ячейки по рядам.
    Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
    между \n равно переданному аргументу.
    Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
    Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
    Тогда метод make_order() вернет строку: *****\n*****\n**.
    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
    Тогда метод make_order() вернет строку: *****\n*****\n*****."""

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num % other.num)

    def make_order(self, param):
        cell_str = ('*' * param + '\n') * (self.num // param) + ('*' * (self.num % param))
        return cell_str


cell1 = Cell(5)
cell2 = cell1 + cell1
cell3 = cell1 * cell1
cell4 = cell3 / cell2
print(f'{cell1.num = }')
print(f'{cell2.num = }')
print(f'{cell3.num = }')
print(f'{cell4.num = }')

print(f'Это make_order(3) для {cell1.num = }\n{cell1.make_order(3)}\n')
print(f'Это make_order(4) для {cell2.num = }\n{cell2.make_order(4)}\n')
print(f'Это make_order(6) для {cell3.num = }\n{cell3.make_order(6)}\n')
print(f'Это make_order(2) для {cell4.num = }\n{cell4.make_order(2)}\n')
