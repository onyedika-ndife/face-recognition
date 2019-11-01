from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from register.register_main import REGISTER_MAIN
from student_detail.student_details import VERIFY


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
        self.verification = QPushButton("Student Details")

        self.register.setObjectName("btn")
        self.verification.setObjectName("btn")

        self.initial_layout.addWidget(self.register)
        self.initial_layout.addWidget(self.verification)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.initial_layout)

        self.main_layout.addWidget(self.main_widget)

        self.register.clicked.connect(
            lambda: self._handle_open_register_view(self.main_layout)
        )
        self.verification.clicked.connect(self._handle_open_student_details_view)

    def _other_view(self):
        # For other screens aside Login Screen And Main View Screen
        self.stacked = QStackedWidget()
        self.main_grid_widget = QWidget()
        self.main_grid = QGridLayout()
        self.back_btn = QCommandLinkButton()
        self.back_btn.setIcon(QIcon("./assets/img/svg/arrow-left-circle.svg"))
        self.main_grid_widget.setLayout(self.main_grid)

        self.main_grid.addWidget(self.back_btn, 0, 0)
        self.main_grid.addWidget(self.stacked, 1, 0, 1, 0)

        self.back_btn.clicked.connect(self._handle_go_back)
        self.back_btn.setMaximumWidth(35)

    def _handle_open_register_view(self, main_layout):
        self.setWindowTitle("REGISTER")

        self.reg_view = REGISTER_MAIN(main_layout)

        self.stacked.addWidget(self.reg_view.main_widget)
        self.stacked.setCurrentWidget(self.reg_view.main_widget)

        self.main_layout.addWidget(self.main_grid_widget)
        self.main_layout.setCurrentWidget(self.main_grid_widget)

    def _handle_open_student_details_view(self):

        self.ver_view = VERIFY(
            self,
            self.main_layout,
            self.main_grid_widget,
            self.stacked,
            self._handle_go_back,
        )

    def _handle_go_back(self):
        self.main_layout.setCurrentIndex(0)
        self.setWindowTitle(self.win_title)

