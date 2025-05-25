def move_zeros(lst):
    for i in range(lst.count(0)):
        lst.remove(0)
        lst.append(0)
        print(lst)
    return lst


if __name__ == "__main__":
    liste = [1, 0, 1, 2, 0, 1, 3]
    # move_zeros(liste)
    print(move_zeros(liste) == [1, 1, 2, 1, 3, 0, 0])