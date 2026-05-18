# taskitem.py
# --------------
# Purpose:
# class TaskItem
# ---------------------------
# Creation date: 2025-07-29
# Modification date: 2025-07-29
# ------------------------------
# Version V1.0.0:

from PySide6.QtCore import QSize
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QListWidgetItem

from resources.constantes import COLORS
import API.task as api

class TaskItem(QListWidgetItem):

    def __init__(self, name, done, list_widget):
        super().__init__(name)
        self.done = done
        self.list_widget = list_widget
        self.name = name

        self.setSizeHint(QSize(self.sizeHint().width(), 100))
        self.list_widget.addItem(self)
        self.set_background_color()

    def toggle_state(self):
        self.done = not self.done
        api.set_tasks_statut(name=self.name, done=self.done)
        self.set_background_color()

    def set_background_color(self):
        colors = COLORS.get(self.done)
        self.setBackground(QColor(*colors)) # * permet d'unpacker le tuple
        color_str = ", ".join(map(str, colors))
        stylesheet = f"""
        QListView::item:selected {{
            background-color: rgb({color_str});
            color: rgb(0, 0, 0);
        }}
        QListView::item:hover {{
            background-color: rgb(220, 220, 220);
        }}
        """
        self.list_widget.setStyleSheet(stylesheet)
