#Повторение

# class SmartPhone:
#     def __init__(self, model, battery, sim_cards):
#         self.model = model
#         self._battery = battery
#         self.__sim_cards = sim_cards

#     @property
#     def sim_cards(self):
#         return self.__sim_cards
    
#     # @sim_cards.setter
#     # def sim_cards(self,sim):
#     #     self.sim_cards == sim

#     def info(self):
#         print(f"Модель телефона - {self.model}, батарея - {self._battery}, сим карта - {self.__sim_cards}")
#         self._protection()
#         self.__password
#     def _protection(self):
#         print("Protection info")

    
#     def __password(self):
#         print("123216425")

#     @property
#     def password(self):
#         return self.__password

# phone = SmartPhone("Redmi", 100, "O!")
# phone.info()
# phone._protection()
# print(phone.model)
# print(phone._battery)
# print(phone.sim_cards)
# phone.password()

##  @ - декараторы

# def lux(fund):
#     def cats():
#         print("Hi , спасибо что используете наш декоратор")
#         fund()
#         print("Bye")

#     return cats


# @lux
# def add():
#     print(2+2)
# add()


#########Новая тема
#Магические методы dunder (double underscore) окружены двумя нижними почеркиваниями
"""В Python  мы не вызываем эти методы , они вызываются автоматически"""
from typing import Any


class Food:
    def __init__(self, price, weight):
         self.price = price
         self.weight = weight

    def info(self):
        print(f"цена {self.price},вес {self.weight}")

    def __str__(self): #__str__ ключевое слово - print
        return f"цена {self.price},вес {self.weight} str"
    
    def __call__(self,a ,b):  #ОБРАЩАЕТСЯ КАК К ФУНКЦИИ
        print(a+b)

    def __repr__(self): #__repr__ - print
        return f"цена {self.price},вес {self.weight } repr"
    
    #Магические методы для арифметических действий
    def __add__(self, other):
        new_price = self.price + other.price
        new_weight = self.weight + other.weight
        return Food(new_price, new_weight)
    
    def __sub__(self, other):
        new_price = self.price - other.price
        new_weight = self.weight - other.weight
        return Food(new_price, new_weight)
    
    def __mul__(self, other):
        new_price = self.price * other.price
        new_weight = self.weight * other.weight
        return Food(new_price, new_weight)
    
    def __truediv__(self, other):
        new_price = self.price / other.price
        new_weight = self.weight / other.weight
        return Food(new_price, new_weight)
    
    def __floordiv__(self, other):
        new_price = self.price // other.price
        new_weight = self.weight // other.weight
        return Food(new_price, new_weight)
    
    def __eg__(self, other):
        return self.price == other.price


pizza = Food(400, 500)
hamburger = Food(60, 280)
print(pizza)
pizza(2,8)
print(pizza+hamburger)
print(pizza-hamburger)
print(pizza*hamburger)
print(pizza/hamburger)
print(pizza//hamburger)
food = Food(798, 390) # вызывается __init__ 
print(food.price, food.weight) 
food.info()
print(food) #__str__
food(2,5)  #__call__

print(25%2)





