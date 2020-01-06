import cv2
import os
import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from function.recognize_student import RECOGNIZE
from .view_details import VIEW_DETAILS
from .edit_details import EDIT_DETAILS


APP_URL = "http://127.0.0.1:8000"
# APP_URL = "https://face-recog-server.herokuapp.com"
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
        self.cam_btn = QPushButton("Capture")

        self.video_init_layout.addWidget(self.cam_view)
        self.video_init_layout.addWidget(self.cam_btn)
        self.video_widget.setLayout(self.video_init_layout)

        self.cam_btn.clicked.connect(self.snap)

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

        image_copy = self.image.copy()

        self.face_cascade = cv2.CascadeClassifier(
            "./assets/classifier/haarcascade_frontalface_alt2.xml"
        )

        # Capture Image-by-Image
        gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 255, 255), 1)

        self.image_shown = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

        # get image infos
        self.height, self.width, self.channel = self.image_shown.shape
        self.step = self.channel * self.width

        # create QImage from image
        self.qImg = QImage(
            self.image_shown.data,
            self.width,
            self.height,
            self.step,
            QImage.Format_RGB888,
        )

        # Set the data from qImg to cam_view
        self.cam_view.setPixmap(QPixmap.fromImage(self.qImg))

    def MAIN_VIEW(self, prev, profile):
        self.title.setWindowTitle("STUDENT DETAILS")
        self.profile = profile
        self.initial_layout = QVBoxLayout()
        self.main_widget = QWidget()

        self.view_details_btn = QPushButton("View Details")
        self.edit_details_btn = QPushButton("Edit Details")

        self.view_details_btn.setObjectName("btn")
        self.edit_details_btn.setObjectName("btn")

        self.view_details_btn.setIcon(QIcon("./assets/img/View Details.png"))
        self.edit_details_btn.setIcon(QIcon("./assets/img/Edit Details.png"))

        self.view_details_btn.setIconSize(QSize(50, 50))
        self.edit_details_btn.setIconSize(QSize(50, 50))

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
        # pm grant com.xda.nobar android.permission.WRITE_SECURE_SETTINGS
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

    def snap(self):
        image_cropped = self.image[0:480, 80:560]

        cv2.imwrite("./assets/img/temp/temp.jpg", image_cropped)

        self.timer.stop()
        self.cam.release()

        for image in os.listdir("./assets/img/temp/"):
            file = {"image": open(f"./assets/img/temp/{image}", "rb").read()}
            r = requests.post(url=f"{APP_URL}/recognize/student/", files=file)

            if r.text == "Unknown Individual":
                self.previous()
            else:
                profile = r.json()
                self.MAIN_VIEW(self.previous, profile)

