"""
### **3. Циклы**
**Цель:**
Закрепить навыки работы с циклами `for` и `while`.
**Задание:**
Напишите программу, которая:
1. Запрашивает у пользователя число `n`.
2. Выводит все числа от 1 до `n` в одной строке, разделяя их пробелами.
3. Выводит сумму всех чисел от 1 до `n`.
"""

number = int(input('Введите число: '))
def number_for(num):
    str_num = ''
    sum_nums = 0
    for i in range(1, num+1):
        str_num += f'{i} '
        sum_nums += i
    return f'Числа: {str_num.strip()}\nСумма чисел: {sum_nums}'

def number_while(num):
    str_num = []
    sum_nums = 0
    iter = 0
    while len(str_num) != num:
        iter += 1
        str_num.append(str(iter))
        sum_nums += iter

    return f'Числа: {' '.join(str_num)}\nСумма чисел: {sum_nums}'


print(number_for(number))

print(number_while(number))
