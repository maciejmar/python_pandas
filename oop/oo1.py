from enum import Enum

class Engine (Enum):
    GAS="gas"
    DIESEL="diesel"
    ELECTRIC="electric" 
    
    
    
class Vehicle:
    
    def __init__(self, name:str, lenght:float, engine:Engine)->None:
        self.name=name
        self.lenght=lenght
        self.engine=engine if isinstance(engine,Engine) else Engine(engine)
        
    def sound(self,lasting)->str:
        for i in range(lasting):
            stri = stri+"..."
        return stri
    def __str__(self)->str:
        return f"vehicle {self.name} with engine {self.engine} and size of {self.lenght}"

class Car(Vehicle):
    def __init__(self,name,lenght,engine):
         super().__init__(name,lenght,engine)
         self.name = name
         self.lenght=lenght
         self.engine=engine
    def __str__ (self)->str:
        return f"Car {self.name},{self.engine},{self.lenght}"

veh=Vehicle("fahrrad",2,Engine.ELECTRIC)
car=Car("punto",10,Engine.GAS)
print(car,veh)

     