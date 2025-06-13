import itertools
chess960_positions = []
temp = []
chess_table = ""
pawn = ["p", "p", "p", "p", "p", "p", "p", "p"]
empty_case = [".", ".", ".", ".", ".", ".", ".", "."]
pieces = ['b', 'b', 'n', 'n', 'q', 'r', 'k', 'r']

for perm_piece in itertools.permutations(pieces):
    index_r = [i for i, piece in enumerate(perm_piece) if piece == 'r']
    index_k = perm_piece.index('k')
    index_b = [j for j, piece in enumerate(perm_piece) if piece == 'b']

    if not (min(index_r) < index_k < max(index_r)):
        continue
    if len(index_b) != 2 or index_b[0] % 2 == index_b[1] % 2:
        continue
    temp.append(perm_piece)

# print(len(set(chess960_positions))) 960 positions en enlevant les doublons
set_chess = set(temp)
chess960_positions = list(set_chess)
# print(len(chess960_positions)) 960 positions
print(chess960_positions[-1])
chess960_positions.sort()
print(chess960_positions[0])

chess_table = []
for row in range(8):
    if row == 0:
        chess_table.append(" ".join(chess960_positions[-1]))
    elif row == 1:
        chess_table.append(" ".join(pawn))
    elif 2 <= row <= 5:
        chess_table.append(" ".join(empty_case))
    elif row == 6:
        chess_table.append(" ".join(pawn).upper())
    elif row == 7:
        chess_table.append(" ".join(chess960_positions[-1]).upper())
print("\\n".join(chess_table)+"\\n")