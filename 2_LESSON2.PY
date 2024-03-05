#Основные принципы ООП - Объектно Ориентированное Програмирование
#наследование второе по легкости , есть два вида
#абстракция самое легкое
#инкапсуляция 
#полиморфизм  возможность выполнять одного и того же метода в разных классах

class Person:
    def __init__(self,name,age,eyes ):
        self.name = name
        self.age = age
        self.eyes = eyes
    def info(self):
        print(f"{self.name},{self.age},{self.eyes}")
    def run(self):
        print("{self.name} -бежит")
        
human_1 = Person("Eliza", 16, "brown")    
print(human_1.name)
human_1.info()
human_2 = Person("Luntik", 9, "purple")
print(human_2.age)

human_3 = Person("Aslan", 15, "brown")
print(human_3.eyes)

class Parents(Person):
    def __init__(self, name, age, eyes, child):
        super().__init__(name, age, eyes)
        self.child = child

    def info(self):
        print(f"{self.name},{self.age},{self.eyes},{self.child}")
    def info(self):
        print(f"Родитель - {self.name} присматривает за {self.child} детьми")
parent_1 = Parents("Stif-Father", 67, "blue", 2)
# print(parent_1.child)
parent_1.info()
parent_1.run()


class Transport:# Абстрактный класс
    def __init__(self, model, year, color):
        self.model = model # Атрибут\поле\свойства объекта
        self.year = year
        self.color = color

    def info(self):
        print(f"модель - {self.model}, \nгод выпуска - {self.year}, \nцвет - {self.color}, \nмашина зведена? {self.is_start}")

    def broken(self):
        print("Машина сломалась")

    def stop(self):
        print("Транспорт не движется")


