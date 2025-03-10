'''
### **7. Изменяемые и неизменяемые типы данных**
**Цель:**
Понять различия между изменяемыми и неизменяемыми типами данных.
**Задание:**
1. Создайте словарь с информацией о баге:
    - ID.
    - Название.
    - Статус.
2. Измените статус баг-репорта.
3. Напишите текстовое объяснение о неизменяемых типах данных (например, `str`, `int`, `tuple`) в отдельном файле `data_types.txt`.
**Результат:**
- Программа `bug_details.py`, которая работает со словарем.
- Файл `data_types.txt` с объяснением неизменяемых типов данных.
'''

bug_info = {
    'id': 1,
    'name': 'strange',
    'status': 'retest'
}

bug_info['status'] = 'done'

print(bug_info)