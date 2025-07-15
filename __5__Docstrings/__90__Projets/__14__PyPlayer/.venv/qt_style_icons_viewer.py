import sys
from PySide6 import QtWidgets, QtGui, QtCore

class IconViewer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt StandardPixmap Icons Viewer")
        self.setGeometry(100, 100, 1200, 800)
        
        # Widget central avec scroll area
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QtWidgets.QVBoxLayout(central_widget)
        
        # Barre de recherche
        search_layout = QtWidgets.QHBoxLayout()
        search_label = QtWidgets.QLabel("Rechercher:")
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setPlaceholderText("Tapez pour filtrer les icônes...")
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        main_layout.addLayout(search_layout)
        
        # Scroll area pour les icônes
        scroll_area = QtWidgets.QScrollArea()
        scroll_widget = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout(scroll_widget)
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)
        
        # Obtenir toutes les icônes StandardPixmap
        self.all_icons = self.get_all_standard_pixmaps()
        self.display_icons()
        
        # Connecter la recherche
        self.search_input.textChanged.connect(self.filter_icons)
    
    def get_all_standard_pixmaps(self):
        """Récupère tous les StandardPixmap disponibles"""
        icons = []
        style = self.style()
        
        # Parcourir tous les attributs de QStyle qui commencent par SP_
        for attr_name in dir(QtWidgets.QStyle.StandardPixmap):
            if attr_name.startswith('SP_'):
                try:
                    pixmap_enum = getattr(QtWidgets.QStyle.StandardPixmap, attr_name)
                    icon = style.standardIcon(pixmap_enum)
                    if not icon.isNull():
                        icons.append((attr_name, icon, pixmap_enum))
                except:
                    pass
        
        return sorted(icons, key=lambda x: x[0])
    
    def display_icons(self, filtered_icons=None):
        """Affiche les icônes dans la grille"""
        # Effacer les widgets existants
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)
        
        icons_to_show = filtered_icons if filtered_icons else self.all_icons
        
        cols = 4
        for i, (name, icon, enum_val) in enumerate(icons_to_show):
            row = i // cols
            col = i % cols
            
            # Créer un widget pour chaque icône
            icon_widget = self.create_icon_widget(name, icon, enum_val)
            self.grid_layout.addWidget(icon_widget, row, col)
    
    def create_icon_widget(self, name, icon, enum_val):
        """Crée un widget pour afficher une icône avec son nom"""
        widget = QtWidgets.QFrame()
        widget.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel)
        widget.setFixedSize(280, 120)
        
        layout = QtWidgets.QVBoxLayout(widget)
        
        # Label pour l'icône
        icon_label = QtWidgets.QLabel()
        pixmap = icon.pixmap(48, 48)
        icon_label.setPixmap(pixmap)
        icon_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        # Label pour le nom
        name_label = QtWidgets.QLabel(name)
        name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        name_label.setWordWrap(True)
        name_label.setStyleSheet("font-weight: bold; font-size: 10px;")
        
        # Label pour la valeur enum
        enum_label = QtWidgets.QLabel(f"Valeur: {int(enum_val)}")
        enum_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        enum_label.setStyleSheet("font-size: 8px; color: gray;")
        
        # Bouton pour copier le code
        copy_button = QtWidgets.QPushButton("Copier code")
        copy_button.setStyleSheet("font-size: 8px;")
        copy_button.clicked.connect(lambda: self.copy_code(name))
        
        layout.addWidget(icon_label)
        layout.addWidget(name_label)
        layout.addWidget(enum_label)
        layout.addWidget(copy_button)
        
        return widget
    
    def copy_code(self, icon_name):
        """Copie le code pour utiliser l'icône"""
        code = f"self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.{icon_name})"
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(code)
        
        # Afficher un message de confirmation
        QtWidgets.QMessageBox.information(self, "Copié", f"Code copié:\n{code}")
    
    def filter_icons(self):
        """Filtre les icônes selon le texte de recherche"""
        search_text = self.search_input.text().lower()
        if not search_text:
            self.display_icons()
            return
        
        filtered = [
            (name, icon, enum_val) for name, icon, enum_val in self.all_icons
            if search_text in name.lower()
        ]
        self.display_icons(filtered)

def main():
    app = QtWidgets.QApplication(sys.argv)
    viewer = IconViewer()
    viewer.show()
    
    # Afficher quelques informations utiles
    print("Icônes liées aux drives:")
    for name, _, _ in viewer.all_icons:
        if 'drive' in name.lower() or 'computer' in name.lower():
            print(f"  - {name}")
    
    print("\nIcônes liées aux médias:")
    for name, _, _ in viewer.all_icons:
        if 'media' in name.lower():
            print(f"  - {name}")
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()