from datetime import date

from animals import Animal

class Goat(Animal):

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food
        self.shift = shift

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

# miss_fainty = Goat()

# miss_fainty.name = "Miss Fainty"
# miss_fainty.species = "domestic goat"



    