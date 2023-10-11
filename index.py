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
print(roberto.feed())
# prints Roberto the alpaca is available to pet during the midday shift.

emma = Cat("Emma", "cat", "midday", "tuna")
print(f'{emma.name} the {emma.species} is available to pet during the {emma.shift} shift. {emma.name} enjoys {emma.food}.')
print(emma.feed())

fred = Dog("Fred", "dog", "midday", "bacon")
print(f'{fred.name} the {fred.species} is available to pet during the {fred.shift} shift. {fred.name} enjoys {fred.food}.')
print(fred.feed())

molly = Goat("Molly", "goat", "midday", "Hay")
print(f'{molly.name} the {molly.species} is available to pet during the {molly.shift} shift. {molly.name} enjoys {molly.food}.')
print(molly.feed())

mary = Donkey("Mary", "donkey", "midday", "carrots")
print(f'{mary.name} the {mary.species} is available to pet during the {mary.shift} shift. {mary.name} enjoys {mary.food}.')
print(mary.feed())

# slithering
regina = Cottonmouth("Regina", "cottonmouth", "rats")
print(f'{regina.name} the {regina.species} is available in the Snakepit attration. {regina.name} enjoys {regina.food}.')
print(regina.feed())

# swimming
kermy = Frog("Kermy", "frog", "flies")
print(f'{kermy.name} the {kermy.species} is available in the Pond attration. {kermy.name} enjoys {kermy.food}.')
print(kermy.feed())





# # Create an attraction
varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
snake_pit = Snakepit("Snake Pit", "critters that slither and strike")
wet_lands = Wetlands("Wetlands", "critters that swim and splash")

# add animal
varmint_village.add_animal_pythonic(emma)
varmint_village.add_animal_type_check(emma)
varmint_village.add_animal_pythonic(emma)

snake_pit.add_animal_pythonic(regina)
snake_pit.add_animal_type_check(regina)
snake_pit.add_animal_pythonic(regina)

wet_lands.add_animal_pythonic(kermy)
wet_lands.add_animal_type_check(kermy)
wet_lands.add_animal_pythonic(kermy)



# check to see which animals where added to attractions list
for animal in varmint_village.animals:
    print(animal)