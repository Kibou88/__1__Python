# constantes.py
# But:
# Contient les constantes du code
# -----------------------------------
# Date de création: 2024-06-08
# Date de dernière modification: 2024-06-16
# ------------------------------------------
# version: 1.0
# -
#-------------------------------------------
import os

DO_VINOS = {
    "Alicante": ((38.3436365, -0.4881708), "Tinto"),
    "Calatayud": ((41.3527628, -1.6422977), "Tinto"),
    "Cariñena": ((41.3382122, -1.2263149), "Tinto"),
    "Condado de Huelva": ((37.3382055, -6.5384658), "Blanco"),
    "Jumilla": ((38.4735408, -1.3285417), "Tinto"),
    "La Gomera": ((28.116, -17.248), "Blanco"),
    "Málaga": ((36.7213028, -4.4216366), "Blanco"),
    "Rías Baixas": ((42.459627886165265, -8.722862824636783), "Blanco"),
    "Ribera del Duero": ((41.49232, -3.005), "Tinto"),
    "Rioja": ((42.29993373411561, -2.486288477690506), "Tinto"),
    "Rueda": ((41.4129785, -4.9597533), "Blanco"),
    "Somontano": ((42.0883878, 0.0994041), "Tinto"),
    "Tarragona": ((41.1172364, 1.2546057), "Tinto"),
    "Txakoli de Getaria": ((43.29428414467608, -2.202397625912913), "Blanco"),
    "Xérès": ((36.6816936, -6.1377402), "Blanco")
}

CURRENT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__))) # Variable pour le répertoire de travail


if __name__ == "__main__":
    print(list(DO_VINOS))
    for i in list(DO_VINOS):
        print(f"Les coordonées de {i} sont {DO_VINOS[i][0]} et le type de vin {DO_VINOS[i][1]}")