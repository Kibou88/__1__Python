# Try-Except
# - Apprendre à utiliser le bloc try-except
###########################################
a = 5
b = "couco"
# b= 10

try:
    resultat = (a/b)

except ZeroDivisionError: # Va gérer si l'erreur ZeroDivisionError remonte
    print("Division par zéro impossible")
except TypeError as e: # Va gérer l'erreur TypeError
    # as e: va permettre de récupérer le message de l'erreur
    print("Erreur:",e)
    print("La variable b n'est pas un int")
except NameError: # Va gérer l'erreur NameError => Problème de nom de variable
    print("La variable b n'est pas défini")

else: # Condition si aucune erreur n'est remontée
    print(resultat)

finally: # Va exécuter le script dessous peu import le résultat du try-except
    print("Fin du bloc")