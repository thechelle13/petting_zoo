# import the python datetime module to help us create a timestamp
from datetime import date
from animals import Animal


# import categories swimming, slithering, and walking and then each animal
# from animals.swimmimg import Bass, Carp, Frog, Goldfish, Mallard
# from animals.slithering import Beetle, Copperhead, Cottonmouth, Kingsnake, Ratsnake
from animals.walking import Cat, Dog, Donkey, Goat, Llama
# from attractions import Pettingzoo, Snakepit, wetlands

# class Llama:

#     def __init__(self):
#         # Establish the properties of each animal
#         # with a default value
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
        
# miss_fuzz = Llama()
# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "domestic llama"
# # print(miss_fuzz)
# print(miss_fuzz.name)

# add vscode


# george = Monkey()
# george.name = "George"
# george.species = "Howler Monkey"

# class Pig:

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         self.date_added = date.today()
#         self.walking = True

# wilbur = Pig("Wilbur", "pot-bellied pig")

# print(wilbur.name, wilbur.species)

roberto = Llama("Roberto", "llama", "midday", "grass")
print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
# prints Roberto the alpaca is available to pet during the midday shift.