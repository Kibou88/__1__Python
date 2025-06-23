from PySide6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyNotes")
        # self.setup_ui(self)

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        pass

    def modify_widgets(self):
        pass

    def create_layout(self):
        pass

    def add_widgets_to_layouts(self):
        pass

    def setup_connections(self):
        pass


app = QApplication() #1 seule  QApplication

main_window1 = MainWindow()
main_window1.show()

app.exec() #Lancer l'application