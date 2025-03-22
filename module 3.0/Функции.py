def rectangle_area(a, b):
    """
    Задача 1: Вычисление площади прямоугольника
    """
    res = a * b
    return f'Площадь прямоугольника с длиной {a} и шириной {b} равна {res}'

# print(rectangle_area(5, 6))


def convert_seconds(sec):
    """
     Задача 2: Перевод из секунд в часы и минуты
    :param sec:
    :return:
    """
    hours = sec // 3600
    mins =  (sec % 3600) // 60
    return f'В {sec} секундах содержится {hours} час(ов) и {mins} минут(ы)'

# print(convert_seconds(3671))

def power_of(number, exponent=2):
    """
    Задача 3: Функция с аргументом по умолчанию
    """
    res = number ** exponent
    return f'Число {number} в степени {exponent} равно {res}.'

# print(power_of(9, 8))
# print(power_of(3))

def count_items(*args):
    """
    Задача 4: Подсчёт элементов
    """
    return f'Количество переданных элементов: {len(args)}'

# print(count_items(1, 2, 3, 4, 5))



