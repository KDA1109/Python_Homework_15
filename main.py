
import logging
from datetime import datetime
from math import pi, sqrt


class Rectangle:
    def __init__(self, width, height=None):
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Недопустимое значение ширины")
        if height is not None and (not isinstance(height, (int, float)) or height <= 0):
            raise ValueError("Недопустимое значение высоты")
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return float(self.width * self.height)

    def __add__(self, other):
        all_perimetr = self.perimeter() + other.perimeter()
        width = self.width + other.width
        height = int(all_perimetr / 2 - width)
        return Rectangle(width, height)

    def __sub__(self, other):
        new_perimeter = self.perimeter() - other.perimeter()
        if new_perimeter < 0:
            self, other = other, self
            new_perimeter = -new_perimeter
        width = abs(self.width - other.width)
        height = int(abs(new_perimeter / 2 - width))
        return Rectangle(width, height)

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False

    def __le__(self, other):
        if self.area() <= other.area():
            return True
        else:
            return False


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def get_length(self):
        return 2 * pi * self.radius

    def get_square(self):
        return pi * self.radius ** 2


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        return abs((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5)


logging.basicConfig(filename='logs.log.', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('Программа')
logger_1 = logging.getLogger('Прямоугольник')
logger_2 = logging.getLogger('Круг')
logger_3 = logging.getLogger('Треугольник')

name = input("Введите свое имя: ")
logger.info(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} вошел в главное меню программы')


text = '' \
           "Главное меню:\n" \
           "0 - Завершить работу программы\n" \
           "1 - Вычислить периметр прямоугольника\n" \
           "2 - Вычислить площадь прямоугольника\n" \
           "3 - Вычислить длину круга\n" \
           "4 - Вычислить площадь круга\n" \
           "5 - Вычислить периметр треугольника\n" \
           "6 - Вычислить площадь треугольника\n" \
           ""


print(text)


while True:
    comand = input('Введите команду: ')


    if comand == '1':
        logger_1.info(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} начал вычислять периметр Прямоугольника')
        while True:

            width = input("Введите ширину прямоугольника: ")
            if not width.isdigit() or int(width) <= 0:
                print("Недопустимое значение")
                logger_1.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                            f'ввел недопустимое значение ширины прямоугольника')
                continue
            while True:
                height = input("Введите высоту прямоугольника: ")
                if not height.isdigit() or int(height) <= 0:
                    print("Недопустимое значение")
                    logger_1.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                            f'ввел недопустимое значение длины прямоугольника')
                    continue
                break
            rect = Rectangle(int(width), int(height))
            print(f"Периметр прямоугольника равен {rect.perimeter()}")
            logger_1.info(
                f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name}'
                f' вычислил периметр прямоугольника со сторонами {width} и {height}')
            break

    elif comand == '2':
        logger_1.info(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} начал вычислять площадь Прямоугольника')
        while True:

            width = input("Введите ширину прямоугольника: ")
            if not width.isdigit() or int(width) <= 0:
                print("Недопустимое значение")
                logger_1.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                f'ввел недопустимое значение ширины прямоугольника')
                continue
            while True:
                height = input("Введите высоту прямоугольника: ")
                if not height.isdigit() or int(height) <= 0:
                    print("Недопустимое значение")
                    logger_1.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                    f'ввел недопустимое значение длины прямоугольника')
                    continue
                break

            rect = Rectangle(int(width), int(height))
            print(f"Площадь прямоугольника ровна {rect.area()}")
            logger_1.info(
                f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name}'
                f' вычислил площадь прямоугольника со сторонами {width} и {height}')
            break
    elif comand == '3':
        logger_2.info(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} начал вычислять длину Круга')
        while True:

            radius = input("Введите радиус круга: ")
            if not radius.isdigit() or int(radius) <= 0:
                print("Недопустимое значение")
                logger_1.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                f'ввел недопустимое значение радиуса круга')
                continue

            long = Circle(int(radius))
            print(f"Длина круга ровна {long.get_length()}")
            logger_2.info(
                f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name}'
                f' вычислил длину круга с радиусом {radius}')
            break
    elif comand == '4':
        logger_2.info(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} начал вычислять площадь Круга')
        while True:

            radius = input("Введите радиус круга: ")
            if not radius.isdigit() or int(radius) <= 0:
                print("Недопустимое значение")
                logger_1.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                f'ввел недопустимое значение радиуса круга')
                continue

            long = Circle(int(radius))
            print(f"Площадь круга ровна {long.get_square()}")
            logger_2.info(
                f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name}'
                f' вычислил площадь круга с радиусом {radius}')
            break
    elif comand == '5':
        logger_3.info(
            f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} начал вычислять периметр Треугольника')
        while True:

            a = input("Введите длину 1ой стороны: ")
            if not a.isdigit() or int(a) <= 0:
                print("Недопустимое значение")
                logger_3.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                  f'ввел недопустимое значение стороны треугольника')
                continue

            while True:
                b = input("Введите длину 2ой стороны: ")
                if not b.isdigit() or int(b) <= 0:
                    print("Недопустимое значение")
                    logger_3.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                      f'ввел недопустимое значение стороны треугольника')
                    continue


                while True:
                    c = input("Введите длину 3ей стороны: ")
                    if not c.isdigit() or int(c) <= 0:
                        print("Недопустимое значение")
                        logger_3.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                          f'ввел недопустимое значение стороны треугольника')
                        continue
                    break
                if int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(b) + int(c) > int(a):
                    trian = Triangle(int(a), int(b), int(c))
                    print(f"Периметр треугольника равен {trian.perimeter()}")
                    logger_3.info(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                  f'вычислил периметр треугольника со сторонами {a}, {b}, {c}')
                    break
                print('Треугольник невозможен. Сумма двух его сторон должна быть больше третьей')
                logger_3.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name}'
                                  f' ввел значения сторон треугольника {a}, {b}, {c}. '
                                  f'Существование такого треугольника невозможно')
                break

            break


    elif comand == '6':
        logger_3.info(
            f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} начал вычислять площадь Треугольника')
        while True:

            a = input("Введите длину 1ой стороны: ")
            if not a.isdigit() or int(a) <= 0:
                print("Недопустимое значение")
                logger_3.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                  f'ввел недопустимое значение стороны треугольника')
                continue

            while True:
                b = input("Введите длину 2ой стороны: ")
                if not b.isdigit() or int(b) <= 0:
                    print("Недопустимое значение")
                    logger_3.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                      f'ввел недопустимое значение стороны треугольника')
                    continue

                while True:
                    c = input("Введите длину 3ей стороны: ")
                    if not c.isdigit() or int(c) <= 0:
                        print("Недопустимое значение")
                        logger_3.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                          f'ввел недопустимое значение стороны треугольника')
                        continue
                    break
                if int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(b) + int(c) > int(a):
                    trian = Triangle(int(a), int(b), int(c))
                    print(f"Площадь треугольника ровна {trian.square()}")
                    logger_3.info(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} '
                                  f'вычислил площадь треугольника со сторонами {a}, {b}, {c}')
                    break
                print('Треугольник невозможен. Сумма двух его сторон должна быть больше третьей')
                logger_3.critical(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name}'
                                  f' ввел значения сторон треугольника {a}, {b}, {c}. '
                                  f'Существование такого треугольника невозможно')
                break

            break
    elif comand == '0':
        print('Работа программы завершена')
        logger.info(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} завершил работу с программой')
        break
    else:
        print("Недопустимый выбор")
        logger.info(f'{datetime.now().strftime("%H:%M:%S")} Пользователь {name} ввел недопустимое значение в главном меню')
        continue

