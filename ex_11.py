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
class Cat(Animalic):
    def __init__(self, name:str, streichelbar:bool)->None:
        super().__init__(name)
    def sound(self):
        return f"miau"
    def _str__(self):
        return "self.name cat sounds like {self.sound()} and likes to stroke:{self.streicheln}"
dog_1 = Dog("border",10)
cat_1 = Cat("nightwalk, 4")
print(dog_1)
print(cat_1)