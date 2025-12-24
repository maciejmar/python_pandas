from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,name):
       self.name = name
       
    @abstractmethod   
    def voice(self, sound_type):
        return f"name is {self.sound_type}"
    
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        
    def voice(self,sound_type):
        return f"\ncar voice is {sound_type}"
    def __str__(self):
        return f"the car is {self.name}"
car_1 = Car("toyota")
print(f"car {car_1.name}  {car_1.voice("wrr...")}")