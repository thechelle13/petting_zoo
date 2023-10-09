from datetime import date

class Cottonmouth:

    def __init__(self
                 
                 ):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True
        

miss_cotton = Cottonmouth()

miss_cotton.name = "Miss Cotton"
miss_cotton.species = "domestic cottonmouth"


# <__main__.Cottonmouth object at 0x7f829fdccdf0>
print(miss_cotton)