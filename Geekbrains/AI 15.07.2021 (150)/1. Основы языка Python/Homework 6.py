# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

import time


class TrafficLight:
    def __init__(self, colour='red'):
        self.colour = colour
        self.colour_time = {'red': 7, 'yellow': 2, 'green': 10}
        self.colour_list = ['red', 'yellow', 'green']

    def running(self):
        print('Демонстрация завершится после двух прогонов всех цветов')
        x = 1
        while x <= 6:
            print(f'\nТекущий режим {self.out_colour()}')
            for i in reversed(range(self.colour_time.get(self.colour))):
                i += 1
                print(f'Переключение через {i}')
                time.sleep(1)
            try:
                self.colour = self.colour_list[self.colour_list.index(self.colour) + 1]
            except IndexError:
                self.colour = 'red'
            x += 1
        print('Конец демонстрации')

    def set_color_time(self, red_time, yellow_time, green_time):
        self.colour_time['red'] = red_time
        self.colour_time['yellow'] = yellow_time
        self.colour_time['green'] = green_time

    def out_colour(self):
        colour_order = ['red', 'yellow', 'green']
        colour_index = colour_order.index(self.colour)
        if colour_index == 0:
            return f"\033[31m\033[40m{self.colour}\033[0m"
        elif colour_index == 1:
            return f"\033[33m\033[40m{self.colour}\033[0m"
        elif colour_index == 2:
            return f"\033[32m\033[40m{self.colour}\033[0m"


input('ENTER - Начать демонстрацию')
print('\nЗадание 1.')
tl = TrafficLight()  # принимает значение по умолчанию 'red' работает с 'red', 'yellow', 'green'
tl.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def how_much_asphalt(self):
        print(f'Для покрытия всего полотна потребуется {self._length * self._width * 25 * 5 / 1000} тонн асфальта')


time.sleep(2)
print('\nЗадание 2.')
my_road = Road(1000, 20)
my_road.how_much_asphalt()


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(sum(self._income.values()))


time.sleep(2)
print('\nЗадание 3.')
id1 = Position('Борис', 'Козлов', 'Прораб', {"wage": 50000, "bonus": 20000})
id1.get_full_name()
id1.get_total_income()


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, color, name, speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        if self.speed != 0:
            print(f'{self.name} изменяет скрость с {self.speed} км/ч на {speed}')
            self.speed = speed
        else:
            self.speed = speed
            print(f'{self.name} начала движение со скоростью {speed} км/ч!')

    def stop(self):
        if self.speed != 0:
            self.speed = 0
            print(f'{self.name} остановилась!')
        else:
            print(f'{self.name} уже стоит на месте!')

    def turn(self, direction):
        print(f'{self.name} повачаивает {direction}!')

    def show_speed(self):
        print(f'Текущая скорость {self.name} ровна {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):  # 60
        while self.speed > 60:
            print(f'ВНИМАНИЕ! {self.name} превышает допустимую скорость (60 км/ч)!'
                  f'Текущая скорость {self.name} км/ч!')
            self.speed = int(input('Введи новую скорость: '))


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):  # 40
        while self.speed > 40:
            print(f'ВНИМАНИЕ! {self.name} превышает допустимую скорость (40 км/ч)!'
                  f'Текущая скорость {self.name} км/ч!')
            self.speed = int(input('Введи новую скорость: '))


class PoliceCar(Car):
    is_police = True


time.sleep(2)
print('\nЗадание 4.')
car1 = Car('red', 'Car1', 100)
print(f'{car1.__class__.__name__ = }')
print(f'{car1.speed = }')
print(f'{car1.name = }')
print(f'{car1.color = }')
print(f'{car1.is_police = }')
car1.show_speed()
car1.turn('направо')
car1.turn('налево')
car1.stop()
car1.stop()
car1.show_speed()
car1.go(100)
car1.show_speed()
car1.go(120)
car1.show_speed()

print('\n', '*' * 50, '\n')

car2 = TownCar('white', 'Car2', 90)
print(f'{car2.__class__.__name__ = }')
print(f'{car2.speed = }')
print(f'{car2.name = }')
print(f'{car2.color = }')
print(f'{car2.is_police = }')
car2.show_speed()
car2.turn('направо')
car2.turn('налево')
car2.stop()
car2.stop()
car2.show_speed()
car2.go(100)
car2.show_speed()
car2.go(120)
car2.show_speed()

print('\n', '*' * 50, '\n')

car3 = SportCar('white', 'Car3', 180)
print(f'{car3.__class__.__name__ = }')
print(f'{car3.speed = }')
print(f'{car3.name = }')
print(f'{car3.color = }')
print(f'{car3.is_police = }')
car3.show_speed()
car3.turn('направо')
car3.turn('налево')
car3.stop()
car3.stop()
car3.show_speed()
car3.go(100)
car3.show_speed()
car3.go(120)
car3.show_speed()

print('\n', '*' * 50, '\n')

car4 = WorkCar('green', 'Car4', 70)
print(f'{car4.__class__.__name__ = }')
print(f'{car4.speed = }')
print(f'{car4.name = }')
print(f'{car4.color = }')
print(f'{car4.is_police = }')
car4.show_speed()
car4.turn('направо')
car4.turn('налево')
car4.stop()
car4.stop()
car4.show_speed()
car4.go(100)
car4.show_speed()
car4.go(120)
car4.show_speed()

print('\n', '*' * 50, '\n')

car5 = PoliceCar('white', 'Car5', 100, True)
print(f'{car5.__class__.__name__ = }')
print(f'{car5.speed = }')
print(f'{car5.name = }')
print(f'{car5.color = }')
print(f'{car5.is_police = }')
car5.show_speed()
car5.turn('направо')
car5.turn('налево')
car5.stop()
car5.stop()
car5.show_speed()
car5.go(100)
car5.show_speed()
car5.go(120)
car5.show_speed()


# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'unknown'

    def draw(self):
        print(f'Запуск отрисовки при помощи {self.title}.')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка ручкой.')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка карандашом.')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка маркером.')


time.sleep(2)
print('\nЗадание 5.')
unknown = Stationery()
unknown.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
