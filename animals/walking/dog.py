from datetime import date
class Dog:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

miss_barky = Dog()

miss_barky.name = "Miss Barky"
miss_barky.species = "domestic dog"