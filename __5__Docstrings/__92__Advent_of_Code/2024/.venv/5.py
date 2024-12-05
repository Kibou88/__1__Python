# Day 5 Advent of Code 2024
#----------------------------
from weakref import finalize

FILE_TEST = "./datas/datas_test_5.txt"
FILE_PUZZLE = "./datas/5.txt"

list_datas_2 = []
list_datas_1 = []
final_list = []
recup_datas = []
wrong_final_list = []



def shape_datas(datas):
    list_datas_1 = []
    list_datas_2 = []

    for data in datas:
        if "|" in data:
            list_datas_1.append(data.split("|"))
        elif "," in data:
            list_datas_2.append(data.split(","))
    return list_datas_1, list_datas_2

def total(final_list):
    total = 0
    for ligne in range(len(final_list)):
        milieu = len(final_list[ligne]) // 2
        total += (int(final_list[ligne][milieu]))
    return total

if __name__ == "__main__":
    with open(FILE_TEST, "r") as f:
        datas = f.read().splitlines()

    list_datas_1, list_datas_2 = shape_datas(datas)


    # print(list_datas_2)
    for numbers in range(len(list_datas_2)):

        total_count = 0
        # print(list_datas_2[numbers]) # Liste pour chaque ligne
        list_test = [True]
        for number in range(len(list_datas_2[numbers])-1):
            recup_datas = []
            # print(list_datas_2[numbers][number]) # Liste chaque élément pour chaque ligne

            for pages in range(len(list_datas_1)):
                # print(list_datas_1[pages]) # Liste chaque ligne de la 1ère partie
                if list_datas_2[numbers][number] == list_datas_1[pages][0]:
                    # print(f"{list_datas_2[numbers][number]} se trouve {list_datas_1[pages]}")
                    recup_datas.append(list_datas_1[pages][1])
            # print(f"Pour {list_datas_2[numbers][number]} récup: {recup_datas}")
            if len(recup_datas) == 0:
                list_test.append(False)
                break

            for index in range(len(list_datas_2[numbers][number+1::])):
                index += 1
                # for data in range(len(recup_datas)):
                if list_datas_2[numbers][number+index] in recup_datas:
                    pass
                    # print(f"{list_datas_2[numbers][number+index]} est bien dans recup datas")
                else:
                    list_test.append(False)
            list_test.append(True)
        if not False in list_test:
            final_list.append(list_datas_2[numbers])
        if False in list_test:
            wrong_final_list.append(list_datas_2[numbers])


    print("Résultat part one:", total(final_list))


# -------------------------- PART TWO --------------------------------------------
    wrong_list = []
    # for line in range(len(wrong_final_list)):
    #     nvline = []
    # for col in range(len(wrong_final_list[line])):
    #     wrong_list.append((line, col))
    # # wrong_list.append(nvline)
    # print(wrong_list)
    #

    print(wrong_list)
    for numbers in range(len(wrong_final_list)):

        total_count = 0
        print(wrong_final_list[numbers]) # Liste pour chaque ligne
        wrong_list.append(numbers)
        for number in range(len(wrong_final_list[numbers])-1):

            recup_datas = []
            # print(wrong_final_list[numbers][number]) # Liste chaque élément pour chaque ligne

            for pages in range(len(list_datas_1)):
                # print(list_datas_1[pages]) # Liste chaque ligne de la 1ère partie
                if wrong_final_list[numbers][number] == list_datas_1[pages][1]:
                    print(f"{wrong_final_list[numbers][number]} se trouve {list_datas_1[pages]}")
                    wrong_list[numbers].append(list_datas_1[pages][1], list_datas_1[pages][0])
            print(wrong_list)
