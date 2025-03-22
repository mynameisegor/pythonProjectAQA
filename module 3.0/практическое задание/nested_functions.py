"""
### **5. Работа с вложенными функциями**
**Цель:**
Освоить концепцию вложенных функций для структурирования кода.
**Задание:**
Напишите программу, которая:
1. Реализует основную функцию `calculator()`, которая:
    - Спрашивает у пользователя два числа.
    - Спрашивает операцию (`+`, , , `/`).
    - Использует вложенные функции для выполнения каждой операции.
2. Возвращает результат выбранной операции.
"""

def calculator():
    num1 = int(input('Введите первое число:'))
    num2 = int(input('Введите второе число:'))
    operation = input('Выберите операцию (+, -, *, /)')

    def add(num1, num2):
        return num1 + num2

    def subtraction(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def division(num1, num2):
        if num2 == 0:
            raise ValueError('Деление на 0 недопустимо!')
        return num1 / num2

    if operation ==  '+':
        result = add(num1, num2)
    elif operation ==  '-':
        result = subtraction(num1, num2)
    elif operation ==  '*':
        result = multiply(num1, num2)
    elif operation ==  '/':
        try:
            result = division(num1, num2)
        except ValueError as e:
            return f'Ошибка: {e}'
    else:
        return "Ошибка: некорректная операция!"

    return f'Результат: {result}'

print(calculator())