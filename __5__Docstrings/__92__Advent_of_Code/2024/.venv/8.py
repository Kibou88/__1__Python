# Day 8 Advent of Code 2024
#----------------------------

FILE_TEST = ".//datas//datas_test_8.txt"
FILE = ".//datas//8.txt"

LIST_ALPHANUM = []
LIST_POSITIONS = []
TOTAL_DIESE = 0
POS_DIESE = []

def recup_alphanum(datas):
    liste = []

    for y in range(len(datas)):
        for x, character in enumerate(datas[y]):
            # print(character)
            if character.isalnum() and character not in liste:
                liste.append(character)
    return liste

def recup_positions(datas, character):
    liste_pos = []
    for y in range(len(datas)):
        for x in range(len(datas[y])):
            if character == datas[y][x]:
                liste_pos.append((x, y))
    return liste_pos

if __name__ == "__main__":
    with open(FILE, 'r') as f:
        datas = f.read().splitlines()

    LIST_ALPHANUM = recup_alphanum(datas)
    print(len(datas[0]))
    for character in LIST_ALPHANUM:
        LISTE_POSITIONS = recup_positions(datas, character)
        for positions in LISTE_POSITIONS:
            print(positions)
            if LISTE_POSITIONS.index(positions) == 0:
                for next in range(1,len(LISTE_POSITIONS)):
                    diff_x = positions[0] - LISTE_POSITIONS[next][0]
                    diff_y = positions[1] - LISTE_POSITIONS[next][1]

                    if ((diff_x + positions[0]) <= len(datas[0]) and (diff_x + positions[0]) >= 0) \
                            and ((diff_y + positions[1]) >= 0 and (diff_y + positions[1]) <= len(datas)):
                        if (diff_x + positions[0]) not in POS_DIESE and (diff_y + positions[1]) not in POS_DIESE:
                            POS_DIESE.append((diff_x + positions[0], diff_y + positions[1]))

                    if ((LISTE_POSITIONS[next][0] - diff_x) <= len(datas[0]) and (LISTE_POSITIONS[next][0] - diff_x) >= 0) \
                        and ((LISTE_POSITIONS[next][1] - diff_y) >= 0 and (LISTE_POSITIONS[next][1] - diff_y) <= len(datas)):
                        if (LISTE_POSITIONS[next][0] - diff_x) not in POS_DIESE and (LISTE_POSITIONS[next][1] - diff_y) not in POS_DIESE:
                            POS_DIESE.append((LISTE_POSITIONS[next][0] - diff_x, LISTE_POSITIONS[next][1] - diff_y))

            elif LISTE_POSITIONS.index(positions) == (len(LISTE_POSITIONS)-1):
                diff_x = positions[0] - LISTE_POSITIONS[-1][0]
                diff_y = positions[1] - LISTE_POSITIONS[-1][1]

                if ((diff_x + positions[0]) <= len(datas[0]) and (diff_x + positions[0]) >= 0) \
                        and ((diff_y + positions[1]) >= 0 and (diff_y + positions[1]) <= len(datas)):
                    if (diff_x + positions[0]) not in POS_DIESE and (diff_y + positions[1]) not in POS_DIESE:
                        POS_DIESE.append((diff_x + positions[0], diff_y + positions[1]))

                if ((LISTE_POSITIONS[-1][0] - diff_x) <= len(datas[0]) and (LISTE_POSITIONS[-1][0] - diff_x) >= 0) \
                        and ((LISTE_POSITIONS[-1][1] - diff_y) >= 0 and (LISTE_POSITIONS[-1][1] - diff_y) <= len(datas)):

                    if (LISTE_POSITIONS[-1][0] - diff_x) not in POS_DIESE and (LISTE_POSITIONS[-1][1] - diff_y) not in POS_DIESE:
                        POS_DIESE.append((LISTE_POSITIONS[-1][0] - diff_x, LISTE_POSITIONS[-1][1] - diff_y))
            else:

                index = LISTE_POSITIONS.index(positions)
                diff_x_1 = positions[0] - LISTE_POSITIONS[index-1][0]
                diff_y_1 = positions[1] - LISTE_POSITIONS[index-1][1]

                if ((diff_x_1 + positions[0]) <= len(datas[0]) and (diff_x_1 + positions[0]) >= 0) \
                        and ((diff_y_1 + positions[1]) >= 0 and (diff_y_1 + positions[1]) <= len(datas)):

                    if (diff_x_1 + positions[0]) not in POS_DIESE and (diff_y_1 + positions[1]) not in POS_DIESE:
                        POS_DIESE.append((diff_x_1 + positions[0], diff_y_1 + positions[1]))

                if ((LISTE_POSITIONS[index-1][0] - diff_x_1) <= len(datas[0]) and (LISTE_POSITIONS[index-1][0] - diff_x_1) >= 0) \
                        and ((LISTE_POSITIONS[index-1][1] - diff_y_1) >= 0 and (LISTE_POSITIONS[index-1][1] - diff_y_1) <= len(datas)-1):
                    if (LISTE_POSITIONS[index-1][0] - diff_x_1) not in POS_DIESE and (LISTE_POSITIONS[index-1][1] - diff_y_1) not in POS_DIESE:
                        POS_DIESE.append((LISTE_POSITIONS[index-1][0] - diff_x_1, LISTE_POSITIONS[index-1][1] - diff_y_1))
                # ----------------------- 2nd part--------------------------
                diff_x_2 = positions[0] - LISTE_POSITIONS[index + 1][0]
                diff_y_2 = positions[1] - LISTE_POSITIONS[index + 1][1]

                if ((diff_x_2 + positions[0]) <= len(datas[0]) and (diff_x_2 + positions[0]) >= 0) \
                        and ((diff_y_2 + positions[1]) >= 0 and (diff_y_2 + positions[1]) <= len(datas)):

                    if (LISTE_POSITIONS[index - 1][0] - diff_x_2) not in POS_DIESE and (LISTE_POSITIONS[index - 1][1] - diff_y_2) not in POS_DIESE:
                        POS_DIESE.append((diff_x_2 + positions[0], diff_y_2 + positions[1]))

                if ((LISTE_POSITIONS[index + 1][0] - diff_x_2) <= len(datas[0]) and (LISTE_POSITIONS[index + 1][0] - diff_x_2) >= 0) \
                        and ((LISTE_POSITIONS[index + 1][1] - diff_y_2) >= 0 and (LISTE_POSITIONS[index + 1][1] - diff_y_2) <= len(datas)):
                    if (LISTE_POSITIONS[index + 1][0] - diff_x_2) not in POS_DIESE and (LISTE_POSITIONS[index + 1][1] - diff_y_2) not in POS_DIESE:
                        POS_DIESE.append((LISTE_POSITIONS[index + 1][0] - diff_x_2, LISTE_POSITIONS[index + 1][1] - diff_y_2))

print(len(POS_DIESE))
print("Nombre dièse: ", len(set(POS_DIESE)))