import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)
from register import register_main
from login import login


class MAIN_WINDOW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Recognition")
        self.setGeometry(500, 200, 350, 250)

        self.setStyleSheet(open("./assets/css/main.css").read())

        self.stacked_layout = QStackedLayout()

        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)

        self.login_view()

    def login_view(self):
        self.log_view = login.LOGIN()

        self.stacked_layout.addWidget(self.log_view.main_widget)

        self.log_view.login_btn.clicked.connect(
            lambda: self.log_view.login(self.main_view)
        )

    def main_view(self):
        self.initial_layout = QVBoxLayout()

        register = QPushButton("Register")
        chk_ver = QPushButton("Verify Student")
        edit = QPushButton("Edit Student Details")

        self.initial_layout.addWidget(register)
        self.initial_layout.addWidget(chk_ver)
        self.initial_layout.addWidget(edit)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.initial_layout)

        self.stacked_layout.addWidget(self.main_widget)

        self.stacked_layout.setCurrentIndex(1)

        register.clicked.connect(self.Reg_Stud_Open)

    def Reg_Stud_Open(self):
        self.setWindowTitle("REGISTER")

        self.reg_view = register_main.REGISTER_MAIN()

        self.stacked_layout.addWidget(self.reg_view.main_widget)

        self.stacked_layout.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    view = MAIN_WINDOW()
    view.show()
    view.raise_()

    sys.exit(app.exec_())
