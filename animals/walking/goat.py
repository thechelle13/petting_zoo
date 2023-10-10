from datetime import date

# from animals import Animal

class Goat:

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

jess = Goat("Jess", "goat", "midday", "grass")
print(f'{jess.name} the {jess.species} is available to pet during the {jess.shift} shift.')



    