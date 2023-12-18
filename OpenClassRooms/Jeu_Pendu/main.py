from start_game import *
from game import *
from function_words import *

while True:
    partie = welcome_game() # Affiche le message de bienvenue et renvoie ce qu'à marquer l'utilisateur
    coups, mort = initialize_counter() # Mets les valeurs des compteurs par défaut

    game = game_on(partie) # Fonction pour savoir si l'utilisateur veut jouer ou non

    if game == 1:
        wordsChoiced = random_words()
        wordGuess = hide_words(wordsChoiced)
        wordGuessStr = convert_table_str(wordGuess)

        while coups < mort and wordGuessStr != wordsChoiced:
            wordGuessStr = convert_table_str(wordGuess)
            lettre = guess_letter(wordGuessStr, coups, mort) # Fonction pour faire deviner une lettre à l'utilisateur
            lst = []
            wordGuess = find_letters_word(lettre, wordGuess, wordsChoiced)
            if not lettre in wordsChoiced:
                coups += 1

        if coups == mort:
            print("Vous avez perdu\n\n")
        elif wordsChoiced == wordGuessStr:
            print(f"Vous avez trouvés le mot {wordGuessStr} en {coups} coups!! Bravo\n\n")
    else:
        break