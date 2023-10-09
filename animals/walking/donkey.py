from datetime import date
class Donkey:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

miss_kickie = Donkey()

miss_kickie.name = "Miss Kickie"
miss_kickie.species = "domestic donkey"