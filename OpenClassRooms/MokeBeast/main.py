from type import *
print("Welcome to MokéBeast\n")
print("Beast Battle Game")

# Création du dictionnaire Beast avec des keys vides
beast = {"name": None, "type": None, "special move": None, "staring HP": None, "staring MP": None}
print("Only 5 types existing: Fire, Earth, Wind, Water and Lightning")

for name in beast.keys():
  beast[name]= input(f"Entry the {name}: ")

animal_type = beast["type"]
beast_type(animal_type)

for name, value in beast.items():
  print(f"Your beast's {name} is {value}")