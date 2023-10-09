from datetime import date

class Goldfish:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True

miss_goldie = Goldfish()

miss_goldie.name = "Miss Goldy"
miss_goldie.species = "domestic goldfish"
