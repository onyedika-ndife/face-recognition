import sys
from PyQt5.QtWidgets import *
from database import db


class LOGIN(QDialog):
    datab = db.Database()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOGIN")

        self.component()
        self.setupUI()
        self.database()

    def component(self):
        self.initial_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_grid = QGridLayout()

        self.user_name_label = QLabel("Username:")
        self.user_name_input = QLineEdit()

        self.pass_word_label = QLabel("Password:")
        self.pass_word_input = QLineEdit()
        self.pass_word_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")

    def setupUI(self):
        self.main_grid.addWidget(self.user_name_label, 0, 0)
        self.main_grid.addWidget(self.user_name_input, 0, 1)

        self.main_grid.addWidget(self.pass_word_label, 1, 0)
        self.main_grid.addWidget(self.pass_word_input, 1, 1)

        self.main_grid.addWidget(self.login_btn, 3, 0, 1, 0)

        self.main_widget.setLayout(self.main_grid)

        self.initial_layout.addWidget(self.main_widget)

    def database(self):
        self.datab.cur.execute(
            "CREATE TABLE IF NOT EXISTS Admin (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)"
        )
        self.datab.conn.commit()

    def login(self, main_view):
        self.datab.cur.execute("SELECT * FROM Admin")

        for row in self.datab.cur:
            if (
                row[1] == self.user_name_input.text()
                and row[2] == self.pass_word_input.text()
            ):
                main_view()
