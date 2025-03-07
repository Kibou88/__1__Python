# For Else
# - Utilisation de For et Else
#------------------------------

invites = ['Julien', 'Marie', 'Pierre', 'Paul', 'Pascal']

for invite in invites:
    if invite == 'Pascal':
        print("Pascal a deja ete invite")
        break # Sotir de la boucle
else:
    print("Pascal n'as pas ete invite")

print("Instruction suivante")
