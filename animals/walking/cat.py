from datetime import date
class Cat:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

miss_purr = Cat()

miss_purr.name = "Miss Purr"
miss_purr.species = "domestic cat"