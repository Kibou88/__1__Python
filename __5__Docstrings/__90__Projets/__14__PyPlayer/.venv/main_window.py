# main_window.py
# --------------
# Purpose:
# Create the GUI for PyPlayer
# ---------------------------
# Creation date: 2025-07-13
# Modification date: 2025-07-15
# ------------------------------
# Version V1.0.0:

import sys
import os
from pathlib import Path
from functools import partial

from PySide6 import QtGui, QtMultimedia, QtMultimediaWidgets, QtWidgets, QtCore
from PySide6.QtGui import QShortcut, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QListWidget, QTextEdit, QGridLayout, QInputDialog, QListWidgetItem

from misc.logs import Logs

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, log_dir_name="Logs"):
        super().__init__()
        self.logs = Logs(application_name="PyPlayer", log_dir=log_dir_name)
        self.setWindowTitle("PyPlayer")
        self.setWindowIcon(QIcon("resources/icons/Icon.ico"))

        # Multimedia icons from PySide6
        self.open_icon = self.style().standardIcon(QtWidgets.QStyle.SP_DriveDVDIcon)
        self.play_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay)
        self.previous_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaSkipBackward)
        self.next_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaSkipForward)
        self.pause_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause)
        self.stop_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop)

        self.setup_ui()

        # Counter
        self.is_fullscreen = False

    def setup_ui(self):
        """
        Initialize l'UI
        :return:
        Occur an error if the initialization fails
        """
        # L'ORDRE EST IMPORTANT
        try:
            self.create_widgets()
            self.create_layouts()
            self.modify_widgets()
            self.add_widgets_to_layouts()
            self.setup_connections()
        except Exception as e:
            self.logs.log_error(e)
            raise Exception(f"Something went wrong {e}.")
        else:
            self.logs.log_info("Successfully setup UI.")

    def create_widgets(self):
        """
        Create widgets for the application
        """
        self.video_widget = QtMultimediaWidgets.QVideoWidget()
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)
        self.audio_output = QtMultimedia.QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.toolbar = QtWidgets.QToolBar("Main ToolBar") # Give a name to the toolbar
        self.file_menu = self.menuBar().addMenu("File") # Belong with QMainWindow

        # Actions:
        self.act_open = self.file_menu.addAction(self.open_icon, "Open")
        self.act_open.setShortcut("Ctrl+O")
        self.act_play = self.toolbar.addAction(self.play_icon, "Play")
        self.act_previous = self.toolbar.addAction(self.previous_icon, "Previous")
        self.act_pause = self.toolbar.addAction(self.pause_icon, "Pause")
        self.act_pause.setShortcut("Ctrl+P")
        self.act_next = self.toolbar.addAction(self.next_icon, "Next")
        self.act_stop = self.toolbar.addAction(self.stop_icon, "Stop")

    def modify_widgets(self):
        """
        Show a style for the application
        """
        pass

    def create_layouts(self):
        """
        Creation of grid layout
        """
        pass

    def add_widgets_to_layouts(self):
        """
        Add widgets to the layout
        """
        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.video_widget)
        self.player.setVideoOutput(self.video_widget)

    def setup_connections(self):
        """
        Connect widgets to the methods
        """
        self.act_open.triggered.connect(self.open_media)
        self.act_play.triggered.connect(self.player.play)
        self.act_pause.triggered.connect(self.player.pause)
        self.act_stop.triggered.connect(self.player.stop)
        self.act_previous.triggered.connect(partial(self.player.setPosition, 0))
        self.act_next.triggered.connect(partial(self.player.setPosition, 1))
        self.player.playbackStateChanged.connect(self.update_buttons)

        # Full Screen Mode
        QShortcut(QtGui.QKeySequence("Ctrl+F"), self.video_widget, self.full_screen_mode)


    def update_buttons(self, state):
        """
        Update the shape of buttons
        If the video is running, disable the play button
        If the video pause, disable the pause button
        :return:
        """
        print(state)
        self.act_play.setDisabled(state == QtMultimedia.QMediaPlayer.PlaybackState.PlayingState)
        self.act_pause.setDisabled(state == QtMultimedia.QMediaPlayer.PlaybackState.PausedState)
        self.act_stop.setDisabled(state == QtMultimedia.QMediaPlayer.PlaybackState.StoppedState)

    def open_media(self):
        """
        Open media file (mp4 format)
        :return:
        """
        file_dialog = QtWidgets.QFileDialog(self)
        # Permet de filtrer les extensions
        file_dialog.setMimeTypeFilters(["video/mp4"])
        # Permet d'aller dans le répertoire des Films
        movies_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_dir)
        if file_dialog.exec() == QtWidgets.QDialog.Accepted: # L'utilisateur aura choisi et validé un fichier
            movie = file_dialog.selectedUrls()[0] # Récupérer le premier élément de la liste
            if movie.fileName()[-3:] != "mp4":
                self.logs.log_error(f"{movie.fileName()} is not a mp4 file.")
                raise Exception(f"File {movie.fileName()} is not a mp4 file.")
            self.logs.log_info(f"Opened {movie.fileName()}")
            self.video_widget.setAspectRatioMode(QtCore.Qt.KeepAspectRatio)
            self.player.setSource(movie)
            self.player.play()

    def full_screen_mode(self):
        """
        Manage the full screen mode
        """
        if self.is_fullscreen == True:
            self.video_widget.setFullScreen(False)
            self.is_fullscreen = False
            self.logs.log_info("Full screen mode disabled.")
        elif self.is_fullscreen == False:
            self.video_widget.setFullScreen(True)
            self.is_fullscreen = True
            self.logs.log_info("Full screen mode enabled.")

if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow(log_dir_name="Test_log")
    windows.resize(800, 600)
    windows.show()
    exit_app_logs = Logs(application_name="PyPlayer", log_dir="Test_log")

    exit_code = app.exec() # 2. Invoke app.exec()
    exit_app_logs.log_info("Application is shutting down")
    sys.exit(exit_code)