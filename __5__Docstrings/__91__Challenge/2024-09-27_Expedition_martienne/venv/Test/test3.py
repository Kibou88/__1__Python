def dijkstra(village, source='blanc'):
    assert all(village[u][v] >= 0 for u in village.keys() for v in village[u].keys())
    precedent = {x:None for x in village.keys()}
    dejaTraite = {x:False for x in village.keys()}
    distance =  {x:float('inf') for x in village.keys()}
    distance[source] = 0
    a_traiter = [(0, source)]
    while a_traiter:
        dist_noeud, noeud = a_traiter.pop()
        if not dejaTraite[noeud]:
            dejaTraite[noeud] = True
            for voisin in village[noeud].keys():
                dist_voisin = dist_noeud + village[noeud][voisin]
                if dist_voisin < distance[voisin]:
                    distance[voisin] = dist_voisin
                    precedent[voisin] = noeud
                    a_traiter.append((dist_voisin, voisin))
        a_traiter.sort(reverse=True)
    return distance, precedent

village={}
village['blanc']={'bleu':3,'jaune':12}
village['bleu']={'blanc':3,'rouge':5,'gris':2}
village['gris']={'bleu':2,'rouge':1}
village['rouge']={'gris':1,'jaune':4}
village['jaune']={'rouge':4,'blanc':12}

distance, precedent = dijkstra(village)
print('Distances minimum :',distance)
print('Liste des précédents :', precedent)