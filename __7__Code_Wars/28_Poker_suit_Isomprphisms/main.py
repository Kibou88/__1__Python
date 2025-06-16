def boards_isomorphic(s1: str, s2: str) -> bool:
    color = ['c', 'd', 'h', 's']
    temp = []
    count_color = 0
    chaine_s1 = "".join(["".join((s1[i], s1[i + 1])) for i in range(0, len(s1), 2)])
    liste_s1 = ["".join((s1[i], s1[i + 1])) for i in range(0, len(s1), 2)]
    liste_s1.sort(key=lambda x: x[1])
    chaine_s2 = "".join(["".join((s2[i], s2[i + 1])) for i in range(0, len(s2), 2)])
    liste_s2 = ["".join((s2[i], s2[i + 1])) for i in range(0, len(s2), 2)]
    liste_s2.sort(key= lambda x: x[1])

    if len(s1) != len(s2):
        return False
    # for i_s1 in range(1, len(chaine_s1), 2):
    #     for j_s2 in range(1, len(chaine_s2), 2):
    #         if
    for card_s1 in chaine_s1[0:len(chaine_s1):2]:
        for card_s2 in chaine_s2[0:len(chaine_s2):2]:
            if card_s1 == card_s2:
                pass





if __name__ == '__main__':
    color = {
        'c': "",
        'd': "",
        'h': "",
        's': ""
    }
    boards_isomorphic("AcAh2h", "AsAd2d")  # True
    boards_isomorphic("AcAh2h", "AsAd2c")  # False
    str1 = "AcAh2h"
    str2 = "AsAd2c"
    chaine_s1 = "".join(["".join((str1[i], str1[i + 1])) for i in range(0, len(str1), 2)])
    liste_s1 = ["".join((str1[i], str1[i + 1])) for i in range(0, len(str1), 2)]
    liste_s1.sort(key=lambda x: x[0])

    liste_s2 = ["".join((str2[i], str2[i + 1])) for i in range(0, len(str2), 2)]
    liste_s2.sort(key=lambda x: x[0])
    new_chaine = []
    print(chaine_s1, liste_s2)
    for i_s1 in range(len(liste_s1)):
        for j_s2 in range(len(liste_s2)):
            if liste_s1[i_s1][0] == liste_s2[j_s2][0]:
                if color[liste_s1[i_s1][1]] == "":
                    color[liste_s1[i_s1][1]] = liste_s2[j_s2][1]
                new_chaine.append((liste_s1[i_s1][0], liste_s2[i_s1][1]))

                # else:
                #     continue
            else:
                continue


    print(new_chaine)
    print(chaine_s1, str2)