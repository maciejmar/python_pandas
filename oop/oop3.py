from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,name):
       self.name = name
       
    @abstractmethod   
    def voice(name):
        return f"name is {name}"
    
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name):
            self.name = name