# main.py
# But:
# Contient la logique du code
# -----------------------------------
# Date de création: 2024-09-27
# Date de dernière modification: 2024-10-24
# ------------------------------------------
# version: 3.0
# - Suppression de l'arrondit à 10^3 (V2)
# - Modification "return list_nodes" par "return list_nodes.reverse()" (V2)
# - Fonction "shortest_distance" suppresion des ".keys()" non nécessaire (V2)
# - Fonction "convert_list_dico" simplificatio avec setdefault (V2)
# - Amélioration efficience des messages en 1 print (V2)
# - Rajoute des types hinting (V3)
#-----------------------------------------------------------------------------------

# Appel des modules internes
from ressources_mars import POINTS_DEPART, POINTS_ARRIVEE, DISTANCES_DES_LIAISONS


def convert_list_dico(distances_liaisons: list) -> dict:
    """
    Fonction pour convertir la table en dico
    :param distances_liaisons (lst): Liste de distance entre 2 points
    :return:
    - dico (dict): Dico de chaque point avec leur voisin et les distances associées
    """
    dico = {}

    for (node1, node2), distance in distances_liaisons:
        dico.setdefault(node1, {})[node2] = distance
        dico.setdefault(node2, {})[node1] = distance

    return dico

def shortest_distance(dico_distance: dict, depart: str) -> dict:
    """
    Fonction pour déterminer la distance la plus courte pour chaque point
    :param dico_distance (dict): Dictionnaire des différents points à passer
    :param depart (str): Point de départ
    :return:
    - distance (dict): Dictionnaire pour la distance totale du point de départ pour chaque point
    - previous_nodes (dict): Dictionnaire affichant le point le plus court (valeur) par rapport au point actuel (clé)
    """
    previous_nodes = {node: None for node in dico_distance}
    visited = {x:False for x in dico_distance}
    distance = {x:float('inf') for x in dico_distance}

    distance[depart] = 0
    current_node = [(0, depart)]

    while current_node:

        node_distance, node = current_node.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in dico_distance[node]:
                neighbor_distance = node_distance + dico_distance[node][neighbor]
                if neighbor_distance < distance[neighbor]:
                    distance[neighbor] = neighbor_distance
                    previous_nodes[neighbor] = node
                    current_node.append((neighbor_distance, neighbor))
        current_node.sort(reverse=True)

    return distance, previous_nodes

def recap_point(previous_node: dict, depart: str, arrivee: str) -> list:
    """
    Fonction pour retrouver les noeuds composant le chemin le plus court
    :param previous_node (dict): dictionnaire contenant tout les noeuds et leur distance
    :param depart (str): Noeud de départ
    :param arrivee (str): Noeud d'arrivée
    :return:
    - list_nodes (list): Liste des noeuds du point de départ à l'arrivée
    """
    list_nodes = [arrivee]
    node = arrivee

    while node != depart:
        node = previous_node[node]
        list_nodes.append(node)

    return list(reversed(list_nodes))


if __name__ == '__main__':
    save_distance = {} # Enregistre le point de départ (key) et la distance jusqu'à Z (value)
    messages = []

    for depart in POINTS_DEPART:

        dico_distance = convert_list_dico(DISTANCES_DES_LIAISONS)
        distance, precedent = shortest_distance(dico_distance, depart)
        list_nodes = recap_point(precedent, depart, POINTS_ARRIVEE)
        messages.append(f"Liste du chemin le plus court de {depart} à {POINTS_ARRIVEE}:")
        messages.append(
            f"\033[0;31m{list_nodes} pour une distance totale de {distance[POINTS_ARRIVEE]} kms\033[0m\n")
        save_distance[depart] = distance[POINTS_ARRIVEE]

    messages.append(f"\033[0;32m\nLe site d'atterrissage recommandé est" \
                    f" {min(save_distance, key=save_distance.get)}\033[0m")

    print("\n".join(messages))