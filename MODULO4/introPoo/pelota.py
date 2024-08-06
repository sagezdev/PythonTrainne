from dataclasses import dataclass

class Pelota():
    def __init__(self, iterable):
        self.item_list = []
        self.__update(iterable)
    
    def asigna_color(self,new_color:str):
        self.color = new_color
    
    
        
@dataclass
class Trabajador:
    name:str
    age: int
    salary: int
    
sagez = Trabajador('Nacho',23,1000)
print(sagez.name)
