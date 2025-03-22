'''
Модуль 2.2.5
docs: https://seniorpomidorov.skillspace.ru/course/68519/1412641#1
'''

'''Задача 1: добавление элемента в список'''

nums = [1, 2, 3]
nums.append(4)
print(nums)

'''Задача 2: удаление элемента из списка'''

fruits = ['Москва', 'Лондон', 'Париж']
fruits.remove('Лондон')
print(fruits)

'''Задача 3: Доступ к элементу по индексу'''

cites = ['Москва', 'Питер', 'Екатеринбург', 'Новосибирск']
print(cites[2])

'''Задача 4: Доступ к элементу по срезу списка'''

nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums1[3:7])

'''Задача 5: изменение элемента списка'''

colors = ['red', 'green', 'blue']
colors[1] = 'yellow'
print(colors)

'''Задача 6: узнаем длину списка'''

animals = ['cat', 'dog', 'rabbit', 'hamster']
len_list = len(animals)
print(len_list)

'''Задача 7: добавление элемента в словарь'''

student = {
    'name': 'Ivan',
        'age': 20
}
student['grade'] = 'A'
print(student)

'''Задача 8: изменение элемента словаря'''

# словарь берем из задачи 7
student['grade'] = 'B'
print(student)

'''Задача 9: Удаление элемента из словаря'''

student1 = {
    'name': 'Ivan',
    'age': 20,
    'grade': 'A'
}
del student1['grade']
print(student1)

'''Задача 10: Доступ к элементу словаря по ключу'''

student2 = {
    'name': 'Ivan',
    'age': 20,
    'grade': 'A'
}
print(f'Имя студента: {student2["name"]}')

'''Задача 11: Проверка наличия ключа в словаре'''

student3 = {
    'name': 'Ivan',
    'age': 20,
    'grade': 'A'
}
print('ключ grade найден в словаре') if 'grade' in student3 else print('ключ grade не найден в словаре')

'''Задача 12: Изменение элемента во вложенном словаре'''

student_student = {
    'name': 'Ivan',
    'adress':{
        'city': 'Moscow',
        'street': 'Lenina'
    }
}
student_student['adress']['city'] = 'Saint Petersburg'
print(student_student)

'''Задача 13: Изменение элемента списка находящемся словаре'''

students= {
    'name': 'Maria',
    'grades': [75, 82, 90]
}
students['grades'][0] = 85
print(students)

'''Задача 14: Изменение элемента в словаре, находящемся внутри списка'''

sudent_list = [
    {
        'name': 'Ivan',
        'age': 20
    },
    {
        'name': 'Petya',
        'age': 22
    }
]
sudent_list[1]['age'] = 23
print(sudent_list)

'''Задача 15: Проверка наличия элемента и определения длины кортежа'''

colors1 = ('red', 'green', 'blue')
var = 'green'
check = var in colors1
print(f'Наличие {var}: {check}. Длина кортежа: {len(colors1)}')
