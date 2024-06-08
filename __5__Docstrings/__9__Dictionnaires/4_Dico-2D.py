# Dictionnaire en 2D
# - But: Créer un dictionnaire en 2D
####################################################################
mokeBeast = {}

def prettyPrint():
    print()
    for key, value in mokeBeast.items():
        print("name: ", key, end=" | ")
        for subKey, subValue in value.items():
            subKey = subKey + ":"
            print(subKey, subValue, end=" | ")
        print()


while True:
    print("MokeBeast Generator\n")
    name = input("Input the beast name > ")
    element = input("Input the beast element > ")
    special = input("Input the beast special > ")
    hp = input("Input the beast hp > ")
    mp = input("Input the beast mp > ")

    mokeBeast[name] = {"element": element, "special": special, "hp": hp, "mp": mp}

    prettyPrint()

    again = input("Again? y/n > ")
    if again.lower() == "y" or again.lower() == "yes":
        exit()
