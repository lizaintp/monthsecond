class Doll:
    def __init__(self, skin, hair_color, height,eyes_color, lip):
        self.skin = skin
        self.hair_color = hair_color
        self.height = height
        self.eyes_color = eyes_color
        self.lip = lip

# class Doll:
#     def __init__(self):
#         self.skin = None
#         self.hair_color = None
#         self.height = 0
#         self.eyes_color = None
#         self.lip = None   
    
    def registration(self, name, age):
        self.name = name
        self.age = age
        name = input("Введите имя: ")
        age = int(input("Введите возраст: "))
        
    def info(self):
        print(f"Цвет кожи - {self.skin}, Цвет солос - {self.hair_color}, Рост - {self.height}, Цвет глаз - {self.eyes_color}, Размер губ - {self.lip}")