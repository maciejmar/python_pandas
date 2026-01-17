class Thing:
    def __init__(self, name, size): #Init has self and the atributes
        self.name = name #atributes defs
        self.size = size
    def __str__(self):#methods do not need atributes as params as they are mentioned in __init__
        return f"The thing has name {self.name} and size {self.size}"

class Circle(Thing):
    def __init__(self, name, size, range):
        super().__init__(name, size) #super without self
        self.range = range
    def __str__(self):
        return f"and here is the {self.name} the range {self.range}"
        
thing = Thing("żelazny","5")
circle = Circle("cyrkiel", 10.2,3)

print ( f"thing - {thing} and circle - {circle}" )