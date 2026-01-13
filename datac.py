from dataclasses import dataclass

@dataclass
class Zwierze:
    name: str
    size: float
    
    def sound (self,name) -> str:
        sounds =""
        return f"zwierze {name} sounds like this: {sounds}"
    
@dataclass
class Pies(Zwierze):
    serve = "aport"
    def sound (self, name) -> str:
        return f"dog {name} sounds like wrrrr"
    
    
    
    