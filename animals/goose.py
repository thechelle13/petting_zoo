from animals import Animal
from movements import Walking

class Goose(Animal, Walking):
    
    def __init__(self, name, species, shift, food, chip_num):
      Animal.__init__(self, name, species, food, chip_num)
      Walking.__init__(self)
      self.shift = shift
    
    # def __init__(self, name, species, date_added ) -> None:
    #     self.name = name
    #     self.species = species
    #     self.date_added = date.today()
    #     self.food = food