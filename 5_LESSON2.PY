# class A:
#     def __init__(self):
#         print("a")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("b")

# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("c")

# class D(B,C):
#     def __init__(self):
#         super().__init__()
#         print("d")

# jg = D()

"""Кастомные - модули, которые мы создаем сами (lesson1.py)
Встроенный - модули , которые встроены в язык пайтон (time, random, math, date time) мы их импортируем
Внешние - модули, которые нужно скачивать для использование(библиотеки или фреймесы)"""
# import random
# random.choice 

# import time
# # print("код запуститься через 5 секунд")
# # time.sleep(5)
# # print("Hello world")
# start = time.time()
# print(start)
# n = 0
# while 0 < 7:
#     n+=1
# time.sleep(0,1)
# print("Loding...")
# end = time.time(0,5)
# result = end-start
# print(result)

"""pip install скачать
pip uninstall  удалить
pip freeze проверить наличие"""

#pip - пакетный менеджер нужен для работы с фриворками и ......

from termcolor import cprint
print("Hello world")
cprint("Hello world", "red", "on_yellow")

