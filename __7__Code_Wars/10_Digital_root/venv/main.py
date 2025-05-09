def digital_root(n: int) -> int:
    while (len(str(n)) >= 2):
        n = str(sum([int(i) for i in str(n)]))
    return int(n)


if __name__ == "__main__":

    n = 493193

    print(digital_root(n))