class VirtualLibrary(Film):
    """Classe Library Virtuel"""
    def __init__(self, name, created_date, place, type, type_choice):
        super().__init__(name, created_date, place, type)
        self.type_choice = type_choice
        
    def sorted_name(self):
        """Méthode pour afficher la liste des films par nom"""
        pass
    
    def sorted_date(self):
        """Méthode pour afficher la liste des films par date de création"""
        pass
    
    def sorted_type(self):
        """Méthode pour afficher la liste des films par type"""
        pass