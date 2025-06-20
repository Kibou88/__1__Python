bishop_movements = []
root_movements = []
queen_movements = []
for i in range(-8, 9):
    if i != 0:
        bishop_movements.append([i, i])
        bishop_movements.append([-i, i])
        root_movements.append([i, 0])
        root_movements.append([0, i])
        queen_movements.append([i, 0])
        queen_movements.append([0, i])
        queen_movements.append([i, i])
        queen_movements.append([-i, i])
print(len(bishop_movements))
print(len(root_movements))
queen_movements.append(bishop_movements)
queen_movements.append(root_movements)
print(queen_movements)