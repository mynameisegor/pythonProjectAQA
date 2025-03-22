def get_unique_elements(lst: list) -> list:
    """Функция принимает список чисел или строк и возвращает новый список,
    содержащий только уникальные элементы из исходного списка."""
    return list(set(lst))

# print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))  # [1, 2, 3, 4, 5]


def is_unique_list(lst: list) -> bool:
    """Функция принимает список и возвращает True,
    если все элементы списка уникальны, и False, если есть повторения."""
    return lst == list(set(lst))

# print(is_unique_list([1, 2, 3, 4]))  # True
# print(is_unique_list([1, 2, 2, 3]))  # False


def get_unique_vowels(s: str) -> set():
    vowels = 'aeiou'
    res = set(s)
    for i in res.copy():
        if i.lower() not in vowels:
            res.remove(i)
    return res

print(get_unique_vowels("Hello World"))  # {'e', 'o'}