# Utilisation des Regex
#
# But:
# - Apprendre à utiliser les regex
# ---------------------------------------------------------

import re

with open("data.txt", "r") as f:
    datas = f.read()

print(datas)

# Correction du motif regex pour trouver des nombres à deux chiffres suivis d'un espace
pattern1 = r"[0-9]{2}"

# Appliquer le regex directement sur le contenu complet du fichier
matches1 = re.findall(pattern1, datas)

# Afficher les correspondances trouvées
print(matches1)
