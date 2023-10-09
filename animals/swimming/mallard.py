from datetime import date

class Mallard:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True

miss_quacky = Mallard()

miss_quacky.name = "Miss Quacky"
miss_quacky.species = "domestic duck"