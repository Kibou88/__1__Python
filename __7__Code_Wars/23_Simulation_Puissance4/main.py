"""
AIDE PAR MISTRAL AI
"""
def connect_four_place(tokens):
    # Initialisation du plateau
    table = [["-" for i in range(7)] for j in range(6)]
    turn = 1  # Yellow first

    for token in tokens:
        column = token
        for row in range(5,-1,-1):
            if table[row][column] == "-":
                if turn % 2 == 0:
                    table[row][column] = "R"
                else:
                    table[row][column] = "Y"
                turn += 1
                break
    for i in table:
        print(i)


if __name__ == '__main__':
    columns = [0,1,2,5,6,2,0,0]

    connect_four_place(columns)