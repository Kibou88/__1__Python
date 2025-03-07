# Exemple de args et kwargs avec pyside
#---------------------------------------
import sys
from PySide6.QtWidgets import QPushButton, QApplication

couleur_bouton = (255, 0, 0) # Code RVB
couleur_bouton2 = {'rouge': 0, 'vert': 255, 'bleu': 0}

class InterfaceBasique(QPushButton):
    def __init__(self, text='Clique'):
        super(InterfaceBasique, self).__init__(text)

        # self.setStyleSheet('background-color: rgb({}, {}, {})'.format(*couleur_bouton))
        self.setStyleSheet('background-color: rgb({rouge}, {vert}, {bleu})'.format(**couleur_bouton2))

app = QApplication([])
bouton = InterfaceBasique()
bouton.show()
sys.exit(app.exec())