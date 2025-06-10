def meteor_shower(solar_system):
    list_planets = ["Mercury", "Venus", "Mars", "Earth"]
    planets = {}

    for i in solar_system:
        for planet in list_planets:
            if planet in i:
                planets[planet] = i.count("(")

    temp = list(solar_system)

    impact = 0
    for i in range(len(solar_system)):
        if "Meteoroid>" in solar_system[i]:
            for j in range(i + 1, len(solar_system)):
                for key in list(planets.keys()):
                    if key in solar_system[j]:
                        planets[key] -= 1
                        impact = 1
                        if planets[key] < 0:
                            impact = 1
                            del planets[key]
                        break
                if impact:
                    impact = 0
                    break
        elif "<Meteoroid" in solar_system[i]:
            for j in range(i, 0, -1):
                for key in list(planets.keys()):
                    if key in solar_system[j]:
                        planets[key] -= 1
                        impact = 1
                        if planets[key] < 0:
                            impact = 1
                            del planets[key]
                        break
                if impact:
                    impact = 0
                    break

    return [(value*"("+key+value*")") for key, value in planets.items()]


if __name__ == '__main__':
    solar_system = ["<Meteoroid", "Meteoroid>", "Meteoroid>", "((Mercury))", "Meteoroid>", "Mars", \
         "<Meteoroid", "Meteoroid>", "((Earth))"]
    solar_system2 = ['Meteoroid>']

    print(meteor_shower(solar_system))
    print(meteor_shower(solar_system2))