import sqlite3

connect = sqlite3.connect("Coins.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               fullname VARCHAR (100) NOT NULL,
               age INTEGER NOT NULL,
               email TEXT NOT NULL,
               mentor_which_month INTEGER,
               which_month INTEGER,
               coins INTEGER DEFAULT 0
);
               """)

class GeeksMentors:
    def __init__(self):
        self.fullname = None
        self.age = 0
        self.email = None
        mentor_which_month = 0
        self.coins = 0
        self.which_month = 0

    def register(self, fullname, age, email, which_month, mentor_which_month):
        self.fullname = fullname
        self.age = age
        self.email = email
        self.which_month = which_month
        self.mentor_which_month = mentor_which_month
        cursor.execute(f"""
INSERT INTO mentors (fullname, age, email, coins, which_month, mentor_which_month)
                       VALUES ('{fullname}', '{age}', '{email}', 0, {which_month}, '{mentor_which_month}');""")
        connect.commit()

    def plus_coins(self, amount, mentor_name):
        cursor.execute(F"UPDATE mentors SET coins = coins + {amount} WHERE fullname = '{mentor_name}' ")
        connect.commit()
        self.coins += amount

    def minus_coins(self, amount, mentor_name):
        cursor.execute(F"UPDATE mentors SET coins = coins - {amount} WHERE fullname = '{mentor_name}' ")
        connect.commit()
        self.coins -= amount

    def main(self):
        while True:
            print("Выберите команду: ")
            print("1-Добавить ментора, 2-Добавление коинов, 3-Отнять коин")
            command = int(input("Введите цифру: "))
            if command ==1:
                fullname = input("Введите имя ментора: ")
                age = int(input("Введите возраст ментора: "))
                email = input("Введите email ментора: ")
                which_month = int(input("Введите в каком месяце учится ментор: "))
                mentor_which_month = int(input("Введите месяц ментора: "))
                self.register(fullname, age, email, which_month, mentor_which_month)

            elif command == 2:
                mentor_name = input("Введите имя ментора: ")
                if mentor_name:
                    amount = int(input("Введите кол-во коинов: "))
                else:
                    print("Такого ментора нет")
                self.plus_coins(amount, mentor_name)

            elif command == 3:
                mentor_name = input("Введите имя ментора: ")
                amount = int(input("Введите кол-во коинов: "))
                self.minus_coins(amount, mentor_name)
            else:
                print("Такой команды нет")

mentor_1 = GeeksMentors()
mentor_1.main()