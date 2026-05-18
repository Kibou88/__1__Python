from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QGridLayout Example with PyQt6')

layout = QGridLayout()

# Ajouter des boutons à la grille
layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)

window.setLayout(layout)
window.show()
sys.exit(app.exec())