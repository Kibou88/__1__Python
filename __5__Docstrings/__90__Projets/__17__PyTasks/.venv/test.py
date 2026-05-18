import numpy as np
import matplotlib.pyplot as plt

# Paramètres
R = 1000          # en ohms
C = 10e-6         # en farads (10 microfarads)
U = 5             # tension d'alimentation en volts
tau = R * C       # constante de temps en secondes

# Temps de simulation : de 0 à 5 tau
t = np.linspace(0, 5*tau, 1000)

# Calcul de la tension aux bornes du condensateur
uC = U * (1 - np.exp(-t / tau))

# Trace
plt.plot(t*1000, uC)  # t*1000 pour afficher en millisecondes
plt.title("Charge d'un condensateur dans un circuit RC")
plt.xlabel("Temps (ms)")
plt.ylabel("Tension aux bornes du condensateur (V)")
plt.grid(True)
plt.show()
