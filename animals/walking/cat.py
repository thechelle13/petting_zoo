from datetime import date

from animals import Animal


class Cat(Animal):

    def __init__(self, name, species, shift):
        super().__init__(name, species, shift)
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        # self.date_added = date.today()
        self.walking = True
        self.shift = shift

# miss_purr = Cat()

# miss_purr.name = "Miss Purr"
# miss_purr.species = "domestic cat"