def narcissistic(value):
    """
    Shortest solution:
    return value == sum(int(x) ** len(str(value)) for x in str(value))
    """
    somme = 0
    for j in [i for i in str(value)]:
        somme += int(j) ** len([i for i in str(value)])
    if somme == value:
        return True
    else:
        return False

if __name__ == "__main__":

    value = 1654
    print(narcissistic(value))