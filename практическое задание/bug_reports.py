"""
### **6. Коллекции данных**
**Цель:**
Научиться работать со списками: добавлять, удалять и сортировать элементы.
**Задание:**
1. Создайте список из 5 баг-репортов с разными приоритетами:
    - `"Ошибка 1 — High"`.
    - `"Ошибка 2 — Low"`.
    - И так далее.
2. Реализуйте следующие функции:
    - Добавление нового бага.
    - Удаление бага с низким приоритетом.
    - Сортировка багов по приоритету.
**Результат:**
Программа `bug_reports.py`, которая:
- Работает со списком багов.
- Реализует добавление, удаление и сортировку.
"""

bugs = ['Ошибка 1 — Critical', 'Ошибка 2 — Low', 'Ошибка 3 — Critical', 'Ошибка 4 — Low', 'Ошибка 5 — Critical']
priority = ['Critical', 'Low']

def add_bug():
    """функция для добавления нового бага"""
    a = input('Введите номер бага и приоритет в формате: <Ошибка * — *приоритет>.\nВарианты приоритета: Low, Critical\nПример: Ошибка 6 — Critical\n')
    if a.split()[-1] in priority:
        bugs.append(a)
        print('Баг добавлен!')
        return bugs
    else:
        return 'Ошибка! Неверное значение priority. Баг не добавлен'

def remove_low_priority_bug(bug_list):
    """функция для удаления багов с низким приоритетом"""
    for bug in bug_list:
        if "Low" in bug:
            bug_list.remove(bug)
            print(f"Баг '{bug}' удален.")
    return bug_list


def sort_by_priority(bug_list, flag=True):
    """
    сортировка багов по приоритету
    если flag=True: от низкого к большему
    иначе от большего к низкому
    по умолчанию: всегда True
    """
    list_low_prior = []
    list_crit_prior = []
    for i in bug_list:
        j = i.split('—')
        if j[-1].strip() == 'Low':
            list_low_prior.append(i)
        else:
            list_crit_prior.append(i)
    if flag is True:
        list_low_prior.extend(list_crit_prior)
        return list_low_prior
    else:
        list_crit_prior.extend(list_low_prior)
        return list_crit_prior

print(add_bug())
print(sort_by_priority(bugs))
print(sort_by_priority(bugs, flag=False))
print(remove_low_priority_bug(bugs))
