from string import ascii_lowercase
from collections import OrderedDict

def connect_the_dots(paper):
    dict_coordoonees ={}
    count_letter = 0
    list_paper = paper.split("\n")[:-1]

    for row in range(len(list_paper)): # Récupération des lettres
        for col in range(len(list_paper[row])):
            if list_paper[row][col] in ascii_lowercase:
                dict_coordoonees[list_paper[row][col]] = (row, col)
    trier_dico = OrderedDict(sorted(dict_coordoonees.items())) # Dico trié

    for key, value in trier_dico.items():
        if count_letter < len(trier_dico) - 1:
            x, y = value
            next_x, next_y = trier_dico[ascii_lowercase[count_letter+1]]
            if next_x == x:
                if y < next_y:
                    list_paper[x] = list_paper[x][:y] + list_paper[x][y:next_y + 1].replace(" ", "*")\
                        .replace(key, "*").replace(ascii_lowercase[count_letter+1], '*') + list_paper[x][next_y+1:]
                elif y > next_y:
                    list_paper[x] = list_paper[x][:next_y] + list_paper[x][next_y:y + 1].replace(" ", "*")\
                        .replace(key, "*").replace(ascii_lowercase[count_letter+1], '*') + list_paper[x][y+1:]

            elif next_y == y:
                if x < next_x:
                    for cross_x in range(x, next_x+1):
                        list_paper[cross_x] = list_paper[cross_x][:next_y] + list_paper[cross_x][next_y:next_y+1]\
                            .replace(" ", "*").replace(key, "*").replace(ascii_lowercase[count_letter+1], "*")\
                                              + list_paper[cross_x][next_y+1:]
                elif x > next_x:
                    for cross_x in range(next_x, x+1):
                        list_paper[cross_x] = list_paper[cross_x][:next_y] + list_paper[cross_x][next_y:next_y + 1] \
                            .replace(" ", "*").replace(key, "*").replace(ascii_lowercase[count_letter + 1], "*") \
                                              + list_paper[cross_x][next_y + 1:]

            else:
                ecart_x = next_x - x
                ecart_y = next_y - y
                if ecart_x > 0:
                    for i in range(0, ecart_x+1):
                        list_paper[x+i] = list_paper[x+i][:(y+i if ecart_y>0 else y-i)] + \
                          list_paper[x+i][(y+i if ecart_y>0 else y-i):(y+i if ecart_y>0 else y-i) + 1] \
                            .replace(" ", "*").replace(key, "*").replace(ascii_lowercase[count_letter + 1], "*") \
                                              + list_paper[x+i][(y+i if ecart_y>0 else y-i) + 1:]
                elif ecart_x < 0:
                    for i in range(0,ecart_x-1, -1):
                        list_paper[x+i] = list_paper[x+i][:(y-i if ecart_y>0 else y+i)] + \
                          list_paper[x+i][(y-i if ecart_y>0 else y+i):(y-i if ecart_y>0 else y+i) + 1] \
                            .replace(" ", "*").replace(key, "*").replace(ascii_lowercase[count_letter + 1], "*") \
                                              + list_paper[x+i][(y-i if ecart_y>0 else y+i) + 1:]
            count_letter += 1


        else:
            break
    print("\n".join(list_paper))
    # return ""


if __name__ == '__main__':
    paper = (
            "           \n" +
            " a       b \n" +
            " e         \n" +
            "           \n" +
            " d       c \n" +
            "           \n" )
    paper2 = (
            "           \n" +
            "     a     \n" +
            "    e      \n" +
            "           \n" +
            "  d     b  \n" +
            "           \n" +
            "           \n" +
            "     c     \n" +
            "           \n")
    connect_the_dots(paper)
    connect_the_dots(paper2)