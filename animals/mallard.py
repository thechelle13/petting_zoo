# from datetime import date

from animals import Animal
from movements import Swimming

class Mallard(Animal, Swimming):

    def __init__(self, name, species, food, chip_num):
      Animal.__init__(self, name, species, food, chip_num)
      Swimming.__init__(self)
      
        # self.name = name
        # self.species = species
        # self.date_added = date.today()
        # self.swimming = True
        # self.food = food