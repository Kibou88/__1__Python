import heapq

# Exemple de tableau de nombres
nombres = [10, 30, 20, 50, 40]

# Pour utiliser heapq comme un max-heap, nous inversons les valeurs
nombres_inverses = [-x for x in nombres]
heapq.heapify(nombres_inverses)

# Fonction pour extraire le plus grand élément
def extraire_max(heap):
    return -heapq.heappop(heap)

# Insérer un nouvel élément dans le tas
nouvel_element = 25
heapq.heappush(nombres_inverses, -nouvel_element)

# Extraire et imprimer les éléments dans l'ordre décroissant
print("Éléments extraits dans l'ordre décroissant:")
while nombres_inverses:
    print(extraire_max(nombres_inverses))