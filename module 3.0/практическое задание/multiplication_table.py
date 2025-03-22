"""
**Цель:**
Научиться использовать циклы для создания структурированных данных.
**Задание:**
Напишите программу, которая выводит таблицу умножения от 1 до 10.
"""

def multiplication_table():
    table = []
    for i in range(1, 11):
        l = []
        table.append(l)
        for j in range(1, 11):
            l.append(i*j)
    return table
# print(multiplication_table())

table = multiplication_table()
for row in table:
    print(" ".join(f"{num}" for num in row))