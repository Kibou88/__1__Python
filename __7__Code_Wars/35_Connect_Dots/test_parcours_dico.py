from string import ascii_lowercase
from collections import OrderedDict

paper = (
            "           \n" +
            "     a     \n" +
            "    e      \n" +
            "           \n" +
            "  d     b  \n" +
            "           \n" +
            "           \n" +
            "     c     \n" +
            "           \n")
list_paper = paper.split("\n")[:-1]
dict_coordoonees = OrderedDict()
for row in range(len(list_paper)): # Récupération des lettres
    # print(len(list_paper[row]))
    for col in range(len(list_paper[row])):
        if list_paper[row][col] in ascii_lowercase:
            dict_coordoonees[list_paper[row][col]] = (row, col)
trier_dico = OrderedDict(sorted(dict_coordoonees.items())) # Dico trié

print(trier_dico)
count_letter = 0
for key, value in trier_dico.items():
    if count_letter < len(trier_dico) - 1:
        x, y = value
        next_x, next_y = trier_dico[ascii_lowercase[count_letter + 1]]
        abs_ecart = abs(next_x - x)
        print(abs_ecart)
        count_letter += 1

    else:
        break
