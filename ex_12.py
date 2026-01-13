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
    typ = data_flush["type"]
    if typ == "dog":
        return Pies(data_flush["name"], data_flush["size"],data_flush["serving"])
    if typ == "cat":
        return Cat(data_flush["name"],data_flush["size"],data_flush["trick"])
items = [
    {"type": "dog", "name": "Burek", "size": 8.6, "serving": "aport"},
    {"type": "cat", "name": "Nightwalk", "size": 4.0, "trick":"likes_petting"},
]
flockofanimals = [makeZwierze(x) for x in items]
pies_1 = Pies("burek",18,"aport")
kot_1 = Cat("mruczek",10,"ble")
print(pies_1)
print(kot_1)
for x in flockofanimals:
  print(x)