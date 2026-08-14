"""
Extract Base de Données
---------------------------
But:
Extraire les données d'une table et les afficher
"""
import sqlite3

# Étape 1: Connexion (crée 'bibliotheque.db')
with sqlite3.connect('tests.db') as conn:  # Context manager auto-ferme
    cur = conn.cursor()

    # Voir toutes les tables présentes dans la DB
    # cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    # Filtrer la table sqlite_sequence: mémorise l'autoincrément
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = cur.fetchall()
    print("Tables de la bd: ", tables)


    # Récupérer les colonnes d'une table
    for table in tables:
        print(table[0])
        cur.execute(f"PRAGMA table_info({table[0]})")
        table_colonnes = cur.fetchall()
        print("Colonne: ", table_colonnes)
        # output pour la table seances:
        # Colonne:  [(0, 'id', 'INTEGER', 0, None, 1), (1, 'date', 'TEXT', 1, None, 0), (2, 'exercices', 'TEXT', 1, None, 0)]
        # 0: Numéro de la colonne
        # 1: Nom de la colonne
        # 2: Type de la colonne
        # 3: 1 si la colonne ne peut pas être NOT NULL, sinon 0
        # 4: valeur par défaut(default value) (NONE: aucune valeur par défaut)
        # 5: pk à 1 veut dire que c'est la clé primaire, sinon 0

    # Récupère la dernière ligne
    cur.execute('SELECT * FROM seances ORDER BY id DESC LIMIT 1')
    last_ligne = cur.fetchall()
    print("Ligne: ", last_ligne)
    # Output: Ligne:  [(4, '17/06/2026', 'fentes_avant')]

    # cur.execute('SELECT * FROM seances ORDER BY id')
    # resultats_seances = cur.fetchall()
    #
    # print(resultats_seances)
    # for ligne in resultats_seances:
    #     print(f"id {ligne[0]}, date {ligne[1]}, exercices {ligne[2]}")