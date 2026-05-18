def factorielle(n):
    # Cas de base
    if n == 0:
        return 1
    # Cas récursif
    else:
        return n * factorielle(n - 1)

print(factorielle(5))