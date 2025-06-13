import itertools

import itertools


def get_chess960_position(n):
    chess960_positions = []
    pieces = ['b', 'b', 'n', 'n', 'r', 'r', 'k', 'q']
    pawn = ["p"] * 8
    empty_case = ["."] * 8
    temp = []

    for perm_piece in itertools.permutations(pieces):
        index_r = [i for i, piece in enumerate(perm_piece) if piece == 'r']
        index_k = perm_piece.index('k')
        index_b = [j for j, piece in enumerate(perm_piece) if piece == 'b']

        if not (min(index_r) < index_k < max(index_r)):
            continue
        if len(index_b) != 2 or index_b[0] % 2 == index_b[1] % 2:
            continue
        temp.append(perm_piece)
        set_chess = set(temp)
    chess960_positions = list(set_chess)
    chess960_positions.sort()

    chess_table = []
    for row in range(8):
        if row == 0:
            chess_table.append(" ".join(chess960_positions[n - 1]))
        elif row == 1:
            chess_table.append(" ".join(pawn))
        elif 2 <= row <= 5:
            chess_table.append(" ".join(empty_case))
        elif row == 6:
            chess_table.append(" ".join([p.upper() for p in pawn]))
        elif row == 7:
            chess_table.append(" ".join([p.upper() for p in chess960_positions[n - 1]]))
    #     print("\\n".join(chess_table)+"\\n")

    return "\\n".join(chess_table) + "\\n"



if __name__ == '__main__':
    print("n=1")
    get_chess960_position(1)
    print("n=480")
    get_chess960_position(480)
    print("n=829")
    get_chess960_position(829)
    print("n=960")
    get_chess960_position(960)