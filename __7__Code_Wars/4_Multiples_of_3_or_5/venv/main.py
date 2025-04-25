def solution(number):
    """
    Shortest solution
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
    """
    count = 0
    if number < 0:
        return 0
    for i in range(number):
        if not i % 3 and not i % 5:
            count += i
        elif not i % 3:
            count += i
        elif not i % 5:
            count += i
    return count


if __name__ == "__main__":

    # solution(10)
    print(f"Voici la somme {solution(10)}")