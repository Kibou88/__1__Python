# --------------------EXO 1-------OK-------------------
def sum_entiers(n):
    if n == 0:
        return 0
    else:
        return n + sum_entiers(n - 1)

print(sum_entiers(5))

# --------------------EXO 2--------NOK------------------
def count_numbers(n):
    if n == 0:
        return 0
    else:
        return 1 + count_numbers(n // 10)
    # Si tu appelles count_numbers(12345), voici comment la fonction se déroule :
    #
    #     1 + count_numbers(1234)
    #     1 + count_numbers(123)
    #     1 + count_numbers(12)
    #     1 + count_numbers(1)
    #     1 + count_numbers(0)
    # Ensuite, les résultats remontent :
    #
    # count_numbers(0) retourne 0
    # count_numbers(1) retourne 1 + 0 = 1
    # count_numbers(12) retourne 1 + 1 = 2
    # count_numbers(123) retourne 1 + 2 = 3
    # count_numbers(1234) retourne 1 + 3 = 4
    # count_numbers(12345) retourne 1 + 4 = 5

print(count_numbers(12345))

# --------------------EXO 3-------OK-------------------
def inverse_character(string):

    if len(string) == 0:
        return ""
    else:
        return string[-1] + inverse_character(string[:-1])

print(inverse_character("Bonjour"))

# --------------------EXO 4-------OK-------------------
def exponentielle(n):

    if n == 0:
        return 1
    else:
        return 2*exponentielle(n-1)

print(exponentielle(3))
