def two_sum(numbers, target):
    for index, number in enumerate(numbers):
        for i, j in enumerate(range(len(numbers) - 1), (index + 1)):
            print(i)
            if i > (len(numbers) - 1):
                break
            if (numbers[index] + numbers[i]) == target:
                return (index, i)

if __name__ == "__main__":

    tests = [[[1, 2, 3], 4], [[3, 2, 4], 6]]
    for test in tests:
        print(two_sum(test[0], test[1]))