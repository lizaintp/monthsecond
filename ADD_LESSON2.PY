#ООП помогает ускорить процесс кода и делает его более читаемым

#1

import sqlite3

connect = sqlite3.connect("person.db")
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS a (
               id INTEGER PRIMARY KEY,
               name VARCHAR (100) NOT NULL,
               surname VARCHAR (100) NOT NULL,
               age INTEGER NOT NULL 
);""")

class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self._surname = surname
        self.age = age
        cursor.execute("""INSERT INTO a (name, surname, age) VALUES (?,?,?);""", (self.name, self._surname, self.age))
        connect.commit()

    @property
    def name(self):
        return self.__name
    
    def info(self):
        print(f"Имя - {self.name}, фамилия - {self._surname}, возраст - {self.age}")
    cursor.execute
    connect.commit()

aslan = Person("Aslan", "Baibalaev", 15)
aslan.info()
hogi = Person("Hogi", "Tahirov", 17)
hogi.info()
nurai = Person("Nurai", "Temirbaeva", 16)
nurai.info()


#2
class Math:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        new_num = self.num+other.num 
        return Math(new_num)
    
    def __sub__(self, other):
        new_num = self.num-other.num
        return Math(new_num)

num = Math(2)
print(192+292)
print(3939-2939)

#3
class Constructor:
    def __init__(self,floor):
        self.floor = floor
        self.floor2 = 0
    def build(self):
        for a in  range(self.floor):
            self.floor2 += 1
            print(f"{self.floor2} этаж - дом закончен!")
    def str(self):
        print("Ваш дом достроен!")
      
hom = Constructor(10)
hom.build()
hom.str()

