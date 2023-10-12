# import the python datetime module to help us create a timestamp
from datetime import date
# from animals import Animal


# import categories swimming, slithering, and walking and then each animal
from animals import Beetle, Copperhead, Cottonmouth, Kingsnake, Ratsnake
from animals import Cat, Dog, Donkey, Goat, Llama, Goose
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

emma = Cat("Emma", "cat", "midday", "tuna", 10)
print(f'{emma.name} the {emma.species} is available to pet during the {emma.shift} shift. {emma.name} enjoys {emma.food}.')
print(emma.feed())

fred = Dog("Fred", "dog", "midday", "bacon", 11)
print(f'{fred.name} the {fred.species} is available to pet during the {fred.shift} shift. {fred.name} enjoys {fred.food}.')
print(fred.feed())

molly = Goat("Molly", "goat", "midday", "Hay", 12)
print(f'{molly.name} the {molly.species} is available to pet during the {molly.shift} shift. {molly.name} enjoys {molly.food}.')
print(molly.feed())

mary = Donkey("Mary", "donkey", "midday", "carrots", 14)
print(f'{mary.name} the {mary.species} is available to pet during the {mary.shift} shift. {mary.name} enjoys {mary.food}.')
print(mary.feed())

# slithering
regina = Cottonmouth("Regina", "cottonmouth", "rats", 50)
print(f'{regina.name} the {regina.species} is available in the Snakepit attration. {regina.name} enjoys {regina.food}.')
print(regina.feed())

pam = Copperhead("Pam", "opperhead", "rats", 60)
print(f'{pam.name} the {pam.species} is available in the Snakepit attration. {pam.name} enjoys {pam.food}.')
print(pam.feed())

rose = Ratsnake("Rose", "ratsnake", "rats", 80)
print(f'{rose.name} the {rose.species} is available in the Snakepit attration. {rose.name} enjoys {rose.food}.')
print(rose.feed())

gus = Beetle("Gus", "beetle", "fruit", 100)
print(f'{gus.name} the {gus.species} is available in the Snakepit attration. {gus.name} enjoys {gus.food}.')
print(gus.feed())

sam = Kingsnake("Sam", "kingsnake", "rats", 110)
print(f'{sam.name} the {sam.species} is available in the Snakepit attration. {sam.name} enjoys {sam.food}.')
print(sam.feed())

# swimming
kermy = Frog("Kermy", "frog", "flies", 112)
print(f'{kermy.name} the {kermy.species} is available in the Pond attration. {kermy.name} enjoys {kermy.food}.')
print(kermy.feed())

kate = Carp("Kate", "carp", "worms",114)
print(f'{kate.name} the {kate.species} is available in the Pond attration. {kate.name} enjoys {kate.food}.')
print(kate.feed())

bess = Bass("Bess", "bass", "flies", 2)
print(f'{bess.name} the {bess.species} is available in the Pond attration. {bess.name} enjoys {bess.food}.')
print(bess.feed())

goldy = Goldfish("Goldie", "goldfish", "pellets",500)
print(f'{goldy.name} the {goldy.species} is available in the Pond attration. {goldy.name} enjoys {goldy.food}.')
print(goldy.feed())

molly = Mallard("Molly", "duck", "bread", 1)
print(f'{molly.name} the {molly.species} is available in the Pond attration. {molly.name} enjoys {molly.food}.')
print(molly.feed())

nan = Goose("Nan", "goose",900, "pellets", 10)
print(f'{nan.name} the {nan.species} is available in the Pond attration. {nan.name} enjoys {nan.food}.')
print(molly.feed())

 # Create an attraction
varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
snake_pit = Snakepit("Snake Pit", "critters that slither and strike")
wet_lands = Wetlands("Wetlands", "critters that swim and splash")

# add animal
varmint_village.add_animal_pythonic(emma)
varmint_village.add_animal_type_check(emma)


snake_pit.add_animal_pythonic(regina)
snake_pit.add_animal_type_check(regina)


wet_lands.add_animal_pythonic(kermy)
wet_lands.add_animal_type_check(kermy)




# check to see which animals where added to attractions list
for animal in varmint_village.animals:
    print(animal)
    
for animal in snake_pit.animals:
    print(animal)
    
for animal in wet_lands.animals:
    print(animal)