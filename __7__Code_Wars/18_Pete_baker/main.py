def cakes(recipe, available):
    number = []
    for ingredient in recipe.keys():
        if not ingredient in available:
            return 0
        number.append(int(available[ingredient] / recipe[ingredient]))

    return sorted(number)[0]


if __name__ == "__main__":
    classicPie = ({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
    applePie = ({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
                {"sugar": 500, "flour": 2000, "milk": 2000})
    # for ingredient in classicPie[0].keys():
    #     print(int(classicPie[1][ingredient] / classicPie[0][ingredient]))

    print(cakes(classicPie[0], classicPie[1]))
    print(cakes(applePie[0], applePie[1]))