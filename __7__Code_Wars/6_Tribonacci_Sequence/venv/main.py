def tribonacci(signature, n):
    if 0 < n < 3:
        return signature[:n]
    elif n >= 3:
        resultat = list(signature)
        for i in range(n-len(signature)):
            resultat.append(sum(resultat[-3::]))
        return resultat
    elif n <= 0 or n != type(int):
        return []

if __name__ == "__main__":

    print(tribonacci([1,1,1], 1))
    print(tribonacci([149, 172, 147], 2))
    print(tribonacci([52, 89, 39], 1))