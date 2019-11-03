import cv2

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from function.recognize_staff import RECOGNIZE
from .view_details import VIEW_DETAILS
from .edit_details import EDIT_DETAILS


class VERIFY(QWidget):
    def __init__(self, title, main_layout, grid_widget, stacked, prev):
        super().__init__()
        self.title = title
        self.previous = prev
        self.stacked = stacked
        self.grid_widget = grid_widget

        self.main_layout = main_layout

        self._video_view()

    def _video_view(self):
        self.video_widget = QWidget()
        self.video_init_layout = QVBoxLayout()

        # Create Camera View
        self.cam_view = QLabel()

        self.video_init_layout.addWidget(self.cam_view)
        self.video_widget.setLayout(self.video_init_layout)

        self.main_layout.addWidget(self.video_widget)
        self.main_layout.setCurrentWidget(self.video_widget)

        # create a timer
        self.timer = QTimer()

        # set timer timeout callback function
        self.timer.timeout.connect(self._video)

        if not self.timer.isActive():
            self.cam = cv2.VideoCapture(0)
            self.timer.start(1)

    def _video(self):
        ret, self.image = self.cam.read()
        self.recognize = RECOGNIZE(self.image)

        self.image_copy = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        # get image infos
        self.height, self.width, self.channel = self.image_copy.shape
        self.step = self.channel * self.width

        # create QImage from image
        self.qImg = QImage(
            self.image_copy.data,
            self.width,
            self.height,
            self.step,
            QImage.Format_RGB888,
        )

        # Set the data from qImg to cam_view
        self.cam_view.setPixmap(QPixmap.fromImage(self.qImg))

        if self.recognize.verified == True:
            self.timer.stop()
            self.cam.release()
            self.MAIN_VIEW(self.previous, self.recognize.profile)

    def MAIN_VIEW(self, prev, profile):
        self.title.setWindowTitle("STUDENT DETAILS")
        self.profile = profile
        self.initial_layout = QVBoxLayout()
        self.main_widget = QWidget()

        self.view_details_btn = QPushButton("View Details")
        self.edit_details_btn = QPushButton("Edit Details")

        self.initial_layout.addWidget(self.view_details_btn)
        self.initial_layout.addWidget(self.edit_details_btn)

        self.main_widget.setLayout(self.initial_layout)

        self.stacked.addWidget(self.main_widget)
        self.stacked.setCurrentWidget(self.main_widget)

        self.main_layout.addWidget(self.grid_widget)
        self.main_layout.setCurrentWidget(self.grid_widget)

        self.view_details_btn.clicked.connect(self._handle_view_details)
        self.edit_details_btn.clicked.connect(self._handle_edit_details)

    def _handle_view_details(self):
        view_details = VIEW_DETAILS(
            self.title,
            lambda: self.main_layout.setCurrentWidget(self.grid_widget),
            self.profile,
            self.main_layout,
        )

    def _handle_edit_details(self):
        edit_details = EDIT_DETAILS(
            self.title,
            lambda: self.main_layout.setCurrentWidget(self.grid_widget),
            self.profile,
            self.main_layout,
        )
