import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from register import register_main
from verify import verify


class MAIN_WINDOW(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 640, 480)
        self.win_title = "FACE RECOGNITION"
        self.setWindowTitle(self.win_title)

        self.setStyleSheet(open("./assets/css/main.css").read())

        # Main Layout of Widget
        self.main_layout = QStackedLayout()
        self.setLayout(self.main_layout)

        self._view()
        self._other_view()

    def _view(self):
        self.initial_layout = QVBoxLayout()

        self.register = QPushButton("Register")
        self.verification = QPushButton("Verify Student")
        self.edit = QPushButton("Edit Student Details")

        view = [self.register, self.verification, self.edit]
        for btn in view:
            btn.setStyleSheet(
                "QPushButton {\n"
                "text-transform: uppercase;\n"
                "font-weight: 600;\n"
                "border-radius: none;\n"
                "background: #1abc9c;\n"
                "color: #fff;\n"
                "font-size: 20px;\n"
                "padding: 5px;}\n"
                "QPushButton:pressed {\n"
                "background: #16a085;}"
            )

        self.initial_layout.addWidget(self.register)
        self.initial_layout.addWidget(self.verification)
        self.initial_layout.addWidget(self.edit)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.initial_layout)

        self.main_layout.addWidget(self.main_widget)

        self.register.clicked.connect(self._handle_open_register_view)
        self.verification.clicked.connect(self._handle_open_verify_view)

    def _other_view(self):
        # For other screens aside Login Screen And Main View Screen
        self.stacked = QStackedWidget()
        self.main_grid_widget = QWidget()
        self.main_grid = QGridLayout()
        self.back_btn = QCommandLinkButton()
        self.back_btn.setIcon(QIcon("./assets/img/arrow_back.svg"))
        self.main_grid_widget.setLayout(self.main_grid)

        self.main_grid.addWidget(self.back_btn, 0, 0)
        self.main_grid.addWidget(self.stacked, 1, 0, 1, 0)

        self.back_btn.clicked.connect(self._handle_go_back)
        self.back_btn.setMaximumWidth(35)

    def _handle_open_register_view(self):
        self.setWindowTitle("REGISTER")

        self.reg_view = register_main.REGISTER_MAIN()

        self.stacked.addWidget(self.reg_view.main_widget)
        self.stacked.setCurrentIndex(1)

        self.main_layout.addWidget(self.main_grid_widget)
        self.main_layout.setCurrentWidget(self.main_grid_widget)

    def _handle_open_verify_view(self):
        self.setWindowTitle("SHOW STUDENT DETAILS")

        prev_screen = self.main_layout
        self.ver_view = verify.VERIFY(self._handle_go_back)

        self.main_layout.addWidget(self.ver_view)
        self.main_layout.setCurrentWidget(self.ver_view)

    def _handle_open_edit_view(self):
        self.win_title = "EDIT STUDENT DETAILS"
        self.setWindowTitle(self.win_title)

    def _handle_go_back(self):
        self.main_layout.setCurrentIndex(0)
        self.setWindowTitle(self.win_title)

