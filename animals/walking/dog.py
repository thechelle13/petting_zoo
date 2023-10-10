from datetime import date
from animals import Animal

class Dog(Animal):

    def __init__(self, name, species, date_added, walking, shift):
        super().__init__(name, species)
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

# miss_barky = Dog()

# miss_barky.name = "Miss Barky"
# miss_barky.species = "domestic dog"