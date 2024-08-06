#POO
class Persona:
    def __init__(self, firstname,lastanme,age,country,city):
        self.firstname = firstname
        self.lastname = lastanme
        self.age = age
        self.country = country
        self.city = city
        self.skills = []    
    def Person_info(self):
        return f'Hola me llamo {self.firstname} {self.lastname} tengo {self.age} años , Soy de {self.city} de {self.country}'
    def Add_Skill_Person(self,skill):
        self.skills.append(skill)
    def Delete_Skill_Person(self,skill,d):
        print(self,skill,d)
                
nacho = Persona('Ignacio','Muñoz',23,'Chile','Santiago')
print(nacho.Person_info())        
nacho.Add_Skill_Person('Js')
nacho.Add_Skill_Person('Css')
nacho.Add_Skill_Person('HTML')
print(nacho.skills)

print(nacho.Delete_Skill_Person('Js',2))
print(nacho.skills)
        