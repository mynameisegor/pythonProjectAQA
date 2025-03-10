'''
Задание 4 Переменные.
**Цель:**
Научиться создавать, изменять и использовать переменные в Python.
**Задание:**
1. Создайте переменные для хранения информации:
    - Имя пользователя.
    - Профессия.
    - Любимый инструмент для тестирования.
2. Позвольте пользователю изменить данные через ввод.
3. Добавьте проверку: если пользователь не ввел данные, программа выводит сообщение об ошибке.
'''

name, job, tool = '', '', ''

name = input("Введите вашу имя: ")
if not name:
    print("Вы не указали имя, повторите попытку")
else:
    print(f"Ваше имя: {name}.")

job = input("Введите вашу профессию: ")
if not job:
    print("профессия не указана. Попробуйте снова!")
else:
    print(f"Ваша проффесия: {job}.")

tool = input("Введите ваш любимый инструмент для тестирования: ")
if not tool:
    print("Инструмент не указан. Попробуйте снова!")
else:
    print(f"Ваш любимый инструмент: {tool}. Отличный выбор!")