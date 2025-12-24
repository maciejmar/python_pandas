from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name)->None:
        self.name = name
    @abstractmethod
    def sound():
        pass

class Animalic:
    def __init__(self, name:str)->None:
        self.name = name
    def sound(self)->str:
        return "cisza"
        
class Dog(Animalic):
    def __init__(self, name:str, size:int)->None:
        super().__init__(name) 
        self.size = size
    def sound(self):
        return f"wrr, wrr..."
    def __str__(self):
        return  f"dog's {self.name} and it sound is: \n {self.sound()}"
    
dog1 = Dog("border",10)
print(dog1)