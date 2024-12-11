# Day 11 Advent of Code 2024
#----------------------------
from logging.config import stopListening

FILE_TEST = "./datas/datas_test_11.txt"
FILE = "./datas/11.txt"

def change_0_to_1():
    return "1"

def split_even_digit_numbers(stone):
    middle_stone = int(len(stone) / 2)

    stone_part0 = stone[0:middle_stone:]
    if len(stone_part0) == stone_part0.count("0"):
        stone_part0 = 0
    elif stone_part0[0] == "0":
        stone_part0 = stone_part0[1:]

    stone_part1 = stone[middle_stone:]
    if len(stone_part1) == stone_part1.count("0"):
        stone_part1 = 0
    elif stone_part1[0] == "0":
        stone_part1 = stone_part1[1:]
    return stone_part0, stone_part1

def multiplication_2024(stone):
    return str(int(stone) * 2024)

if __name__ == "__main__":
    with open(FILE, 'r') as f:
        datas = f.read()
    stones = datas.split(" ")

    print("Initial arrangement:")
    print(stones)
    print()
    temp_list = []

    for i in range(1,26,1):
        for index_stone in range(len(stones)):
            if int(stones[index_stone]) == 0:
                temp_list.append(change_0_to_1())

            elif len(stones[index_stone]) % 2 == 0:
                stone_part0, stone_part1 = split_even_digit_numbers(stones[index_stone])
                temp_list.append(stone_part0)
                temp_list.append(stone_part1)

            else:
                temp_list.append(multiplication_2024(stones[index_stone]))

        stones = temp_list
        temp_list = []
        print(f"After {i} blinks:")
        print(stones)
        print(len(stones))
        print()
