import sys
import os
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QStandardPaths

from misc.logs import Logs

class AppContext:
    """
    Classe de contexte d'application remplaçant ApplicationContext de fbs
    Gère les ressources, chemins et cache des icônes
    """
    
    def __init__(self):
        
        self.logs = Logs(application_name="AppContext")
        # Initialiser l'application Qt si pas déjà fait
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QApplication.instance()
            
        # Cache pour les icônes et ressources
        self._icon_cache = {}
        self._resource_cache = {}
        
        # Définir les chemins de base
        self._setup_paths()
    
    def _setup_paths(self):
        """Configure les chemins vers les ressources"""
        # Chemin du script principal
        if getattr(sys, 'frozen', False):
            # Si l'app est "gelée" (empaquetée)
            self.app_dir = Path(sys.executable).parent
        else:
            # En développement
            self.app_dir = Path(__file__).parent
            
        # Dossiers de ressources
        self.resources_dir = self.app_dir / "resources"
        self.icons_dir = self.resources_dir / "icons"
        self.images_dir = self.resources_dir / "images"
        
        # Créer les dossiers s'ils n'existent pas
        self.resources_dir.mkdir(exist_ok=True)
        self.icons_dir.mkdir(exist_ok=True)
        self.images_dir.mkdir(exist_ok=True)
    
    def get_resource_path(self, relative_path):
        """
        Retourne le chemin absolu vers une ressource
        
        Args:
            relative_path (str): Chemin relatif depuis le dossier resources
            
        Returns:
            str: Chemin absolu vers la ressource
        """
        full_path = self.resources_dir / relative_path
        if full_path.exists():
            return str(full_path)
        else:
            self.logs.log_error(f"Attention: Ressource introuvable: {full_path}")
            return str(full_path)  # Retourner quand même le chemin
    
    def get_icon(self, icon_name, cache=True):
        """
        Récupère une icône avec mise en cache optionnelle
        
        Args:
            icon_name (str): Nom du fichier d'icône (avec ou sans extension)
            cache (bool): Utiliser le cache ou non
            
        Returns:
            QIcon: L'icône chargée
        """
        # Ajouter l'extension si elle n'est pas présente
        if not any(icon_name.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.svg', '.ico']):
            # Chercher le fichier avec différentes extensions
            for ext in ['.png', '.svg', '.ico', '.jpg']:
                if (self.icons_dir / (icon_name + ext)).exists():
                    icon_name = icon_name + ext
                    break
        
        # Vérifier le cache
        if cache and icon_name in self._icon_cache:
            return self._icon_cache[icon_name]
        
        # Chemin complet vers l'icône
        icon_path = self.icons_dir / icon_name
        
        if icon_path.exists():
            icon = QIcon(str(icon_path))
            
            # Mettre en cache si demandé
            if cache:
                self._icon_cache[icon_name] = icon
                
            return icon
        else:
            self.logs.log_error(f"Attention: Icône introuvable: {icon_path}")
            # Retourner une icône vide plutôt que None
            return QIcon()
    
    def get_pixmap(self, image_name, cache=True):
        """
        Récupère un pixmap avec mise en cache optionnelle
        
        Args:
            image_name (str): Nom du fichier image
            cache (bool): Utiliser le cache ou non
            
        Returns:
            QPixmap: L'image chargée
        """
        cache_key = f"pixmap_{image_name}"
        
        if cache and cache_key in self._resource_cache:
            return self._resource_cache[cache_key]
        
        image_path = self.images_dir / image_name
        
        if image_path.exists():
            pixmap = QPixmap(str(image_path))
            
            if cache:
                self._resource_cache[cache_key] = pixmap
                
            return pixmap
        else:
            self.logs.log_error(f"Attention: Image introuvable: {image_path}")
            return QPixmap()
    
    def clear_cache(self):
        """Vide le cache des ressources"""
        self._icon_cache.clear()
        self._resource_cache.clear()
    
    def get_app_data_dir(self):
        """Retourne le dossier de données de l'application"""
        app_name = self.app.applicationName() or "MonApp"
        return QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
    
    def run(self):
        """Lance l'application Qt"""
        return self.app.exec()


# Exemple d'utilisation
if __name__ == "__main__":
    from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
    
    class MainWindow(QMainWindow):
        def __init__(self, ctx):
            super().__init__()
            self.ctx = ctx
            self.setWindowTitle("Test AppContext")
            self.setGeometry(300, 300, 400, 200)
            
            # Widget central
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
            layout = QVBoxLayout(central_widget)
            
            # Bouton avec icône
            btn = QPushButton("Bouton avec icône")
            # Suppose qu'il y a un fichier "app_icon.png" dans resources/icons/
            icon = self.ctx.get_icon("app_icon")
            btn.setIcon(icon)
            layout.addWidget(btn)
            
            # Label avec chemin de ressource
            label = QLabel(f"Dossier ressources: {self.ctx.resources_dir}")
            layout.addWidget(label)
    
    # Créer et lancer l'application
    ctx = AppContext()
    ctx.app.setApplicationName("MonApp")
    
    window = MainWindow(ctx)
    window.show()
    
    ctx.run()