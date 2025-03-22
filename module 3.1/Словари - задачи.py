def char_frequency(s: str) -> dict:
    """
    Функция создаёт словарь, где ключами являются символы строки,
    а значениями — количество раз, когда каждый символ встречается в строке.

    """
    res_dict = dict()
    for i in s:
        if i not in res_dict:
            res_dict[i] = 1
        else:
            res_dict[i] += 1
    return res_dict

# print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Функция принимает два словаря и объединяет их в один.
    Если в обоих словарях есть одинаковые ключи, суммируйте их значения (значения только числа)."""
    res_dict = dict1.copy()
    for key, value in dict2.items():
        if key in res_dict:
            res_dict[key] += value
        else:
            res_dict[key] = value
    return res_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
# print(merge_dicts(dict1, dict2))  # {"a": 1, "b": 5, "c": 4}


def dict_to_lists(my_dict: dict) -> tuple:
    """Функция принимает словарь и возвращает два списка:
        один с ключами и другой с соответствующими значениями."""
    keys = [i for i in my_dict.keys()]
    values = [i for i in my_dict.values()]
    return keys, values

my_dict = {"a": 1, "b": 2, "c": 3}
# print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])


def group_by_first_letter(strings: list) -> dict:
    """Функция принимает словарь и список ключей. Функция должна вернуть новый словарь,
        включающий только те пары, ключи которых содержатся в списке."""
    res_dict = dict()
    for i in strings:
        if i[0] not in res_dict:
            res_dict[i[0]] = [i]
        else:
            res_dict[i[0]].append(i)
    return res_dict

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
# print(group_by_first_letter(strings))
# {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}


def extract_subdict(my_dict: dict, keys: list) -> dict:
    """Функция принимает словарь и список ключей.
    Функция должна вернуть новый словарь, включающий только те пары, ключи которых содержатся в списке."""
    res_dict = my_dict.copy()
    for key in my_dict.keys():
        if key not in keys:
            del res_dict[key]
    return res_dict

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
# print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}