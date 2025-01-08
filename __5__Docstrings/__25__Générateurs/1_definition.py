# Définition générateur
# - Apprendre le rôle des générateurs
#--------------------------------------

def exemple_generateur():
    yield 1 # yield équivalent return
    yield 2
    yield 3

generateur = exemple_generateur()
print(type(generateur))
print(next(generateur))
print(next(generateur))
print(next(generateur))

print("\n")
#----------------------------------------------------
def custom_range(n):
    for i in range(1, n + 1):
        yield i

generateur2 = custom_range(10)
for i in generateur2:
    print(i)