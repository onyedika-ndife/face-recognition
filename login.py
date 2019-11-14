import sys
from PyQt5.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QDialog,
    QApplication,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from database import db
from MainWindow import main_window


class LOGIN(QDialog):
    datab = db.Database()

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
        self.datab.cur.execute("SELECT * FROM Admin")

        for row in self.datab.cur:
            if (
                row[1] == self.user_name_input.text()
                and row[2] == self.pass_word_input.text()
            ):
                self.hide()
                self.app_view = main_window.MAIN_WINDOW()
                self.app_view.show()
            elif (
                self.user_name_input.text() == "" and self.pass_word_input.text() == ""
            ):
                self.credentials_incorrect.setText(
                    "Username and Password cannot be empty!"
                )
            elif (
                not self.user_name_input.text() == ""
                and self.pass_word_input.text() == ""
            ):
                self.credentials_incorrect.setText("Password cannot be empty!")
            elif (
                self.user_name_input.text() == ""
                and not self.pass_word_input.text() == ""
            ):
                self.credentials_incorrect.setText("Username cannot be empty!")
            elif (
                not row[1] == self.user_name_input.text()
                and not row[2] == self.pass_word_input.text()
            ):
                self.credentials_incorrect.setText("Username and Password Incorrect!!")
            elif (
                not row[1] == self.user_name_input.text()
                and row[2] == self.pass_word_input.text()
            ):
                self.credentials_incorrect.setText("Username Incorrect!!")
            elif (
                row[1] == self.user_name_input.text()
                and not row[2] == self.pass_word_input.text()
            ):
                self.credentials_incorrect.setText("Password Incorrect!!")
            else:
                pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    view = LOGIN()
    view.show()
    view.raise_()

    sys.exit(app.exec_())
