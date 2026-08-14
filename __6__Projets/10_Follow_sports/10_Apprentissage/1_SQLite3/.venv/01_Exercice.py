import sqlite3
from datetime import datetime

print("=== GESTIONNAIRE DE TÂCHES ===")

# Étape 1-2: Créer base + table COMPLÈTE
with sqlite3.connect('taches.db') as conn:
    cur = conn.cursor()

    # Table COMPLÈTE avec TOUTES les colonnes
    cur.execute('''
        CREATE TABLE IF NOT EXISTS taches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            description TEXT,
            priorite INTEGER NOT NULL DEFAULT 3 CHECK (priorite BETWEEN 1 AND 5),
            terminee INTEGER NOT NULL DEFAULT 1 CHECK (terminee IN (0, 1)),
            date_creation TEXT
        )
    ''')
    print("✅ Table 'taches' créée/vérifiée.")

    # Étape 3: Insérer 5 tâches d'exemple CORRECTES
    taches = [
        ('Faire courses', 'Pain, lait, fruits', 5, '2026-01-18'),
        ('Ranger bureau', 'Trier papiers', 4, '2026-01-18'),
        ('Python exercices', 'Finir chap SQLite', 2, '2026-01-18'),
        ('Appel client', 'Confirmer rdv', 2, '2026-01-18'),
        ('Lire docs', 'SQLite avancé', 1, '2026-01-18')
    ]

    # AVANT insertion: vider table pour test propre
    cur.execute('DELETE FROM taches')

    cur.executemany('''
        INSERT INTO taches (titre, description, priorite, date_creation) 
        VALUES (?, ?, ?, ?)
    ''', taches)
    conn.commit()
    print("✅ 5 tâches insérées.")

# Étape 4: Afficher TOUTES les tâches (tri priorité DESC, puis titre)
print("\n📋 Tâches par priorité :")
with sqlite3.connect('taches.db') as conn:
    cur = conn.cursor()
    cur.execute('''
        SELECT id, titre, priorite, terminee, date_creation 
        FROM taches 
        ORDER BY priorite DESC, titre
    ''')
    resultats = cur.fetchall()

    for tache in resultats:
        statut = "✓" if tache[3] else "○"
        print(f"ID={tache[0]}: \"{tache[1]}\" (prio {tache[2]}) - {statut} terminée")

# Étape 7: Statistiques
with sqlite3.connect('taches.db') as conn:
    cur = conn.cursor()

    cur.execute('SELECT COUNT(*) FROM taches')
    total = cur.fetchone()[0]

    cur.execute('SELECT COUNT(*) FROM taches WHERE terminee = 1')
    terminees = cur.fetchone()[0]

    cur.execute('SELECT COUNT(*) FROM taches WHERE priorite = 5')
    prio5 = cur.fetchone()[0]

    print(f"\n📊 Stats: Total={total} | Terminées={terminees} | Prio 5={prio5}")

print("\n🎉 Code COMPLET fonctionnel ! Copie-colle et exécute.")
