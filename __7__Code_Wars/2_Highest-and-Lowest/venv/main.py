def high_and_low(numbers):
    splitNumbers = numbers.split(" ")
    for number in range(len(splitNumbers)):
        splitNumbers[number] = int(splitNumbers[number])

    return f"{max(splitNumbers)} {min(splitNumbers)}"

if __name__ == "__main__":
    numbers = "1 9 3 4 -5"
    print(high_and_low(numbers))