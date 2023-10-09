from datetime import date

class Ratsnake:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True

miss_ratty = Ratsnake()

miss_ratty.name = "Miss Ratty"
miss_ratty.species = "rat snake"
