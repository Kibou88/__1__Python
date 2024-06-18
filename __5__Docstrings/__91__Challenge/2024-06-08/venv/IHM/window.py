    # window.py
    # But:
    # Contient le code du challenge
    # -----------------------------------
    # Date de création: 2024-06-08
    # Date de dernière modification: 2024-06-18
    # ------------------------------------------------------------------------------------------------
    # version: 2.0
    # - Importation du module complet tkintermapview + modif associé
    # - Ajout et modification des coordonées GPS dans la partie "Constantes classe"
    # - Ajout d'une constante "SPACING" permettant de faire les espaces entre chaque bouton + modif associé
    # - Modification du zoom initial afin de voir tous les markers
    # - Méthode "set_marker": ajout du ternaire dans "icon=" pour simplifier le code
    #-------------------------------------------------------------------------------------------------

    # Appel des modules externes
    from tkinter import ttk, Tk
    from tkintermapview import TkinterMapView
    import os
    from PIL import Image, ImageTk

    # Appel des modules internes
    from constantes import DO_VINOS, CURRENT_PATH

    class MainWindow(Tk):
        """
        Classe MainWindow:
        Permet de définir toutes les caractéristiques de la fenêtre d'application
        Hérite de la classe Tk

        3 méthodes:
         - set_marker: Pour la gestion des marqueurs sur la carte
         - set_coordonnees: Pour gérer le centre de la carte avec la ville sélectionnée
         - set_button: Pour gérer la création des boutons
        :param
        - Tk: Permet à MainWindow d'hériter de la classe Tk
        """
        # Constantes de la classe
        POS_ROW = 10
        POS_COLUMN = 25
        WIDTH = 130
        SPACING = 45
            # Coordonnées GPS pour centrer la carte afin de voir tous les markers
        POS_X = 38.4472452
        POS_Y = -4.9252987

        def __init__(self):
            super().__init__()
            # Windows options
            self.title(f"VINOS IBEROS")
            self.configure(bg="purple")
            self.geometry('1000x700')

            # create map widget
            self.map_widget = TkinterMapView(self, width=745, height=650, corner_radius=0)
            # set current widget position and zoom
            self.map_widget.set_position(self.POS_X, self.POS_Y)  # Carte centrer pour faire apparaitre tous les markers
            self.map_widget.set_zoom(5)
            self.map_widget.place(x=230, y=25)

            # Style options
            self.style = ttk.Style(self)
            # Configure le style des boutons
            self.style.configure('TButton',
                font=('Helvitica', 10),
                bd=10,
                foreground="#FFCC00",
                bg="#FFFF33",
                activebackground="blue",
                padding=5)


        def set_marker(self):
            """
            Méthode pour afficher le type de vin en fonction de la ville
            :return: Images (vin blanc ou rouge) sur les coordonnées GPS de la ville en fonction des valeurs du dictionnaires
            """
            blanco = ImageTk.PhotoImage(Image.open(os.path.join(CURRENT_PATH, "images", "blanco.webp")).resize((40, 40)))
            tinto = ImageTk.PhotoImage(Image.open(os.path.join(CURRENT_PATH, "images", "tinto.webp")).resize((40, 40)))
            for i in list(DO_VINOS):
                self.map_widget.set_marker(DO_VINOS[i][0][0], DO_VINOS[i][0][1],
                                           icon=(tinto if DO_VINOS[i][1].lower() == "tinto" else blanco))

        def set_coordonnees(self, i):
            """
            Méthode pour centrer la carte sur la ville en fonction des coordonnées
            :param i: Récupère le nom de la ville de la méthode set_button
            :return: Permet de centrer la carte sur la ville sélectionnée
            """
            self.POS_X = DO_VINOS[i][0][0]
            self.POS_Y = DO_VINOS[i][0][1]
            self.map_widget.set_position(self.POS_X, self.POS_Y)  # Centrer sur la ville sélectionnée
            self.map_widget.set_zoom(8) # Permet de faire un zoom sur la ville sélectionnée

        def set_button(self):
            """
            Méthode pour la création des boutons
            :return: Créer tout les boutons du dictionnaire.
            Action des boutons: Centrer la carte sur la ville sélectionnée
            """
            for i in list(DO_VINOS):
                # Création de tout les boutons pour quitter la fenêtre avec position dans la grille
                self.button = ttk.Button(self, text=i, command=lambda i=i:self.set_coordonnees(i))
                self.button.place(x=self.POS_COLUMN, y=self.POS_ROW, width=self.WIDTH, height=40)
                self.POS_ROW += self.SPACING


    if __name__ == "__main__":
        main_window = MainWindow() # Créer l'instance main_window
        main_window.set_marker() # Appel de la méthode pout afficher le type de vin en fonction de la ville
        main_window.set_button() # Appel de la méthode pour créer et gérer les boutons
        main_window.mainloop()  # Affiche la fenêtre