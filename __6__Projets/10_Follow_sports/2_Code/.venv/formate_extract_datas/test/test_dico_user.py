add_seance = {
    "date": "3/1/26",                    # Format dd/mm/aa (flexible)
    "exercices": [                          # Liste d'exercices
        {
            "nom": "squats",                 # lower case validé
            "series": [                      # Liste de séries multiples
                {
                    "series": 5,             # Entier
                    "reps": 10,              # Entier
                    "charge": 60.0           # Float (virgule → point)
                },
                {
                    "series": 3,
                    "reps": 8,
                    "charge": 55.0
                }
            ]
        },
        {
            "nom": "fentes_avant",
            "series": [{"series": 4, "reps": 12, "charge": 20.0}]
        }
    ]
}
