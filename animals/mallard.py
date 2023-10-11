# from datetime import date

from animals import Animal
from movements import Walking, Swimming

class Mallard:

    def __init__(self, name, species, food):
      Animal.__init__(self, name, species, food)
      
        # self.name = name
        # self.species = species
        # self.date_added = date.today()
        # self.swimming = True
        # self.food = food