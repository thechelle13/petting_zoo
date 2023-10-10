from datetime import date
from animals import Animal

class Dog(Animal):

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food
        self.shift = shift

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

# miss_barky = Dog()

# miss_barky.name = "Miss Barky"
# miss_barky.species = "domestic dog"