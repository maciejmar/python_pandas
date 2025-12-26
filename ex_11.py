from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name:str)->None:
        self.name = name
    @abstractmethod
    def sound(self)->str:
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
    def sound(self)->str:
        return f"wrr, wrr..."
    def __str__(self):
        return  f"dog's {self.name} and it sound is: \n {self.sound()}"
class Cat(Animalic):
    def __init__(self, name:str, streichelbar:bool=True)->None:
        super().__init__(name)
        self.streichelbar = streichelbar
    def sound(self)->str:
        return f"miau..."
    def __str__(self):
        return f"{self.name} cat sounds like {self.sound()} and likes to stroke:{self.streichelbar}"
dog_1 = Dog("border",10)
cat_1 = Cat("nightwalk", False)
cat_2 = Cat("bubek", True)
print(dog_1)
print(cat_1)
print(cat_2)
flock: list[Animalic] =  [dog_1,cat_1,cat_2]
for f in flock:
    print(f"{f} is in flock")