from datetime import date
class Goat:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

miss_fainty = Goat()

miss_fainty.name = "Miss Fainty"
miss_fainty.species = "domestic goat"