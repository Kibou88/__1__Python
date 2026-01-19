"""
Tables Base de Données
---------------------------
But:
Savoir créer et gérer plusieurs tables dans une même base de données
"""

import sqlite3

# Connexion à la base (créée si inexistante)
conn = sqlite3.connect('ma_base.db')
cur = conn.cursor()

# Table 1: Utilisateurs
cur.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        age INTEGER CHECK (age >= 0)
    )
''')

# Table 2: Produits (différente structure)
cur.execute('''
    CREATE TABLE IF NOT EXISTS produits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT UNIQUE NOT NULL,
        prix REAL CHECK (prix > 0),
        stock INTEGER DEFAULT 0
    )
''')

# Table 3: Commandes (avec clé étrangère pour relation)
cur.execute('''
    CREATE TABLE IF NOT EXISTS commandes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        utilisateur_id INTEGER,
        produit_id INTEGER,
        quantite INTEGER NOT NULL,
        FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs (id),
        FOREIGN KEY (produit_id) REFERENCES produits (id)
    )
''')

# Validation des changements
conn.commit()
print("Tables créées avec succès !")

# Liste 1: utilisateurs
utilisateurs_data = [
    ('Alice Dupont', 28),
    ('Bob Martin', 35),
    ('Clara Leroy', 22),
    ('David Roux', 41)
]

# Liste 2: produits
produits_data = [
    ('Ordinateur Portable', 899.99, 10),
    ('Souris Sans Fil', 25.50, 50),
    ('Clavier Mécanique', 120.00, 15),
    ('Écran 27 pouces', 299.00, 8)
]

# Liste 3: commandes
commandes_data = [
    (1, 1, 2),  # utilisateur 1, produit 1, quantite 2
    (2, 2, 1),  # utilisateur 2, produit 2, quantite 1
    (1, 3, 1),  # utilisateur 1, produit 3, quantite 1
    (3, 4, 1)   # utilisateur 3, produit 4, quantite 1
]

cur.executemany('''
        INSERT INTO utilisateurs (nom, age) 
        VALUES (?, ?)
    ''', utilisateurs_data)

cur.executemany('''
        INSERT INTO produits (nom, prix, stock) 
        VALUES (?, ?, ?)
    ''', produits_data)

cur.executemany('''
        INSERT INTO commandes (utilisateur_id, produit_id, quantite) 
        VALUES (?, ?, ?)
    ''', commandes_data)

conn.commit()
conn.close()
