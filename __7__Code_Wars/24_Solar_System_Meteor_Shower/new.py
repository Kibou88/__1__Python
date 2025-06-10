def meteor_shower(solar_system):
    list_planets = ["Mercury", "Venus", "Mars", "Earth"]
    dict_planets = {}

    for i in solar_system:
        for planet in list_planets:
            if planet in i:
                dict_planets[planet] = i.count("(")
    # print(dict_planets)
    impact = 0
    for element in range(len(solar_system)):
        # Météorite va à droite
        if "Meteoroid>" in solar_system[element]:
            # j = element + 1
            for j in range(element + 1, len(solar_system)):
                for key in list(dict_planets.keys()):
                    if key in solar_system[j]:
                        if dict_planets[key] >= 1:
                            dict_planets[key] -= 1
                            print("Planete trouve: ", key)
                            print("Nouvelle valeur bouclier: ", dict_planets[key])
                            print()
                            impact += 1
                        elif dict_planets[key] == 0:
                            dict_planets.pop(key)
                            print(f"La planete {key} a ete supprime")
                            print()
                            impact += 1
                        break
                if impact:
                    impact = 0
                    break

        elif "<Meteoroid" in solar_system[element]:
            # j = element - 1
            for j in range(element - 1, -1, -1):
                for key in list(dict_planets.keys()):
                    if key in solar_system[j]:
                        if dict_planets[key] >= 1:
                            dict_planets[key] -= 1
                            print("Planete trouve: ", key)
                            print("Nouvelle valeur bouclier: ", dict_planets[key])
                            print()
                            impact += 1
                        elif dict_planets[key] == 0:
                            dict_planets.pop(key)
                            print(f"La planete {key} a ete supprime")
                            print()
                            impact += 1
                        break
                if impact:
                    impact = 0
                    break
    return [(value*"("+key+value*")") for key, value in dict_planets.items()]



if __name__ == '__main__':
    solar_system = ["<Meteoroid", "Meteoroid>", "Meteoroid>", "((Mercury))", "Meteoroid>", "Mars", \
         "<Meteoroid", "Meteoroid>", "((Earth))"]
    solar_system2 = ['((((((((Venus))))))))', '<Meteoroid', '<Meteoroid', '<Meteoroid', '<Meteoroid', \
                     '<Meteoroid', '<Meteoroid']

    # print(meteor_shower(solar_system))
    print(meteor_shower(solar_system2))