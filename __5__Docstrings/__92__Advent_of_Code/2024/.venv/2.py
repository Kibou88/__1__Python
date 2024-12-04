# Day 2 Advent of Code 2024
#----------------------------
file_test = "/home/kibou/Bureau/Python/__1__Python/__5__Docstrings/__92__Advent_of_Code/2024/.venv/datas/data_test.txt"
file = "/home/kibou/Bureau/Python/__1__Python/__5__Docstrings/__92__Advent_of_Code/2024/.venv/datas/2.txt"
number_table = []
origine = 0
total_safe = 0
total_unsafe = 0
variation = None  # True si increase // False si decrease
unsafe_table = []

with open(file, "r") as f:
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
# Partie 2
for ko_numbers in unsafe_table:
    # print(unsafe_table)
    deleted_level_remaining = 1
    origine = 0
    variation = None



    for number in ko_numbers:

        for reverse_number in ko_numbers[::-1]:
            if reverse_number == number and ko_numbers.count(number) == 2:
                ko_numbers.remove(reverse_number)
                deleted_level_remaining -= 1
                new_ko_numbers.append(ko_numbers)
        number = int(number)
        print(f"Number {number}")
        print(f"longueur {len(ko_numbers)}\n")
        print(new_ko_numbers)
        if origine == 0:
            origine = number
        elif ko_numbers.count(str(number)) >= 3:
            break
        elif ko_numbers.index(str(number)) ==  len(ko_numbers):
            total_unsafe += 1
        elif (origine + 1) == number or (origine + 2) == number or (origine + 3) == number:
            if variation != False:
                origine = number
                variation = True
            elif variation == False and deleted_level_remaining == 1:
                print(number)
                ko_numbers.remove(str(number))
                deleted_level_remaining -= 1
            else:
                break
        elif (origine - 1) == number or (origine - 2) == number or (origine - 3) == number:
            if variation != True:
                origine = number
                variation = False

            elif variation == True and deleted_level_remaining == 1:
                print(number)
                ko_numbers.remove(str(number))
                deleted_level_remaining -= 1
            else:
                break
        elif ((origine + 3) > number or (origine - 3) < number) and deleted_level_remaining == 1:
            print(number)
            ko_numbers.remove(str(number))
            deleted_level_remaining -= 1

print()
print(total_safe)
print(total_unsafe)
