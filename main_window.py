import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from register import register_main
from login import login


class MAIN_WINDOW(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Recognition")
        self.setGeometry(500, 200, 350, 250)

        self.setStyleSheet(open("./assets/css/main.css").read())

        self.main_layout = QStackedLayout()

        self.setLayout(self.main_layout)

        # For other screens aside Login Screen And Main View Screen
        self.stacked = QStackedWidget()
        self.main_grid_widget = QWidget()
        self.main_grid = QGridLayout()
        self.back_btn = QCommandLinkButton("Back")
        self.main_grid_widget.setLayout(self.main_grid)

        self.main_grid.addWidget(self.back_btn, 0, 0)
        self.main_grid.addWidget(self.stacked, 1, 0, 1, 0)

        self.login_view()

    def login_view(self):
        self.log_view = login.LOGIN()

        self.main_layout.addWidget(self.log_view.main_widget)

        self.log_view.login_btn.clicked.connect(
            lambda: self.log_view.login(self.main_view)
        )

    def main_view(self):
        self.setWindowModality(Qt.ApplicationModal)
        self.setEnabled(True)
        self.initial_layout = QVBoxLayout()

        register = QPushButton("Register")
        chk_ver = QPushButton("Verify Student")
        edit = QPushButton("Edit Student Details")

        self.initial_layout.addWidget(register)
        self.initial_layout.addWidget(chk_ver)
        self.initial_layout.addWidget(edit)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.initial_layout)

        self.main_layout.addWidget(self.main_widget)

        self.main_layout.setCurrentIndex(1)

        register.clicked.connect(self.reg_view)

    def reg_view(self):
        self.setWindowTitle("REGISTER")

        self.reg_view = register_main.REGISTER_MAIN()

        self.stacked.setLayout(self.reg_view.initial_layout)

        self.main_layout.addWidget(self.main_grid_widget)
        # self.main_layout.addWidget(self.reg_view.main_widget)

        self.main_layout.setCurrentIndex(2)

    def edit_view(self):
        self.setWindowTitle("Edit")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    view = MAIN_WINDOW()
    view.show()
    view.raise_()

    sys.exit(app.exec_())
