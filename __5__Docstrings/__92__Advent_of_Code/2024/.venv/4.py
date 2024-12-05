# Day 4 Advent of Code 2024
#----------------------------

FILE_TEST = "./datas/data_test_4.txt"
FILE_PUZZLE = "./datas/4.txt"

def read_horizontally(words, datas):
    count_words = 0
    for data in datas:
        for mot in words:
            count_words += data.count(mot)
    return count_words


def read_vertically(words, datas):
    count_words = 0

    for ligne in range(len(datas) - 3):
        # vertical_word = ""
        for colonne in range(len(datas[ligne])):
            # print(len(datas[ligne]))
            vertical_word = datas[ligne][colonne] + datas[ligne + 1][colonne] + datas[ligne + 2][colonne] + \
                            datas[ligne + 3][colonne]
            if vertical_word in words:
                count_words += 1
    return count_words


def read_diagonnally(words, datas):
    count_words = 0
    word_1 = words[0]  # MAS
    word_2 = words[1]  # SAM

    for ligne in range(len(datas) - 3):
        diagonal_words = ""
        for colonne in range(len(datas[ligne]) - 3):
            # print(len(datas[ligne]))
            diagonal_words = datas[ligne][colonne] + datas[ligne + 1][colonne + 1] + datas[ligne + 2][colonne + 2] + \
                             datas[ligne + 3][colonne + 3]
            if diagonal_words in words:
                count_words += 1

    for ligne in range(len(datas) - 3):
        diagonal_words = ""
        for colonne in range(len(datas[ligne]) - 3):
            # print(len(datas[ligne]))
            diagonal_words = datas[ligne][colonne + 3] + datas[ligne + 1][colonne + 2] + datas[ligne + 2][colonne + 1] + \
                             datas[ligne + 3][colonne]
            if diagonal_words in words:
                count_words += 1
    # print(count_words)
    return count_words


def read_diagonnally_2(words, datas):
    count_words = 0
    coord_x_y = []
    word_1 = words[0]  # MAS
    word_2 = words[1]  # SAM

    for ligne in range(len(datas) - 2):
        diagonal_words = ""
        for colonne in range(len(datas[ligne]) - 2):
            diagonal_words = datas[ligne][colonne] + datas[ligne + 1][colonne + 1] + datas[ligne + 2][colonne + 2]
            if diagonal_words in words:
                coord_x_y.append((ligne+1,colonne+1))
    print(coord_x_y)
    for ligne in range(len(datas) - 2):
        diagonal_words = ""
        for colonne in range(len(datas[ligne]) - 2):

            diagonal_words = datas[ligne][colonne + 2] + datas[ligne + 1][colonne + 1] + datas[ligne + 2][colonne]
            if diagonal_words in words:
                for coord in range(len(coord_x_y)):
                    if (ligne+1) == coord_x_y[coord][0] and (colonne+1) == coord_x_y[coord][1]:
                        count_words += 1

    return count_words


if __name__ == '__main__':
    with open(FILE_PUZZLE, "r") as f:
        datas = f.read().splitlines()

    total_count = 0
    total_count_2 = 0
    words = ['XMAS', 'SAMX']
    words_2 = ['MAS', 'SAM']

    # total_count += read_horizontally(words, datas)
    # total_count += read_vertically(words, datas)
    # total_count += read_diagonnally(words, datas)
    # print(total_count)

# total_count_2 += read_horizontally(words_2, datas)
# total_count_2 += read_vertically(words_2, datas)
total_count_2 += read_diagonnally_2(words_2, datas)
print(total_count_2)