def remove_duplicates(lst: list) -> list:
    """Удаляет все повторяющиеся элементы из списка, оставляя только уникальные значения."""
    res = list()
    for i in lst:
        if not i in res:
            res.append(i)
    return res

# print(remove_duplicates([1, 2, 2, 3, 4, 4]))


def generate_squares(n: int) -> list:
    """Функция генерирует список квадратов чисел от 1 до n"""
    return [i**2 for i in range(1, n+1)]

# print(generate_squares(5))


def merge_lists(list1: list, list2:list) -> list:
    """Функция объединяет два списка, удаляя дубликаты."""
    res = set(list1 + list2)
    return list(res)

# print(merge_lists([1, 2, 3], [3, 4, 5]))


def is_sorted(lst: list) -> bool:
    """Функция проверяет, отсортирован ли список"""
    srtd_list = sorted(lst)
    return lst == srtd_list

# print(is_sorted([1, 2, 3, 4, 5]))  # True
# print(is_sorted([1, 3, 2, 4, 5]))  # False


def merge_lists(list1: list, list2: list) -> (list, str):
    """Функция принимает два списка одинаковой длины и возвращает новый список, где элементы получены путём сложения соответствующих элементов из обоих списков."""
    if len(list1) == len(list2):
        return [list1[i] + list2[i] for i in range(len(list1))]
    else:
        return 'Ошибка! Разная длина списков.'

print(merge_lists([1, 2, 3], [4, 5, 6]))