"""
AIDE PAR MISTRAL AI
"""
def strip_comments(strng, markers):
    lines = strng.split('\n')
    result = []

    for line in lines:
        # Trouver le premier indice d'un marqueur dans la ligne
        min_index = len(line)
        for marker in markers:
            index = line.find(marker)
            if index != -1 and index < min_index:
                min_index = index

        # Ajouter la partie de la ligne avant le marqueur
        result.append(line[:min_index].rstrip())

    # Joindre les lignes avec des sauts de ligne
    return '\n'.join(result)




if __name__ == '__main__':
    strng = "apples, pears # and bananas\ngrapes\nbananas !apples"
    markers = ["#", "!"]
    result = "apples, pears\ngrapes\nbananas"
    strng2 = "  ^ bananas apples apples cherries bananas\npears strawberries !\n="
    marker2 = ["'", '=', '@', '^', '-', '?']
    # result2 = ' \npears strawberries !\n' should equal '\npears strawberries !\n'
    result2 = "\npears strawberries !\n"
    strip_comments(strng, markers)
    print(strip_comments(strng, markers) == result)
    print(strip_comments(strng2, marker2) == result2)