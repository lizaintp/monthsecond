#1
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.account_number = 0
        self.age = 0
        self.surname = None
    

    def plus(self, amount):
        self.balance += amount
        print(f"Ваш баланс пополнен на {self.balance} сом .")
        print(f'Ваш баланс {self.balance}')

    def minus(self,amount):
        self.balance -= amount
        print(f"С вашего счета было снято {self.balance} сом")
        print(f'Ваш баланс {self.balance}')

    def acc(self):
        print(f"Номер счета: {self.account_number}")        


    def registr(self):
        self.name = None
        self.surname = None
        self.age = 0 


    def __str__(self):
        return f"Ваш текущий баланс: {self.balance}"
    

    def main(self):
        while True:
            print("Выберите действие : 1 -регистрация, 2 - пополнение , 3 - вывести деньги , 4 - выйти")
            choice = int(input("Выберите действие: "))
            if choice == 1:
                print("Регистрация!")
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                age = int(input("Введите возраст: "))
                self.registr()
            elif choice == 2:
                   print("Пополнение")
                   amount = int(input("Введите сумму: "))
                   self.plus(amount)
            elif choice == 3:    
                    print("Вывести деньги")
                    amount = int(input("Введите сумму: "))
                    self.minus(amount)

            elif choice == 4:
                break
            else:
                print("1 - Регистрация, 2 - Пополнение, 3-Вывести деньги, 4 - выйти ")
                choice = int(input("Выберите действие: "))


    
azamat = BankAccount()
azamat.main()



#допдз

num1 = int(input("Введите  возраст двух человек: "))
num2 = int(input("Введите разницу : "))

age = num1-num2
age2 = age/2
age3 = age2+num2
print(f"Одному {age2}, другому {age3}")
