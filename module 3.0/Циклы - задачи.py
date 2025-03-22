def sum_numbers(n: int) -> str:
    """
    :param n: входной параметр
    :return: возвращается сумма чисел от 1 до n
    """
    res = 0
    for i in range(1, n+1):
        res += i

    return f'Сумма чисел от 1 до {n}: {res}'

# print(sum_numbers(5))


def find_min(numbers: list) -> str:
    """
    :param numbers: список чисел на вход
    :return: минимальное значение из списка
    """
    num = numbers[0]
    for i in numbers:
        if num > i:
            num = i
    return f'Минимальное число в списке {numbers}: {num}'

# print(find_min([3, 1, -4, 1, 5]))

def count_vowels(string: str) -> str:
    """
    :param string:  входная строка, может быть в любом регистре
    :return: возвращает кол-во гласных букв в слове
    """
    check = 'aeiou'
    counter = 0
    for i in string.lower():
        if i in check:
            counter += 1
    return f'Количество гласных в строке "{string}": {counter}'

# print(count_vowels("Hello WOrld"))


def print_diamond(rows: int) -> str:
    """
    :param rows: кол-во рядов в ромбовой фигуре
    :return: ромбовая фигура
    """
    for i in range(1, rows+1):
        print('*'*i)
    for i in range(rows-1, 0, -1):
        print('*'*i)

# print_diamond(4)


def countdown():
    """
    :return: функция выводит обратный отсчет от 10 до 1
    """
    for i in range(10, 0, -1):
        print(i)
    print('Старт!')

# countdown()

def countdown_while():
    """
    :return: функция выводит обратный отсчет от 10 до 1
    """
    counter = 11
    while counter != 1:
        counter -= 1
        print(counter)
    print('Старт!')

# countdown_while()
