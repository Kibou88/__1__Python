from unittest import case


def will_robots_collide(x1, y1, x2, y2, commands):
    if (x1 == x2 and y1 == y2):
        return True

    liste_pos_robot1 = {(x1, y1)}
    temp_pos_robot1 = set()
    liste_pos_robot2 = {(x2, y2)}
    temp_pos_robot2 = set()
    for command in commands:
        if command in ["U", "D"]:
            for position in liste_pos_robot1:
                if 0 <= (position[1] + (1 if command == "U" else -1)) <= 500:
                    new_y = (1 if command == "U" else -1) + position[1]
                    temp_pos_robot1.add((position[0], new_y))
            for position in liste_pos_robot2:
                if 0 <= (position[1] + (1 if command == "U" else -1)) <= 500:
                    new_y = (1 if command == "U" else -1) + position[1]
                    temp_pos_robot2.add((position[0], new_y))

        elif command in ["L", "R"]:
            for position in liste_pos_robot1:
                if 0 <= (position[0] + (1 if command == "L" else -1)) <= 500:
                    new_x = (1 if command == "L" else -1) + position[0]
                    temp_pos_robot1.add((new_x, position[1]))
            for position in liste_pos_robot2:
                if 0 <= (position[0] + (1 if command == "L" else -1)) <= 500:
                    new_x = (1 if command == "L" else -1) + position[0]
                    temp_pos_robot2.add((new_x, position[1]))

        liste_pos_robot1 |= temp_pos_robot1
        liste_pos_robot2 |= temp_pos_robot2

    return True if (liste_pos_robot1 & liste_pos_robot2) else False

if __name__ == '__main__':
    # will_robots_collide(0, 0, 1, 0, "UL")
    print(will_robots_collide(0, 0, 1, 0, "UL"))
    # will_robots_collide(0, 0, 0, 1, 'LRLR')
    print(will_robots_collide(0, 0, 0, 1, 'LRLR'))