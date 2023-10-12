from datetime import date
from movements import Walking
from animals import Animal

class Dog(Animal, Walking):
  
  def __init__(self, name, species, shift, food, chip_num):
      Animal.__init__(self, name, species, food, chip_num)
      Walking.__init__(self)
      self.shift = shift

    # def __init__(self, name, species, shift, food, chip_num):
    #     self.name = name
    #     self.species = species
    #     self.date_added = date.today()
    #     self.walking = True
    #     self.food = food
    #     self.shift = shift

    # def feed(self):
    #   print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
      
    # def __str__(self):
    #     return f"{self.name} is a {self.species}"

# miss_barky = Dog()

# miss_barky.name = "Miss Barky"
# miss_barky.species = "domestic dog"