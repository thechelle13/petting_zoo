from datetime import date

class Bass:

    def __init__(self
                 
                 ):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True

miss_bassy = Bass()

miss_bassy.name = "Miss Bassy"
miss_bassy.species = "domestic bass"