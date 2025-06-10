solar_system = ["<Meteoroid", "Meteoroid>", "Meteoroid>", "((Mercury))", "Meteoroid>", "Mars", \
         "<Meteoroid", "Meteoroid>", "((Earth))"]

list_planets = ["Mercury", "Venus", "Mars", "Earth"]
dict_planet = {}

for i in solar_system:
    for planet in list_planets:
        if planet in i:
            dict_planet[planet] = i.count("(")


print(dict_planet)