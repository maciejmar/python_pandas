from abc import abstractmethod, ABC

class Vehicle(ABC):
    DEFAULT_LASTING = 5
    def __init__(self, name:str)->None:
        self.name=name
       
    @abstractmethod    
    def sound(self,lasting:int | None=None)->str:
        if lasting==None:
            lasting=None
        else:
            stri=""
            for i in range(lasting):
                stri = stri+"...wrr"
        return stri
    
    def __str__(self)->str:
        return f"vehicle name is {self.name}"

class Car(Vehicle):
    DEFAULT_LASTING = 3
    
    def __init__(self,name):
         super().__init__(name)
         self.name = name
    def __str__ (self)->str:
        return f"Car {self.name}"
    def sound(self,lasting:int | None=None)->str:
        stri=""
        if lasting==None:
            lasting = self.DEFAULT_LASTING
        else: 
            for i in range(lasting):
                stri=stri+"wrr..."+"child lasting..." + stri
        return stri


car=Car("punto")
print(f"{car}\nand \ncar1 = {car.sound(3)} \nand car2 = {car.sound(4)}")

     