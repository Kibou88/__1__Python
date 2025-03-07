# Definition opérateurs ternaires
# - Apprendre le rôle des opérateurs ternaires
#-----------------------------------------------
age = 18

if age >= 18:
    print("Vous etes majeur")
else:
    print("Vous etes mineur")

# Opérateur ternaire

print("Vous etes majeur") if age >= 18 else print("Vous etes mineur")

#---------------------------------------------------------------------
test = None

if age >= 18:
    test = True
else:
    test = False
print(test)

test = True if age >= 18 else False
print(test)

#---------------------------------------------------------------------
objet = 1
print(f"Il y a {objet} objet{'s' if objet > 1 else ''}")
objet = 2
print(f"Il y a {objet} objet{'s' if objet > 1 else ''}")