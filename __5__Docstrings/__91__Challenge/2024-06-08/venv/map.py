# map.py
# But:
# Contient le code pour faire la carte intéractive
# -----------------------------------
# Date de création: 2024-06-08
# Date de dernière modification: 2024-06-08
# ------------------------------------------
# version: 1.0
# -
#-------------------------------------------
import folium
import webbrowser

#Position [latitude, longitude] sur laquelle est centrée la carte
location = [40, -3.7] # Centré sur Madrid

lieu = [38.3436365, -0.4881708]
#Niveau de zoom initial :
#3-4 pour un continent, 5-6 pour un pays, 11-12 pour une ville
zoom = 6

#Style de la carte
# tiles = 'cartodbpositron'

Carte = folium.Map(location = location,
                   zoom_start = zoom)
folium.Marker(
        location=lieu,
        popup="Alicante",
        icon=folium.Icon(color='green')
        ).add_to(Carte)
Carte.save('map.html')

webbrowser.open('map.html')



if __name__ == "__main__":
    pass