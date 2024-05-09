import string
compteur=0
phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
phrase_lower=phrase.lower()
print(string.ascii_lowercase)
resultat = 0
for i in string.ascii_lowercase:
    if i in phrase_lower:
        compteur += 1
        print(i, compteur)
if compteur == 26:
    resultat = "La phrase est un Pangramme"
print(resultat)