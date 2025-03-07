# Test condition if, elif, else
# - Utilisation de if, elif, else, and, or, not
###############################################

a = 1
b = 2
c = 3
d = 3

if a == 1: # Test vrai
    print("a est bien égal à 1")

if a == 1 and b == 2: # Test vrai
    print("a = 1 et b = 2")

if a == 2: # Test faux
    print("Test faux")
elif a == 2 or c == 3: # Test vrai
    print("a et/ou b sont égales à 2")
else:
    print("ni a ni b est égale à 2")

if not a == 2: #Test vrai
    print("Si a n'est pas égale à 2")
    if b != 1: #Test vrai
        print("Si b est différent de 1")
        if a == 1 and (b==2 or d == 3): #Test vrai
            print("Si b=2 OU d=3, PUIS ET a=1")
