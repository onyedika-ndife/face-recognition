import sys

import qdarkstyle
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
)

from main_window import main_window

APP_URL = "http://127.0.0.1:8000"
# APP_URL = "https://face-recog-server.herokuapp.com"


class LOGIN(QDialog):
    def __init__(self):
        super().__init__()
        self.move(500, 200)
        self.setFixedSize(350, 250)

        self.setStyleSheet(open("./assets/css/login.css").read())

        self.setWindowTitle("LOGIN")

        self._component()

    def _component(self):
        self.main_grid = QGridLayout()

        self.user_name_label = QLabel("Username:")
        self.user_name_label.setObjectName("Label")
        self.user_name_input = QLineEdit()

        self.pass_word_label = QLabel("Password:")
        self.pass_word_label.setObjectName("Label")
        self.pass_word_input = QLineEdit()
        self.pass_word_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self._handle_login)

        self._setup_ui()

    def _setup_ui(self):
        self.main_grid.addWidget(self.user_name_label, 0, 0)
        self.main_grid.addWidget(self.user_name_input, 0, 1)

        self.main_grid.addWidget(self.pass_word_label, 1, 0)
        self.main_grid.addWidget(self.pass_word_input, 1, 1)

        self.main_grid.addWidget(self.login_btn, 2, 0, 1, 0)

        self.setLayout(self.main_grid)

    def _handle_login(self):
        user_name = str(self.user_name_input.text())
        pass_word = str(self.pass_word_input.text())

        data = {"user_name": user_name, "pass_word": pass_word}

        r = requests.post(url=f"{APP_URL}", data=data)

        msg = QMessageBox()

        if r.text == "Authentication Success":
            self.hide()
            self.app_view = main_window.MAIN_WINDOW()
            self.app_view.show()
        elif self.user_name_input.text() == "" and self.pass_word_input.text() == "":
            msg.setWindowTitle("Error!")
            msg.setText("Username and Password cannot be empty")
            msg.show()
            msg.exec_()
        elif (
            self.user_name_input.text() == "" and not self.pass_word_input.text() == ""
        ):
            msg.setWindowTitle("Error!")
            msg.setText("Username cannot be empty")
            msg.show()
            msg.exec_()
        elif (
            not self.user_name_input.text() == "" and self.pass_word_input.text() == ""
        ):
            msg.setWindowTitle("Error!")
            msg.setText("Password cannot be empty")
            msg.show()
            msg.exec_()
        elif r.text == "Incorrect Password":
            msg.setWindowTitle("Error!")
            msg.setText("Incorrect Password")
            msg.show()
            msg.exec_()
        else:
            msg.setWindowTitle("Error!")
            msg.setText("Username and Password are Incorrect")
            msg.show()
            msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    try:
        r = requests.get(url=f"{APP_URL}")
        print(r.text)
    except requests.exceptions.ConnectionError as e:
        msg = QMessageBox()
        msg.setIconPixmap(QPixmap("./assets/icons/no_connection.png"))
        msg.setWindowTitle("Error!")
        msg.setWindowIcon(QIcon("./assets/icons/error.png"))
        msg.setText("Connect to the Internet to use app!")
        msg.show()

        if msg.exec_() or msg == QMessageBox.Ok:
            sys.exit()
    except requests.exceptions.Timeout as e:
        msg = QMessageBox()
        msg.setIconPixmap(QPixmap("./assets/icons/network_timeout.png"))
        msg.setWindowIcon(QIcon("./assets/icons/error.png"))
        msg.setWindowTitle("Information")
        msg.setText("Poor Network Connection!")
        msg.show()

        if msg.exec_() or msg == QMessageBox.Ok:
            sys.exit()

    view = LOGIN()
    view.show()
    view.raise_()

    sys.exit(app.exec_())
