import sys
import requests
from PyQt5.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QDialog,
    QMessageBox,
    QApplication,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from MainWindow import main_window


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
        self._setup_ui()

    def _component(self):
        self.main_grid = QGridLayout()

        self.user_name_label = QLabel("Username:")
        self.user_name_label.setObjectName("Label")
        self.user_name_input = QLineEdit()

        self.pass_word_label = QLabel("Password:")
        self.pass_word_label.setObjectName("Label")
        self.pass_word_input = QLineEdit()
        self.pass_word_input.setEchoMode(QLineEdit.Password)

        self.credentials_incorrect = QLabel()
        self.credentials_incorrect.setStyleSheet("font-weight: bold; color: red")
        self.credentials_incorrect.setAlignment(Qt.AlignCenter)
        self.credentials_incorrect.setMaximumHeight(12)

        self.login_btn = QPushButton("Login")

        self.login_btn.clicked.connect(self._handle_login)

    def _setup_ui(self):
        self.main_grid.addWidget(self.user_name_label, 0, 0)
        self.main_grid.addWidget(self.user_name_input, 0, 1)

        self.main_grid.addWidget(self.pass_word_label, 1, 0)
        self.main_grid.addWidget(self.pass_word_input, 1, 1)

        self.main_grid.addWidget(self.credentials_incorrect, 2, 0, 1, 0)

        self.main_grid.addWidget(self.login_btn, 3, 0, 1, 0)

        self.setLayout(self.main_grid)

    def _handle_login(self):
        user_name = str(self.user_name_input.text())
        pass_word = str(self.pass_word_input.text())

        data = {"user_name": user_name, "pass_word": pass_word}

        r = requests.post(url=f"{APP_URL}", data=data)

        if r.text == "Success!!":
            self.hide()
            self.app_view = main_window.MAIN_WINDOW()
            self.app_view.show()
        elif self.user_name_input.text() == "" and self.pass_word_input.text() == "":
            self.credentials_incorrect.setText("Username and Password cannot be empty!")
        elif (
            not self.user_name_input.text() == "" and self.pass_word_input.text() == ""
        ):
            self.credentials_incorrect.setText("Password cannot be empty!")
        elif (
            self.user_name_input.text() == "" and not self.pass_word_input.text() == ""
        ):
            self.credentials_incorrect.setText("Username cannot be empty!")
        else:
            self.credentials_incorrect.setText("Username and Password Incorrect!!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    try:
        r = requests.get(url=f"{APP_URL}")
    except requests.exceptions.ConnectionError as e:
        msg = QMessageBox()
        msg.setIconPixmap(QPixmap("./assets/icons/no_connection.png"))
        msg.setWindowTitle("Error!")
        msg.setText("Connect to the Internet to use app!")
        msg.show()

        if msg.exec_() or msg == QMessageBox.Ok:
            sys.exit()
    except requests.exceptions.Timeout as e:
        msg = QMessageBox()
        msg.setIconPixmap(QPixmap("./assets/icons/network_timeout.png"))
        msg.setWindowTitle("Information")
        msg.setText("Poor Network Connection!")
        msg.exec_()

        if msg.exec_() or msg == QMessageBox.Ok:
            sys.exit()

    view = LOGIN()
    view.show()
    view.raise_()

    sys.exit(app.exec_())
