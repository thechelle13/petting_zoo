from datetime import date

from animals import Animal

class Goat(Animal):

    def __init__(self, name, species, date_added, walking, shift):
        super().__init__(name, species)
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

# miss_fainty = Goat()

# miss_fainty.name = "Miss Fainty"
# miss_fainty.species = "domestic goat"