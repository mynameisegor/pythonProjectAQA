'''
Модуль практическое задание
Задание 3. Основы
docs: https://seniorqadenis.notion.site/4-0-Fullstack-Python-1628d6cd33d0804d9624e88da4f831bc#1628d6cd33d08080b8c9e9aa70ed5304
Напишите программу, которая:
1. Запрашивает имя пользователя и профессию.
2. Спрашивает, сколько лет пользователь работает в QA.
3. Проверяет, знает ли пользователь, что такое переменная (вопрос: "Что такое переменная?").
4. Выводит разные ответы в зависимости от правильности ответа.
'''

name = input('Введите ваше имя:')
job = input('Введите ваше профессию:')
exp = input('Введите кол-во опыта в QA:')
ask = input('Что такое переменная?')

if ask.lower() == 'ссылка на объект в памяти':
    print('Ответ корректный')
else:
    print('Не верно. Попробуй еще раз')