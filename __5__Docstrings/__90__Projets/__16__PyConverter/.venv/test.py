import keyboard

def ma_fonction_callback(event):
    print(f"Touche pressée: {event.name}")

# On "enregistre" la fonction pour qu'elle soit appelée à chaque pression
keyboard.on_press(ma_fonction_callback)

# On garde le programme en vie pour écouter les événements
keyboard.wait()  # Attend qu'on appuie sur une touche spécifique pour arrêter


