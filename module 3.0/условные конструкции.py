def check_grade(score: int) -> str:
    """
    Функция check_grade(score), которая принимает оценку и возвращает текстовое описание:
    :param score: оценка пользователя
    :return: перевод оценки в результат
    """
    if 90 <= score <= 100:
        return f'Оценка за {score} баллов: Отлично.'
    elif 75 <= score <= 89:
        return f'Оценка за {score} баллов: Хорошо.'
    elif 50 <= score <= 74:
        return f'Оценка за {score} баллов: Удовлетворительно.'
    elif 0 <= score <= 49:
        return f'Оценка за {score} баллов: Неудовлетворительно.'
    else:
        return 'Некорректное значение! Повторите попытку'

# print(check_grade(16))


def is_even(number: int) -> str:
    """
    Функция определяет "чётное" или "нечётное" входное число
    :param number: входное число
    :return: строка "чётное" или "нечётное"
    """

    return f'Число {number} является чётным' if number % 2 == 0 else f'Число {number} является нечётным.'

# print(is_even(3))


def find_max(a: int, b: int) -> str:
    """
    :param a: число 1
    :param b: число 2
    :return: возвращает большее из входящих чисел
    """
    if a > b:
        return f'Максимальное из чисел {a} и {b}: {a}.'
    elif a < b:
        return f'Максимальное из чисел {a} и {b}: {b}.'
    else:
        return f'число {a} = числу {b}.'

# print(find_max(99, 99))


def check_number(number: int) -> str:
    """
    :param number: число
    :return: в ответе возвращается число после проверки является ли число положительным.
    Если число положительное, проверьте, является ли оно чётным.
    """
    if number > 0:
        if number % 2 == 0:
            return f'Число {number} положительное и чётное.'
        else:
            return f'Число {number} положительное, но не чётное.'
    elif number < 0:
        return f'Число {number} отрицательное.'
    else:
        return f'Число {number} равно нулю.'

# print(check_number(23))

def check_string_length(string: str, length: int) -> str:
    """
    :param string: строка
    :param length: число
    :return: Если длина строки больше указанного числа, выведите "Длина строки достаточная",
     иначе – "Строка слишком короткая"
    """
    if len(string) > length:
        return f'Длина строки {string} достаточная.'
    else:
        return f'Строка {string} слишком короткая.'

# print(check_string_length('HI', 1))