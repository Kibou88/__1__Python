"""
Creation Bae de Données
---------------------------
But:
Premier pas avec SQLite3
Création d'une bade de données avec lecture
"""

import sqlite3  # Import standard

# Étape 1: Connexion (crée 'bibliotheque.db')
with sqlite3.connect('bibliotheque.db') as conn:  # Context manager auto-ferme
    cur = conn.cursor()

    # Étape 2: Créer table si inexistante
    cur.execute('''
        CREATE TABLE IF NOT EXISTS liste_livres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            auteur TEXT NOT NULL,
            annee INTEGER
        )
    ''')  # Types basiques : INTEGER, TEXT
    print("Table 'livres' créée ou vérifiée.")

    # Étape 3: Insérer des données avec placeholders (sécurisé)
    livres = [
        ('1984', 'George Orwell', 1949),
        ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943),
        ('Dune', 'Frank Herbert', 1965)
    ]
    # INSERT INTO livres (id, titre, auteur, annee) VALUES(titre, auteur, annee), liste(livres)
    cur.executemany('INSERT INTO liste_livres (titre, auteur, annee) VALUES (?, ?, ?)', livres)
    conn.commit()  # Sauvegarde obligatoire !
    print("3 livres insérés.")

# Étape 4: Lire des données (nouvelle connexion)
with sqlite3.connect('bibliotheque.db') as conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM liste_livres ORDER BY annee')
    resultats = cur.fetchall()
    print(resultats)
    for livre in resultats:
        print(f"ID: {livre[0]}, Titre: {livre[1]}, Auteur: {livre[2]}, Année: {livre[3]}")
