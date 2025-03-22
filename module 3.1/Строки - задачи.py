from codecs import replace_errors
from runpy import run_path


def is_anagram(s1: str, s2: str) -> bool:
    """
    # Приводим строки к нижнему регистру и сортируем
    """
    return sorted(s1.lower()) == sorted(s2.lower())

# print(is_anagram('listen', 'silent'))


def is_palindrome(s: str):
    """
    Удаляем все не буквенно-цифровые символы
    """
    new_s = ''.join([c.lower() for c in s if c.isalnum()])
    return new_s == new_s[::-1]

# print(is_palindrome('A man, a plan, a canal: Panama'))


def longest_word(s: str)-> str:
    """
    Возвращает самое длинное слово в строке
    """
    lst = [i for i in s.split() if i.isalnum()]
    longest = ''
    for i in lst:
        if len(i) > len(longest):
            longest = i
    return longest

# print(longest_word('In the middle of a vast desert, an extraordinary adventure awaits")  # "extraordinar'))


def format_phone_number(digits: str)-> str:
    """
    Принимает строку из 10 цифр и возвращает её в формате (XXX) XXX-XXXX
    """
    return '('+ digits[0:3] + ') ' + digits[3:6] + '-' + digits[6:10]


# print(format_phone_number("1234567890"))


def remove_duplicates(s: str) -> str:
    """
    Принимает строку и возвращает без дубликатов
    """
    result = []
    for i in s:
        if i not in result:
            result.append(i)
    return ''.join(result)

print(remove_duplicates('programming'))


def is_unique(s: str) -> bool:
    """
    Проверка строки на уникальность
    """
    check = []
    for i in s:
        if i not in check:
            check.append(i)
    return ''.join(check) == s


# print(is_unique("abcdef"))  # True
# print(is_unique("hello")) # False