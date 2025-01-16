# Modifier une liste en itérant dedans
#--------------------------------------

prenoms = ['Pierre', 'Julien', 'Marie', 'Paul']
# for i in range(len(prenoms)):
#     if prenoms[i] == 'Julien':
#         del prenoms[i] # Retourne un IndexError

prenoms2 = [p for p in prenoms if p != 'Julien']
print(prenoms2)

