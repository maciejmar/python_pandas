class Zwierze:
    def __init__(self,name:str,size:float):
        
        self.name = name
        self.size = size
        
    def sound (self)->str:
        return "cisza"
    def __str__(self)->str:
       return f"{self.name}"
    
class Pies(Zwierze):
    def __init__(self, name,size,serving:str)->None:
        
        super().__init__(name,size)
        self.serving = serving
        
    def sound(self)->str:
        return("wrrr....")
    def __str__(self)->str:
        return f"the dog {self.name} is sizeOf {self.size} and is serving {self.serving}"
    
class Cat(Zwierze):
    def __init__(self, name, size, trick:str)->None:
        self.trick=trick
        super().__init__(name, size)    
    def sound(self)->str:
        return "miau"
    def __str__(self)->str:
        return f"the cat {self.name} size of {self.size} and knows tricks {self.trick}"
    
def makeZwierze(data_flush:dict)->Zwierze:
    return 
        
pies_1 = Pies("burek",18,"aport")
kot_1 = Cat("mruczek",10,"ble")
print(pies_1)
print(kot_1)