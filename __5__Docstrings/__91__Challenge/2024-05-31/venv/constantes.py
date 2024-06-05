# constantes.py
# But:
# Contient les constantes du code
# -----------------------------------
# Date de création: 2024-06-01
# Date de dernière modification: 2024-06-02
# ------------------------------------------
# version: 2.0
# - Changed LISTE_ELEVES from list type to tuple type
# - Added EOR
#-------------------------------------------

LISTE_ELEVES = (
    ("Tao", (18, 12, 3, 5, 19)),
    ("Josette", (20, 2, 12, 18, 14)),
    ("Patrick", (2, 4, 6, 18, 17)),
    ("Pema", (3, 19, 15, 3, 12)),
    ("Jean", (0, 9, 8, 8, 4)),
    ("Bixente", (14, 20, 10, 12, 4)),
    ("Paco", (16, 1, 1, 1, 20)),
    ("Chuluun", (15, 6, 17, 20, 15)),
    ("Marie", (16, 4, 16, 20, 12)),
    ("Mohamed", (16, 19, 17, 6, 20))
)

EOR = "\n"

"""
Tao     -> 18, 12, 3, 5, 19
Josette -> 20, 2, 12, 18, 14
Patrick -> 2, 4, 6, 18, 17
Pema    -> 3, 19, 15, 3, 12
Jean    -> 0, 9, 8, 8, 4
Bixente -> 14, 20, 10, 12, 4
Paco    -> 16, 1, 1, 1, 20
Chuluun -> 15, 6, 17, 20, 15
Marie   -> 16, 4, 16, 20, 12
Mohamed -> 16, 19, 17, 6, 20
"""

if __name__ == "__main__":
    print(LISTE_ELEVES(0))