def array_diff(a, b):
    """
    Shortes solution:
    return [x for x in a if x not in b]
    """
    for i in b:
        for j in a:
            if i in a:
                a.remove(i)
    return a


if __name__ == "__main__":
    a = [1, 2, 2, 2, 3]
    b = []

    print(array_diff(a, b))