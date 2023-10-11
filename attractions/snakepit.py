from .attraction import Attraction


class Snakepit(Attraction):

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = "Wonder at the variety and sizes of snakes."
        self.animals = list()
