from datetime import date

class Frog:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True

miss_froggy = Frog()

miss_froggy.name = "Miss Froggy"
miss_froggy.species = "domestic frog"