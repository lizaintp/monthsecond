#1
# class Fruits:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def info(self):
#         print(f"название - {self.name}, \nцвет -  {self.color}, \nмасса - {self.weight}")

# apple = Fruits("apple","red", 242 )
# apple.info()        
# print("apple:" , apple.name)
# banana = Fruits("banana","yellow", 240)
# banana.info()
# print("banana:" , banana.color)
# pear = Fruits("pear","green" , 150)
# pear.info()
# print("banana:" , pear.weight)

#2
# class Car:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.is_start = True
#         self.fuel = 0
#     def info(self):
#         print(f"модель - {self.model}, \nгод выпуска - {self.year}, \nцвет - {self.color}, \nмашина зведена? {self.is_start}")


#     def refuel(self, gaz):
#         self.gaz = gaz
#         self.fuel+=self.gaz
#         print("Бак заполнен")
#         if gaz >= 40:
#             print("За раз можно пополнить только до 40")

    
#     def start(self):
#         self.is_start = True
#         print("Машина завелась")

#     def drive(self, city, distance):
#         if self.is_start == True:
#             print(f"Машина едет в {city}")
#         else:
#             print("Заведите машину")
#         self.distance = distance
#         if self.distance >400 and self.fuel >40:
#             print("На одной заправке можно доехать только 400 км")
#         else:
#             print("Вы заправились")

# bmw = Car("bmw - x7", 2018, "White")
# bmw.info()
# bmw.refuel(40)
# bmw.start()
# bmw.drive("Bishkek",400)
