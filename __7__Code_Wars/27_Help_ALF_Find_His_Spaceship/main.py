def find_spaceship(astromap):
    if not "\n" in astromap:
        if "X" in astromap:
            return [astromap.index("X"), 0]
        return "Spaceship lost forever."

    # elif astromap.count("\n") >= 1:
    map = astromap.split("\n")
    map.reverse()
    for row in range(0,len(map)):
        for column in range(len(map[row])):
            if map[row][column] == "X":
                return [column, row]
    return "Spaceship lost forever."

if __name__ == '__main__':
    astromap = "X\n."
    # print(astromap.split('\n'))
    print(find_spaceship(astromap))