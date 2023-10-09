from datetime import date

class Kingsnake:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True

miss_king = Kingsnake()

miss_king.name = "Miss King"
miss_king.species = "domestic kingsnake"