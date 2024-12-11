# Day 2 Advent of Code 2024
#----------------------------
file_test = "./datas/datas_test_2.txt"
file = "./datas/2.txt"
number_table = []
origine = 0
total_safe = 0
total_unsafe = 0
variation = None  # True si increase // False si decrease
unsafe_table = []

with open(file_test, "r") as f:
    lines = f.read().splitlines()

# Partie 1
for line in lines:
    number_table = line.split()
    variation = None
    origine = 0
    for number in number_table:
        number = int(number)
        if origine == 0:
            origine = number

        elif number_table.count(str(number)) >= 2:
            # print(f"Number_table {number_table} non pris en compte")
            unsafe_table.append(number_table)
            break

        elif number == int(number_table[-1]):
            # print("fin")
            if (origine + 1) == number or (origine + 2) == number or (origine + 3) == number:
                if variation != False:
                    total_safe += 1
                else:
                    unsafe_table.append(number_table)
                    break

            elif (origine - 1) == number or (origine - 2) == number or (origine - 3) == number:
                if variation != True:
                    total_safe += 1
                else:
                    unsafe_table.append(number_table)
                    break

            # print("lignes juste", number_table)

        elif (origine + 1) == number or (origine + 2) == number or (origine + 3) == number:
            if variation != False:
                origine = number
                variation = True
            else:
                break

        elif (origine - 1) == number or (origine - 2) == number or (origine - 3) == number:
            if variation != True:
                origine = number
                variation = False
            else:
                unsafe_table.append(number_table)
                break

        else:
            unsafe_table.append(number_table)
            break

print(unsafe_table)

# ------------------------ Partie 2 ----------------------
new_unsafe_table = []
for ko_numbers in unsafe_table:
    # Si il ya plus de 2 éléments identiques, suppression de la liste => OK
    for index, number in enumerate(ko_numbers):
        print(number, ko_numbers.count(number))
        if ko_numbers.count(number) == 2:
            ko_numbers.pop(number)
        elif ko_numbers.count(number) > 2:
            unsafe_table.pop(unsafe_table.index(ko_numbers))
            print("Liste retirée: ", ko_numbers)
            break

    print(unsafe_table)

    for index_number in range(len(ko_numbers)):
        if (int(ko_numbers[index_number]) + 1) == ko_numbers[index_number + 1] or \
            (int(ko_numbers[index_number]) + 2) == ko_numbers[index_number + 1] or \
              (int(ko_numbers[index_number]) + 3) == ko_numbers[index_number + 1]:
            pass
        elif (int(ko_numbers[index_number]) - 1) == ko_numbers[index_number + 1] or \
              (int(ko_numbers[index_number]) - 2) == ko_numbers[index_number + 1] or \
                (int(ko_numbers[index_number]) - 3) == ko_numbers[index_number + 1]:
            pass

        else:
            pass

    # print()


# print()
# print(total_safe)
# print(total_unsafe)
