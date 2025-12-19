class Vehicle:
    
    def __init__(self, name:str)->None:
        self.name=name
       
        
    def sound(self,lasting)->str:
        for i in range(lasting):
            stri = stri+"..."
        return stri
    def __str__(self)->str:
        return f"vehicle name is {self.name}"

class Car(Vehicle):
    def __init__(self,name):
         super().__init__(name)
         self.name = name
    def __str__ (self)->str:
        return f"Car {self.name}"

veh=Vehicle("fahrrad")
car=Car("punto")
print(f"{car} and {veh}")

     