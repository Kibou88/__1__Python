# Module Datetime
# - Apprendre le fonctionnement des classes date, time et datetime
##################################################################
from datetime import date, time, datetime

# date peut prendre les paramètres année mois et jour
print(date(year=2024, month=2, day=17))
# date.today affiche la date du jour format YYYY-MM-DD
print(date.today())

# time prend les paramètres heures, minutes, secondes et µsec
print(time(hour=10, minute=55, second=10, microsecond=500))

# datetime prend les paramètres des 2 autres modules
# datetime.today et datetime.now affiche la date du jour avec heures,minutes,secondes et µsec
print(datetime.today())

now = datetime.now() # Fonctionne aussi avec today()
print(now.hour) # Récupère l'heure qu'il est

# Utiliser la méthode replace pour modifier le temps
# Fonctionne avec today()
tomorrow = now.replace(day=now.day +1) # Remplace le jour actuel par jour + 1
print(tomorrow)