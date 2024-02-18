# Les listes part 5
# - Comprendre les listes imbriquées
#######################################################
liste = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]
"""
Hiérachie:
\-> Python (indice 0)
|
\-- (indice 1)
| \-> Java (indice 1 - 0)
| |
| \-> C++ (indice 1 - 1)
| |
| \-- (indice 1 - 2)
|   |
|   \-> C (indice 1 - 2 -0)
|
\-- (indice 2)
  |
  \->Ruby (indice 2 - 1)
"""
print(liste[1]) # Affiche la liste dans l'indice 1: Java, C++, [C]
print(liste[1][-1]) # Affiche la liste dans l'indice 1 et le dernier élément: [C]
print(liste[1][-1][0]) # Affiche l'élément: C

print(liste[0][0:2]) # Récupère l'élément 0 et affiche les 2 premiers caractères: Py