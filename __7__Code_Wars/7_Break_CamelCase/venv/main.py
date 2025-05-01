def solution(s):
    x = 0
    tableau = []
    for letter in range(len(s)):
        if s[letter].isupper():
            tableau.append(s[x:letter])
            x = letter
        elif (letter + 1)  == len(s):
            tableau.append(s[x:letter + 1])

    return " ".join(tableau)

if __name__ == "__main__":
    # s = "helloWorld"
    s = "breakCamelCase"
    print(solution(s))