import sqlite3

connect = sqlite3.connect("bank.db")
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS customs (
               id INTEGER PRIMARY KEY,
               name VARCHAR (100) NOT NULL,
               surname VARCHAR (100) NOT NULL,
               age INTEDER NOT NULL ,
               address TEXT NOT NULL,
               email VARCHAR (100) NOT NULL,
               wallet INTEGER NOT NULL DEFAULT 0

);""")


class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = 0
        self.address = None
        self.email = None
        self.wallet = 0
    
    def register(self, name, surname, age, address, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.email = email
        cursor.execute(f"""
                    INSERT INTO customs (name, surname, age, address, email)
                        VALUES ('{name}', '{surname}', {age} , '{address}', '{email}');""")
        connect.commit()

    def wallett(self, wallet):
        self.wallet = wallet
        cursor.execute(f"Ваш баланс на счету {self.wallet}")
        connect.commit()
    
    def top_up(self, all):
        cursor.execute(f"""UPDATE customs SET wallet = wallet + {all} WHERE name = '{self.name}' """)
        connect.commit()
        self.wallet += all

    def withdraw_money(self, all):
        cursor.execute(f"UPDATE customs SET wallet = wallet - {all} WHERE name = '{self.name}' ")
        connect.commit()
        if self.wallet < all:
            print("Недасточно средств")
        else:
            print(self.wallet)
            self.wallet -= all

    def start(self):
        while True:
            print("Выберите действие!")
            you = int(input("1 - регистрация, 2 - пополнить счет, 3 - снять деньги со счета: "))
            if you == 1:
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                age = int(input("Введите возраст: "))
                address = input("Введите ваш адрес: ")
                email = input("Введите ваш email: ")
                self.register(name, surname, age, address, email)

            elif you == 2:
                name = input("Введите ваше имя: ")
                if name:
                    all = int(input("Введите на сколько хотите пополнить счет: "))
                    print("Пополнено")
                else:
                    print("Такого имени нет")
                self.top_up(all)

            elif you == 3:
                name = input("Введите ваше имя: ")
                all = int(input("Введите сколько денег хотите снять: "))
                if all > self.wallet:
                    print(f"Недостаточно средств ")
                    break
                else:
                    self.withdraw_money(all)
            else:
                print("Такой команды нет")

people = Bank()
people.start()