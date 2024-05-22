class Computer:
    def __init__(self,name, cpu, memory):
        self.name = name
        self.__cpu = cpu
        self.__memory = memory
    
    @property
    def cpu(self):
        return self.__cpu
    
    @property
    def memory(self):
        return self.__memory
    

    def __make_computations(self):
        print(f""" Результат сложения: {self.cpu+self.memory},\nРезультат вычитания: {self.cpu-self.memory},\nРезультат умножения: {self.cpu*self.memory},\nРезультат деления: {self.cpu/self.memory}""")
        

    @property
    def make_computions(self):
        return self.__make_computations



 
acer = Computer("acer aspire 5", 4500, 8)
acer.make_computions()

class Laptop(Computer):
    def __init__(self, name, cpu, memory, memory_card):
        Computer.__init__(self, name, cpu, memory)
        self.__memory_card = memory_card
    @property
    def memory_card(self):
        return self.__memory_card
    
    def info(self):
        print(f"Процессор: {self.cpu}, память: {self.memory}, карта памяти: {self.memory_card}")
    
acer_2 = Laptop("acer3", 1235, 4, 755)
acer_2.make_computions()
acer_2.info()
print(acer_2.name)
print(acer.cpu)


