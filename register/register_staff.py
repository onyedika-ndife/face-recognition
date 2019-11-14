import cv2
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class REGISTER_STAFF(QDialog):
    def __init__(self, main_layout, components):
        super().__init__()
        self.main_layout = main_layout

        self.setWindowTitle("REGISTER STAFF")

        comp = components()

        # For other screens
        self.stacked = QStackedLayout()

        self.setupUI(comp)

    def setupUI(self, components):
        self.comp = components

        self.personal_details()

        self.setLayout(self.stacked)

    def personal_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("Personal Details")

        _next = QPushButton("Next")
        _next.setIcon(QIcon("./assets/img/Next.png"))

        # ADDING WIDGETS
        grid.addWidget(self.comp.f_name, 0, 0)
        grid.addWidget(self.comp.f_name_input, 0, 1)

        grid.addWidget(self.comp.m_name, 1, 0)
        grid.addWidget(self.comp.m_name_input, 1, 1)

        grid.addWidget(self.comp.l_name, 2, 0)
        grid.addWidget(self.comp.l_name_input, 2, 1)

        grid.addWidget(self.comp.dob_label, 3, 0)
        grid.addLayout(self.comp.dob_layout, 3, 1)

        grid.addWidget(self.comp.age, 4, 0)
        grid.addWidget(self.comp.age_input, 4, 1)

        grid.addWidget(self.comp.gender, 5, 0)
        grid.addLayout(self.comp.gender_layout, 5, 1)

        grid.addWidget(self.comp.marital, 6, 0)
        grid.addWidget(self.comp.marital_select, 6, 1)

        grid.addWidget(self.comp.nationality, 7, 0)
        grid.addWidget(self.comp.nationality_input, 7, 1)

        grid.addWidget(self.comp.state_origin, 8, 0)
        grid.addWidget(self.comp.state_origin_input, 8, 1)

        grid.addWidget(self.comp.lga_origin, 9, 0)
        grid.addWidget(self.comp.lga_origin_input, 9, 1)

        grid.addWidget(_next, 10, 0, 1, 0)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.pd_main_widget = QWidget()
        self.pd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.pd_main_widget)
        self.stacked.setCurrentWidget(self.pd_main_widget)

        # When next button is clicked
        _next.clicked.connect(self.school_details)

    def school_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("Work Details")

        btn_view = QHBoxLayout()
        _next = QPushButton("Next")
        _prev = QPushButton("Previous")
        _prev.setIcon(QIcon("./assets/img/Prev.png"))
        _next.setIcon(QIcon("./assets/img/Next.png"))


        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.profession, 0, 0)
        grid.addWidget(self.comp.profession_input, 0, 1)

        grid.addLayout(btn_view, 1, 0, 1, 0)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.sd_main_widget = QWidget()
        self.sd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.sd_main_widget)
        self.stacked.setCurrentWidget(self.sd_main_widget)

        # When prev button is clicked
        _prev.clicked.connect(
            lambda: self.stacked.setCurrentWidget(self.pd_main_widget)
        )

        # When next button is clicked
        _next.clicked.connect(self.contact_details)

    def contact_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("Contact Details")

        btn_view = QHBoxLayout()
        _next = QPushButton("Next")
        _prev = QPushButton("Previous")
        _prev.setIcon(QIcon("./assets/img/Prev.png"))
        _next.setIcon(QIcon("./assets/img/Next.png"))

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.address, 0, 0)
        grid.addWidget(self.comp.address_input, 0, 1)

        grid.addWidget(self.comp.phone, 1, 0)
        grid.addWidget(self.comp.phone_input, 1, 1)

        grid.addWidget(self.comp.email, 2, 0)
        grid.addWidget(self.comp.email_input, 2, 1)

        grid.addLayout(btn_view, 3, 0, 1, 0)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.cd_main_widget = QWidget()
        self.cd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.cd_main_widget)
        self.stacked.setCurrentWidget(self.cd_main_widget)

        # When prev button is clicked
        _prev.clicked.connect(
            lambda: self.stacked.setCurrentWidget(self.sd_main_widget)
        )

        # When next button is clicked
        _next.clicked.connect(self.done)

    def done(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox()

        btn_view = QHBoxLayout()
        _next = QPushButton("Capture Face")
        _prev = QPushButton("Previous")
        _prev.setIcon(QIcon("./assets/img/Prev.png"))
        _next.setIcon(QIcon("./assets/img/Capture.png"))
        _next.setIconSize(QSize(20,20))

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.dor, 0, 0)
        grid.addWidget(self.comp.dor_text, 0, 1)

        grid.addLayout(btn_view, 1, 0, 1, 0)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.d_main_widget = QWidget()
        self.d_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.d_main_widget)
        self.stacked.setCurrentWidget(self.d_main_widget)

        # When prev button is clicked
        _prev.clicked.connect(
            lambda: self.stacked.setCurrentWidget(self.cd_main_widget)
        )

        # When next button is clicked
        _next.clicked.connect(self.register_staff_details)

    def register_staff_details(self):
        # Assigning Variables
        first_name = self.comp.f_name_input.text()
        middle_name = self.comp.m_name_input.text()
        last_name = self.comp.l_name_input.text()
        date_of_birth = self.comp.dob_date_label.text()
        age = self.comp.age_input.text()
        gender = (
            self.comp.gender_1.text()
            if self.comp.gender_1.isChecked()
            else self.comp.gender_2.text()
        )
        nationality = self.comp.nationality_input.text()
        state_of_origin = self.comp.state_origin_input.text()
        lga_origin = self.comp.lga_origin_input.text()
        marital = self.comp.marital_select.currentText()
        profession = self.comp.profession_input.text()
        date_of_reg = self.comp.dor_text.text()

        self.comp.datab.cur.execute(
            f"INSERT INTO recognize_staff(first_name, middle_name, last_name,age,date_of_birth, gender, nationality, state_of_origin, lga_origin,marital_status, profession,address,phone_number,email,date_of_registration) VALUES('{first_name}','{middle_name}','{last_name}',{age},'{date_of_birth}','{gender}','{nationality}','{state_of_origin}','{lga_origin}','{marital}','{profession}','{address}','{phone}','{email}','{date_of_reg}')"
        )


        self.register_face()

    def register_face(self):
        self.comp.datab.cur.execute("SELECT * FROM recognize_staff")
        self.latest_register = self.comp.datab.cur.fetchall()[-1]

        self._id = self.latest_register[0]
        self.name = f"{self.latest_register[3]}_{self.latest_register[1]}".lower()

        self.face_cascade = cv2.CascadeClassifier(
            "./assets/classifiers/haarcascade_frontalface_alt2.xml"
        )

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

        # self.train_faces.TRAINER(self._id, self.name)

    def snap(self):
        image_cropped = self.image[0:480, 80:560]
        if not os.path.exists(
            f"./face_recog_android/assets/staff/{str(self.name)}"
        ):
            os.makedirs(
                f"./face_recog_android/assets/staff/{str(self.name)}"
            )
        cv2.imwrite(
            f"./face_recog_android/assets/staff/{str(self.name)}/{str(self.name)}.jpg",
            image_cropped,
        )

        self.timer.stop()
        self.cam.release()

        self.comp.datab.conn.commit()
        self.comp.datab.conn.close()

        # trainer = TRAINER.train_staff(self._id, self.name)

        self.main_layout.setCurrentIndex(0)

