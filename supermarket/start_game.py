class Burger:
    def __init__(self):
        self.name = None
        self.age = 0
        self.souses = None
        self.fillings = None
        self.cotlet = None

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

    def roll(self):
        print("Берем булочку для бургера")
        user = input("Введите слово Булочка , чтобы получить его: ")
        if user == "Булочка":
            print("У вас есть Булочка")

    def souse(self):
        print("Берем соус для бургера")
        user = input("Выберите один соус: сырный, кетчуп, майонез, кетчунез")
        # user = input("Введите слово Соус , чтобы получить его")
        if user == "сырный":
            print("У вас есть сырный соус")
        if user =="кетчуп":
            print("У вас есть кетчуп")
        if user =="майонез":
            print("У вас есть майонез")
        if user == "кетчунез":
            print("У вас есть кетчунез")
        
    def fellings(self):
        print("Берем начинку для бургера")
        user = input("Выберите начинку: огурец, помидор, лук")
        if user == "огурец":
            print("Огурец добавлен в бургер")
        if user == "помидор":
            print("Помидор добавлен в бургер")
        if user == "лук":
            print("Лук добавлен в бургер")

    def cotlet(self):
        print("Добавим мясо в бургер")
        user = input("Выберите какое мясо вы хотите: куриный, говяжий. Или откажитесь: я не буду мясо")
        if user == "я не буду мясо":
            print("Хорошо мы вам сделаем бургер без мяса")
        if user == "куриный":
            print("Куриная котлета добавлено в ваш бургер ")
        if user == "говяжий":
            print("Говяжая котлета добавлено в ваш бургер")

i = Burger()
i.registration()
i.emae()
# i.roll()
# i.souse()
# i.fillings()
# i.cotlet()