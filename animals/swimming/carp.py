from datetime import date

class Carp:

    def __init__(self
                 
                 ):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True
        

miss_carp = Carp()

miss_carp.name = "Miss Carp"
miss_carp.species = "domestic carp"