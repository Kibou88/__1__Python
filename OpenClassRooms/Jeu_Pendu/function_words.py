# Fonction pour choisir un mot aléatoire
def random_words():
    import random
    listOfWords = ['british', "suave", "integrity", "accent", "evil", "genius", "downton"]
    wordsChoiced = random.choice(listOfWords)  # Permet de choisir un mot dans la liste
    return wordsChoiced

# Fonction pour remplacer le mot choisis par des "_"
def hide_words(wordsChoiced):
    wordGuess = []
    for i in wordsChoiced:
        wordGuess.append("_")
    return wordGuess

# Fonction pour convertir le tableau wordGuess en string
def convert_table_str(wordGuess):
    wordGuessStr = ''.join(wordGuess)
    return wordGuessStr

# Fonction pour trouver la (les) position(s) de la lettre écrite par l'utilisateur
def find_letters_word(lettre, wordGuess, wordsChoiced):
    lst = []
    for pos, char in enumerate(wordsChoiced):  # On recherche toutes les lettres correspondantes à la lettre écrite
        if char == lettre:
            lst.append(pos)
            wordGuess[pos] = lettre
    return wordGuess