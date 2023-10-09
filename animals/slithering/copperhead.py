from datetime import date

class Copperhead:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True
        

miss_bitie = Copperhead()

miss_bitie.name = "Miss Bitie"
miss_bitie.species = "domestic copperhead"