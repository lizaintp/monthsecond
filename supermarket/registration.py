def registration(self, name, age):  
    self.name = name
    self.age = age

def emae(self):
    print("Регистрация")
    print("Окройте свой личный кабинет")
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    print(f"Игрок {name} здравствуй")
    print(f"Регистрация прошла успешно!!!")
    self.registration(name, age)
