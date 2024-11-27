import re

chiffre_ligne = []
nombres = []
total = 0

path_1 = "/home/kibou/Bureau/Python/__1__Python/__5__Docstrings/__92__Advent_of_Code/2023/AOC_2023/.venv/data_input/1.txt"
path_test = "/home/kibou/Bureau/Python/__1__Python/__5__Docstrings/__92__Advent_of_Code/2023/AOC_2023/.venv/data_input/test.txt"
path_test2 = "/home/kibou/Bureau/Python/__1__Python/__5__Docstrings/__92__Advent_of_Code/2023/AOC_2023/.venv/data_input/test2.txt"

dico = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

# Fonction pour convertir les mots en chiffres
def convert_words_to_digits(line):
    # Utiliser une expression régulière pour trouver tous les mots et chiffres
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    matches = re.findall(pattern, line)
    return matches

# Fonction pour obtenir le premier et le dernier chiffre d'une ligne
def get_first_and_last_digit(line):
    matches = convert_words_to_digits(line)
    first_digit = dico.get(matches[0], matches[0])
    last_digit = dico.get(matches[-1], matches[-1])
    return int(first_digit + last_digit)


with open(path_1, 'r') as file:
    contenu = file.read().splitlines()
print(contenu)

total_sum = sum(get_first_and_last_digit(line) for line in contenu)
print(total_sum)