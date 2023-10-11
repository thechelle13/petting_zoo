from .attraction import Attraction

class Wetlands(Attraction):

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = "Disappearing every moment, come enjoy and learn about our wetlands."
        self.animals = list()
