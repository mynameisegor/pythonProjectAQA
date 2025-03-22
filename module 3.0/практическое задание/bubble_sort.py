"""
### **7. Сортировка чисел**
**Цель:**
Научиться реализовывать простые алгоритмы сортировки.
**Задание:**
Напишите программу, которая:
1. Запрашивает у пользователя список чисел через запятую.
2. Реализует функцию `bubble_sort(numbers)`, которая сортирует список чисел методом пузырька.
3. Выводит отсортированный список.
"""

def buble_sort(numbers):
    lst = [int(i) for i in numbers.split(',')]
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

numbers = input('Введите числа через запятую: ')
print(buble_sort(numbers))
