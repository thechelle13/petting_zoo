from datetime import date

class Beetle:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True

miss_buggy = Beetle()

miss_buggy.name = "Miss Froggy"
miss_buggy.species = "domestic beetle"