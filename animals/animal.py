from datetime import date

class Animal:
    def __init__(self, name, species, date_added, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        
    # def __str__(self):
    #     return 
    # "
    #     {self.name}
    #     {self.species}
    #     "
        