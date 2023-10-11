# import the python datetime module to help us create a timestamp
from datetime import date
# from animals import Animal


# import categories swimming, slithering, and walking and then each animal
from animals import Beetle, Copperhead, Cottonmouth, Kingsnake, Ratsnake
from animals import Cat, Dog, Donkey, Goat, Llama
from animals import Frog, Bass, Carp, Goldfish, Mallard
from attractions import PettingZoo
from attractions import Snakepit
from attractions import Wetlands

# , Snakepit, Wetlands

# add vscode
# walking
roberto = Llama("Roberto", "llama", "midday", "grass", 1)
print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
# prints Roberto the alpaca is available to pet during the midday shift.

emma = Cat("Emma", "cat", "midday", "tuna")
print(f'{emma.name} the {emma.species} is available to pet during the {emma.shift} shift. {emma.name} enjoys {emma.food}.')
print(emma.feed())

# slithering
regina = Cottonmouth("Regina", "cottonmouth", "rat")
print(f'{regina.name} the {regina.species} is available in the Snakepit attration. {regina.name} enjoys {regina.food}.')
print(regina.feed())

# swimming
kermy = Frog("Kermy", "frog", "flies")
print(f'{kermy.name} the {kermy.species} is available in the Pond attration. {kermy.name} enjoys {kermy.food}.')
print(kermy.feed())





# # Create an attraction
varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")

# add animal
varmint_village.add_animal_pythonic(emma)
varmint_village.add_animal_type_check(emma)
varmint_village.add_animal_pythonic(emma)


# check to see which animals where added to attractions list
for animal in varmint_village.animals:
    print(animal)