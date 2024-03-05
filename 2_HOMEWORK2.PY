#1
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
#2
    def info(self):
        print(self.fullname, self.age, self.is_married)
    def info(self):
        print(f"Здравствуйте меня зовут {self.fullname}, мне {self.age}  и я {self.is_married}")
people_1 = Person("Emil", 15, "не женат")
people_1.info()
people_2 = Person("Ernis", 46, "я женат")
people_2.info()
#3
class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 0

    def info(self):
        print(f"Здравствуйте меня зовут {self.fullname}, мне {self.age}  я {self.is_married}, а мой опыт работы {self.experience} лет")

    def calculate_salary(self):
        for i in range(self.experience):
            self.salary += 3000
        print(f"Зарплата: {self.salary}")
    def introduce_myself(self):
        
        print(f"Опыт работы: {self.experience} лет")
        # print(f"Зарплата {self.salary}")
        
worker = Teacher("Жаркынай Калмаматовна", 39, "замужем", 15 )
worker.info()
worker.calculate_salary()
worker.introduce_myself()

