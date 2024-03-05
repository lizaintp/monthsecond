class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Имя - {self.name}, Почта - {self.email}, телефон - {self.phone}"

class Student(GeeksPeople):
    def __init__(self, name, email, phone, state):
        GeeksPeople.__init__(self, name, email, phone)
        self.state = state

    def info(self):
        print(f"Имя - {self.name}, почта - {self.email}, номер телефона - {self.phone}, состояние - {self.state}")

    def study(self):
        print(f"{self.name} учиться")

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, salary):
        GeeksPeople.__init__(self, name, email, phone)
        self.salary = salary

    def info(self):
        print(f"Имя - {self.name}, почта - {self.email}, номер телефона - {self.phone}, зарплата - {self.salary}")

    def work(self):
        print(f"{self.name} работаeт ")

class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id

    def info(self):
        print(f"Имя - {self.name}, почта - {self.email}, номер телефона - {self.phone}, тдентификатор администратора {self.admin_id}")

    def create_group(self):
        print(f"{self.name} создает новую группу")

class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, state, salary):
        Student.__init__(self, name, email, phone, state)
        Teacher.__init__(self, name, email, phone, salary)

    def info(self):
        print(f"Имя - {self.name}, почта - {self.email}, номер телефона - {self.phone}, состояние - {self.state}, зарплата - {self.salary}")

stu = GeeksPeople("Eliza", "liza@gmail.com", +996706634966)
print(stu)
Aslan = Student("Aslan", "aslan@gmail.com", 898071, "Усталое")
Aslan.info()
Aslan.study()
Abduloh = Student("Abduloh", "abduloh@gmail.com", 40983251, "Усталое")
Abduloh.info()
Abduloh.study()
Syimyk = Teacher("Syimyk", "syimyk@gmail.com", 882506246, 30000)
Syimyk.info()
Syimyk.work()
Nursultan = Teacher("Nursultan", "Nursultan@gmail.com", 137855, 30000)
Nursultan.info()
Nursultan.work()
Kamola = Admin("Kamola", "kamola@gmail.com", 3859689, 2)
Kamola.info()
Kamola.create_group()
Kudbuhon = Mentor("Kudbuhon","kudbuhon@gmail.com", 88415687, "Усталое", 2000)
Kudbuhon.info()
Kudbuhon.study()
Kudbuhon.work()
Nurai = Mentor("Nurai","nurain@gmail.com", 851463, "Усталое", 2000)
Nurai.info()
Nurai.study()
Nurai.work()
