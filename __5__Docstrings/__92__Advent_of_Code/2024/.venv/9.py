# Day 9 Advent of Code 2024
#----------------------------

FILE_TEST = ".//datas//datas_test_9.txt"
FILE = ".//datas//9.txt"

formatted_datas = ""

def formatting_datas(datas):
    format_data = ""
    count_id = 0
    for index, character in enumerate(datas):
        if index % 2 == 0:
            format_data += str(count_id) * int(character)
            count_id += 1
        else:
            format_data += "." * int(character)
    # print(format_data)
    return format_data

def move_blocks(formatted_datas):
    compacting_process = []
    reverse_index = -1
    total_point = []
    list_datas = []
    for data in formatted_datas:
        list_datas.append(data)
    # print(list_datas)
    for index, character in enumerate(formatted_datas):
        if character.isdigit():
            compacting_process.append(character)
        elif character == ".":
            # total_point.append(character)
            # print(list_datas[-1])
            print(index)
            list_datas.insert(index, 9)
            list_datas.append(list_datas.pop(list_datas.index(character)))
            reverse_index -= 1
    print(total_point)
    print("".join(list_datas))

if __name__ == "__main__":
    with open(FILE_TEST, "r") as f:
        datas = f.read()

    formatted_datas = formatting_datas(datas)

    move_blocks(formatted_datas)