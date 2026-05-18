def fibonacci(n):
    # Cas de base
    if n <= 1:
        return n
    # Cas récursif
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))