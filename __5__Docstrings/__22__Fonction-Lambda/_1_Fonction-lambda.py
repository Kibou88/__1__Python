# Fonction Lambda
# - Apprendre à utiliser les fonctions Lambda
#############################################

# def multiplication(a,b):
#     return a*b

"""
On stocke le résultat de lambda dans une variable (multiplication)
Forme:
lambda argument: expression
"""
multiplication = lambda a, b: a * b
resultat = multiplication(5,10)
print(resultat)

"""
Il est possible de printer avec une fonction lambda
/!\Valable depuis la version 3 de Python /!\
"""
print_bonjour = lambda x: print(x)
print_bonjour('Python')