# Fonction pour savoir si l'utilisateur veut jouer ou non
def game_on(partie):
    if partie.lower() == "exit":  # Mets toutes les lettres en minuscules et test si l'utilisateur a tapé "exit"
        print("Au revoir")
        exit()
    elif partie.lower() == "oui":  # Test si l'utilisateur a tapé "oui"
        return 1
    else: # Si aucune commande valide a été tapé
        print("Commande invalide!\n")
        return 0

# Fonction pour deviner une lettre à l'utilisateur
def guess_letter(wordGuessStr, coups, mort):
    print("Voici l'avancer du mot à devenir: ", wordGuessStr)
    print(f"Vous avez fait {coups} plus que {mort - coups} avant la mort!")
    return input("Entrez une lettre: ")