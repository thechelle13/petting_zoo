from datetime import date

# from animals import Animal


class Cat:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food
        self.shift = shift

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
      
    def __str__(self):
        return f"{self.name} is a {self.species}"

emma = Cat("Emma", "cat", "midday", "tuna")
print(f'{emma.name} the {emma.species} is available to pet during the {emma.shift} shift. {emma.name} enjoys {emma.food}.')
print(emma.feed())