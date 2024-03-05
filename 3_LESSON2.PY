# #инкапсуляция защищенный и приватные методы, (защита данных)
# #setter меняет название
# class SmartPhone:
#     def __init__(self, sim_cards, battery):
#         self.__sim_cards = sim_cards
#         self.battery = battery

#     @property #декаратор из приватного в публичный
#     def sim_cards(self):
#         return self.__sim_cards #приватный 
    
#     @sim_cards.setter
#     def sim_cards(self,sim):
#         self.sim_cards == sim
    
    
#     def __info(self):
#         print(f"Ваша сим карта {self.sim_cards}, ваш объем батареи {self.battery} ")

#     @property
#     def info(self):
#         return self.__info
    
# poco = SmartPhone(["O!", "Megacom"], 16)
# poco.info()
    
# class Car:
#     def __init__(self, model, color) :
#         self.model = model
#         self.color = color

#     def info(self):
#         print(f"Бренд машины { self.model}, цвет {self.color}")

# class ElectricCar(Car):
#     def __init__(self, model, year, battery):
#         Car.__init__(self, model, year )
#         self.battery = battery

#     def drive(self):
#         print(f"{self.model} еде на электричестве")

# class FuelCar(Car):
#     def __init__(self, model, color,fuel_back):
#         super().__init__(model, color)
#         self.fuel_back = fuel_back

#     def drive(self):
#         print(f"{self.model} едет на топливе")

# class HybridCar(ElectricCar, FuelCar):
#     def __init__(self, model, year, battery):
#         ElectricCar.__init__(self, model, year, battery)
#         FuelCar.__init__(self, model, year, battery)

#     def drive(self):
#         print(f"{self.model} едет на топливе и на электричестве")

# Tesla = ElectricCar("Tesla Model X", 2020, 193104 )
# Tesla.info()
# Tesla.drive()

# audi = FuelCar("R-R" , 2013, 194141)
# audi.info()
# audi.drive()

# toyota = HybridCar("Avaison", 1929, 12771)
# toyota.info()
# toyota.drive()


class Laptop:
    def __init__(self, model, year,  core, color):
        self.model = model
        self.year = year
        self.core = core
        self.color = color

    
    def info(self):
        print(f"Бренд ноутбука { self.model}, цвет {self.color}")

class Mac(Laptop):
    def __init__(self, model, year, core, color,apple):
        Laptop.__init__(self, model, year, core, color) 
        self.apple = apple

    def info(self):
        print(f"{self.model} ноут с откушенным яблочком")

class Acer(Laptop):
    def __init__(self, model, year, core, color, keyboard):
        Laptop.__init__(self, model, year, core, color)
        self.keyboard = keyboard

    def info(self):
        print(f"{self.model} ноут со светящейся клавиатурой")

class AcMac(Mac, Acer):
    def __init__(self, model, year, core, color, apple, keyboard):
        Mac.__init__(self, model, year, core, color, apple)
        Acer.__init__(self, model, year, core, color, keyboard)

    def info(self):
        print(f"{self.model} это ребенок Mac и Acer")

mac = Mac("Mac", 2019, 19394, "grey", "с откушенным яблоком")
mac.info()

acer = Acer("Acer 3", 2017, 1838, "black", "цветящаяся клавиатура")
acer.info()

acmac = AcMac("AcMac34", 2024, 138495, "blue", "с откушенным яблоком", "цветящаяся клавиатура")
print(acmac.model)
acmac.info()