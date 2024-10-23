DISTANCES_DES_LIAISONS = (
    (('A', 'G'), 687),
    (('G', 'F'), 1111),
    (('G', 'H'), 932),
    (('G', 'W'), 2503),
    (('H', 'C'), 3000),
    (('F', 'O'), 1426),
    (('O', 'W'), 786),
    (('H', 'X'), 2121),
    (('X', 'W'), 1325),
)

def convert_list_dico(DISTANCES_DES_LIAISONS):
    dico = {}

    for (node1, node2), distance in DISTANCES_DES_LIAISONS:
        if node1 not in dico:
            dico[node1] = {}
        if node2 not in dico:
            dico[node2] = {}

        dico[node1][node2] = distance
        dico[node2][node1] = distance

    return dico

def shortest_distance(dico_distance, depart):
    """
    Fonction pour déterminer la distance la plus courte pour chaque point
    :param dico_distance (dict): Dictionnaire des différents points à passer
    :param depart (str): Point de départ
    :return:
    - distance(dict): Dictionnaire pour la distance totale du point de départ pour chaque point
    - previous_nodes(dict): Dictionnaire affichant le point le plus court (valeur) par rapport au point actuel (clé)
    """
    previous_nodes = {node: None for node in dico_distance.keys()}
    visited = {x:False for x in dico_distance.keys()}
    distance = {x:float('inf') for x in dico_distance.keys()}

    distance[depart] = 0
    current_node = [(0, depart)]

    while current_node:

        node_distance, node = current_node.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in dico_distance[node].keys():
                neighbor_distance = node_distance + dico_distance[node][neighbor]
                if neighbor_distance < distance[neighbor]:
                    distance[neighbor] = neighbor_distance
                    previous_nodes[neighbor] = node
                    current_node.append((neighbor_distance, neighbor))
        current_node.sort(reverse=True)

    # Arrondit les valeurs à 10^3
    distance = {key: round(value / 1000) for key, value in distance.items()}

    return distance, previous_nodes

def recap_point(previous_node, depart, arrivee):
    list_nodes = [arrivee]
    node = arrivee

    while node != depart:
        node = previous_node[node]
        list_nodes.append(node)

    list_nodes.reverse()
    return list_nodes


if __name__ == '__main__':
    depart = 'A'
    arrivee = 'W'
    dico_distance = convert_list_dico(DISTANCES_DES_LIAISONS)
    distance, precedent = shortest_distance(dico_distance, depart)
    print("Distance minimum:", distance)
    print("Liste des précédents:", precedent)
    list_nodes = recap_point(precedent, depart, arrivee)
    print(f"Liste du chemin le plus court de {depart} à {arrivee}: ")
    print(f"{list_nodes} pour une distance totale de {distance[arrivee]} kms")