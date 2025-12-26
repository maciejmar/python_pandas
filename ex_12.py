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
        
pies_1 = Pies("burek",18,"aport")
print(pies_1)