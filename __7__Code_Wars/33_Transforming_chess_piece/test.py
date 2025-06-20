board = [['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', 'B', '.'],
          ['.', '.', '.', '.', 'N', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', 'R', '.', '.', '.'],
          ['.', 'K', '.', 'P', '.', '.', '.', '.'],
          ['Q', '.', '.', '.', '.', '.', '.', '.']]
piece = "P"
liste_piece = []
liste_position_piece = []
no_piece_around = False
knight_movements = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
king_movements = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]
pawn_movements = [(-1, -1), (-1, 1)]
root_movements = []
bishops_movements = []
queen_movements = []

for i in range(-8, 9):  # Initialization bishop, root and queen movements
    if i != 0:
        bishops_movements.append([i, i])
        bishops_movements.append([-i, i])
        root_movements.append([i, 0])
        root_movements.append([0, i])
        queen_movements.append([i, 0])
        queen_movements.append([0, i])
        queen_movements.append([i, i])
        queen_movements.append([-i, i])

for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] != ".":
            liste_piece.append(board[row][col])
            liste_position_piece.append((row, col))
print(liste_piece)
print(liste_position_piece)

while not (no_piece_around):
    if piece == 'N':
        for knight_movement in knight_movements:
            knight_x = knight_movement[0] + liste_position_piece[liste_piece.index(piece)][0]
            knight_y = knight_movement[1] + liste_position_piece[liste_piece.index(piece)][1]
            if (knight_x, knight_y) in liste_position_piece:
                liste_position_piece.pop(liste_piece.index(piece))  # retrait de la position de la pièce
                liste_piece.remove(piece)  # retrait de la pièce
                piece = liste_piece[liste_position_piece.index((knight_x, knight_y))]
                break
        if piece == "N":
            no_piece_around = True
    elif piece == 'K':
        for king_movement in king_movements:
            king_x = king_movement[0] + liste_position_piece[liste_piece.index(piece)][0]
            king_y = king_movement[1] + liste_position_piece[liste_piece.index(piece)][1]
            if (king_x, king_y) in liste_position_piece:
                liste_position_piece.pop(liste_piece.index(piece))  # retrait de la position de la pièce
                liste_piece.remove(piece)  # retrait de la pièce
                piece = liste_piece[liste_position_piece.index((king_x, king_y))]
                break
        if piece == "K":
            no_piece_around = True
    elif piece == 'P':
        for pawn_movement in pawn_movements:
            pawn_x = pawn_movement[0] + liste_position_piece[liste_piece.index(piece)][0]
            pawn_y = pawn_movement[1] + liste_position_piece[liste_piece.index(piece)][1]
            if (pawn_x, pawn_y) in liste_position_piece:
                liste_position_piece.pop(liste_piece.index(piece))  # retrait de la position de la pièce
                liste_piece.remove(piece)  # retrait de la pièce
                piece = liste_piece[liste_position_piece.index((pawn_x, pawn_y))]
                break
        if piece == "P":
            no_piece_around = True
    elif piece == 'R':
        for root_movement in root_movements:
            root_x = root_movement[0] + liste_position_piece[liste_piece.index(piece)][0]
            root_y = root_movement[1] + liste_position_piece[liste_piece.index(piece)][1]
            if (root_x, root_y) in liste_position_piece:
                liste_position_piece.pop(liste_piece.index(piece))  # retrait de la position de la pièce
                liste_piece.remove(piece)  # retrait de la pièce
                piece = liste_piece[liste_position_piece.index((root_x, root_y))]
                break
        if piece == "R":
            no_piece_around = True
    elif piece == 'B':
        for bishops_movement in bishops_movements:
            bishop_x = bishops_movement[0] + liste_position_piece[liste_piece.index(piece)][0]
            bishop_y = bishops_movement[1] + liste_position_piece[liste_piece.index(piece)][1]
            if (bishop_x, bishop_y) in liste_position_piece:
                liste_position_piece.pop(liste_piece.index(piece))  # retrait de la position de la pièce
                liste_piece.remove(piece)  # retrait de la pièce
                piece = liste_piece[liste_position_piece.index((bishop_x, bishop_y))]
                break
        if piece == "B":
            no_piece_around = True
    elif piece == 'Q':
        for queen_movement in queen_movements:
            queen_x = queen_movement[0] + liste_position_piece[liste_piece.index(piece)][0]
            queen_y = queen_movement[1] + liste_position_piece[liste_piece.index(piece)][1]
            if (queen_x, queen_y) in liste_position_piece and len(liste_position_piece) >= 3:
                liste_position_piece.pop(liste_piece.index(piece))  # retrait de la position de la pièce
                liste_piece.remove(piece)  # retrait de la pièce
                piece = liste_piece[liste_position_piece.index((queen_x, queen_y))]
                print("new piece: ", piece)
                break
            elif (queen_x, queen_y) in liste_position_piece and len(liste_position_piece) <= 2:
                # liste_position_piece.pop(liste_piece.index(piece))  # retrait de la position de la pièce
                liste_piece.pop(liste_position_piece.index((queen_x, queen_y)))  # retrait de la pièce
                print(liste_position_piece.index((queen_x, queen_y)))
                # piece = "Q"
                # break
        if piece == "Q":
            no_piece_around = True


liste_piece.sort()

print("fin de la boucle")
print(liste_piece)