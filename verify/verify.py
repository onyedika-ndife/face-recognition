import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from function import recognize


class VERIFY(QMainWindow):
    def __init__(self, prev_scrn):
        super().__init__()

        self.recognize = recognize.RECOGNIZE()

        self.UI(prev_scrn)

        # create a timer
        self.timer = QTimer()

        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)

    def UI(self, prev_scrn):
        self.main_menu = self.menuBar()

        self.file_menu = self.main_menu.addMenu("File")
        self.edit_menu = self.main_menu.addMenu("Edit")

        self.print_action = QAction(QIcon("./assets/img/printer.svg"), "Print", self)
        self.print_action.setShortcut("Ctrl+P")

        self.edit_action = QAction(
            QIcon("./assets/img/edit.svg"), "Edit Student Details", self
        )

        self.exit_action = QAction(QIcon("./assets/img/arrow_back.svg"), "Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")

        self.file_menu.addAction(self.print_action)
        self.file_menu.addAction(self.exit_action)

        self.edit_menu.addAction(self.edit_action)

        self.print_action.triggered.connect(self.print_details)
        self.exit_action.triggered.connect(lambda: prev_scrn())

    def print_details(self):
        print("a")

