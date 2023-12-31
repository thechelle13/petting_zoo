# from datetime import date
from movements import Walking
from animals import Animal

# Designate Llama as a child class by adding (Animal) after the class name
class Llama(Animal, Walking):
  
   def __init__(self, name, species, shift, food, chip_num):
     Animal.__init__(self, name, species, food, chip_num)
     Walking.__init__(self)
     self.shift = shift
  

#     # Remove redundant properties from Llama's initialization, and set their values via Animal
#     def __init__(self, name, species, shift, food, chip_num):
#         super().__init__(name, species, food, chip_num)
#         self.shift = shift # stays on Llama because not all animals have shifts
#         self.walking = True

#     def feed(self):
#       print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
      
#     def __str__(self):
#         return f"{self.name} is a {self.species}"
    
# roberto = Llama("Roberto", "llama", "midday", "grass", 1)
# print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
