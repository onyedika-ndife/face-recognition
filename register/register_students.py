import cv2
import os
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .trainer import train


class REGISTER_STUDENT(QDialog):
    def __init__(self, components):
        super().__init__()
        self.setWindowTitle("REGISTER STUDENT")
        self.setStyleSheet(open("./assets/css/main.css").read())

        self.comp = components()

        self.setupUI()

    def setupUI(self):
        # self.comp.dob_date_choose.setStyleSheet("border-radius: inherit")

        # ADDING WIDGETS
        self.comp.main_grid.addWidget(self.comp.f_name, 0, 0)
        self.comp.main_grid.addWidget(self.comp.f_name_input, 0, 1)

        self.comp.main_grid.addWidget(self.comp.m_name, 1, 0)
        self.comp.main_grid.addWidget(self.comp.m_name_input, 1, 1)

        self.comp.main_grid.addWidget(self.comp.l_name, 2, 0)
        self.comp.main_grid.addWidget(self.comp.l_name_input, 2, 1)

        self.comp.main_grid.addWidget(self.comp.dob_label, 3, 0)
        self.comp.main_grid.addLayout(self.comp.dob_layout, 3, 1)

        self.comp.main_grid.addWidget(self.comp.age, 4, 0)
        self.comp.main_grid.addWidget(self.comp.age_input, 4, 1)

        self.comp.main_grid.addWidget(self.comp.gender, 5, 0)
        self.comp.main_grid.addLayout(self.comp.gender_layout, 5, 1)

        self.comp.main_grid.addWidget(self.comp.j_num, 6, 0)
        self.comp.main_grid.addWidget(self.comp.j_num_input, 6, 1)

        self.comp.main_grid.addWidget(self.comp.college, 7, 0)
        self.comp.main_grid.addWidget(self.comp.college_select, 7, 1)

        self.comp.main_grid.addWidget(self.comp.dept, 8, 0)
        self.comp.main_grid.addWidget(self.comp.dept_select, 8, 1)

        self.comp.main_grid.addWidget(self.comp.level, 9, 0)
        self.comp.main_grid.addWidget(self.comp.level_select, 9, 1)

        self.comp.main_grid.addWidget(self.comp.m_num, 10, 0)
        self.comp.main_grid.addWidget(self.comp.m_num_input, 10, 1)

        self.comp.main_grid.addWidget(self.comp.dor, 11, 0)
        self.comp.main_grid.addWidget(self.comp.dor_text, 11, 1)

        self.comp.main_grid.addWidget(self.comp._next, 12, 0, 1, 0)

        self.comp._next.setText("Capture Face")

        # SETTING LAYOUTS
        self.setLayout(self.comp.main_grid)

        # On change of College
        self.comp.college_select.currentIndexChanged.connect(self.school)

        # When next button is clicked
        self.comp._next.clicked.connect(self.register_student_details)

    def school(self, i):
        if i == 0 or i == 1 or i == 4 or i == 6 or i == 7 or i == 9 or i == 10:
            self.comp.level_select.clear()
            self.comp.level_select.addItems(["100L", "200L", "300", "400L"])
        elif i == 2 or i == 3 or i == 5 or i == 8:
            self.comp.level_select.clear()
            self.comp.level_select.addItems(["100L", "200L", "300", "400L", "500L"])
        elif i == 11:
            self.comp.level_select.clear()
            self.comp.level_select.addItems(
                ["100L", "200L", "300", "400L", "500L", "600L"]
            )

        if i == 0:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "AGRIBUSINESS MANAGEMENT",
                    "AGRICULTURAL ECONOMICS",
                    "AGRICULTURAL EXTENSION AND RURAL SOCIOLOGY",
                ]
            )

        elif i == 1:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ANIMAL BREEDING AND PHYSIOLOGY",
                    "ANIMAL NUTRITION AND FORAGE SCIENCE",
                    "ANIMAL PRODUCTION AND LIVESTOCK MANAGEMENT",
                ]
            )

        elif i == 2:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "FOOD SCIENCE AND TECHNOLOGY",
                    "HOME SCIENCE/HOSPITALITY MANAGEMENT AND TOURISM",
                    "HUMAN NUTRITION AND DIETETICS",
                ]
            )
        elif i == 3:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                ["AGRONOMY", "PLANT HEALTH MANAGEMENT", "SOIL SCIENCE AND METREOLOGY"]
            )
        elif i == 4:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ADULT AND CONTINUING EDUCATION",
                    "EDUCATIONAL FOUNDATION",
                    "INDUSTRIAL TECHNOLOGY EDUCATION",
                    "LIBRARY AND INFORMATION SCIENCE",
                    "PSYCHOLOGY AND COUNSELING",
                    "SCIENCE EDUCATION",
                ]
            )
        elif i == 5:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "AGRICULTURAL AND BIO-RESOURCES ENGINEERING",
                    "CHEMICAL ENGINEERING",
                    "CIVIL ENGINEERING",
                    "COMPUTER ENGINEERING",
                    "ELECTRICAL AND ELECTRONICS ENGINEERING",
                    "MECHANICAL ENGINEERING",
                ]
            )
        elif i == 6:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "FRENCH LANGUAGE",
                    "GERMAN LANGUAGE",
                    "HISTORY AND PHILOSOPHY OF SCIENCE",
                    "NIGERIA HISTORY",
                    "PEACE AND CONFLICT STUDIES",
                    "PHILOSOPHY AND LOGIC",
                    "PHYSICAL AND HEALTH EDUCATION",
                    "SOCIAL SCIENCE",
                ]
            )
        elif i == 7:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ACCOUNTING",
                    "BANKING AND FINANCE",
                    "BUSINESS ADMINISTRATION",
                    "ECONOMICS",
                    "ENTREPRENEURIAL STUDIES",
                    "HUMAN RESOURCE MANAGEMENT",
                    "MARKETING",
                ]
            )
        elif i == 8:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ENVIRONMENTAL MANAGEMENT AND TOXICOLOGY",
                    "FORESTRY AND ENVIRONMENTAL MANAGEMENT",
                    "FISHERIES AND AQUATIC RESOURCES MANAGEMENT",
                ]
            )
        elif i == 9:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "BIOCHEMISTRY",
                    "MICROBIOLOGY",
                    "PLANT SCIENCE AND BIOTECHNOLOGY",
                    "ZOOLOGY AND ENVIRONMENTAL BIOLOGY",
                ]
            )

        elif i == 10:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "CHEMISTRY",
                    "PHYSICS",
                    "COMPUTER SCIENCE",
                    "STATISTICS",
                    "MATHEMATICS",
                ]
            )

        elif i == 11:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "VERTINARY ANATOMY",
                    "VERTINARY MEDICINE",
                    "VERTINARY PUBLIC HEALTH AND PREVENTIVE MEDICINE",
                ]
            )

    def register_student_details(self):
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
        jamb_number = self.comp.j_num_input.text()
        college = self.comp.college_select.currentText()
        dept = self.comp.dept_select.currentText()
        level = self.comp.level_select.currentText()
        matric_number = self.comp.m_num_input.text()
        date_of_reg = self.comp.dor_text.text()

        self.comp.datab.cur.execute(
            "CREATE TABLE IF NOT EXISTS Students (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255) NOT NULL, middle_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL, age INT(3) NOT NULL,date_of_birth VARCHAR(10) NOT NULL, gender VARCHAR(6) NOT NULL,jamb_number VARCHAR(10) NOT NULL, college VARCHAR(255) NOT NULL, dept VARCHAR(255) NOT NULL, level VARCHAR(4) NOT NULL,matric_number VARCHAR(255) NOT NULL, date_of_reg VARCHAR(255) NOT NULL)"
        )
        self.comp.datab.cur.execute(
            f"INSERT INTO Students(first_name, middle_name, last_name,date_of_birth, age, gender, jamb_number,college,dept,level,matric_number,date_of_reg) VALUES('{first_name}','{middle_name}','{last_name}','{date_of_birth}',{int(age)},'{gender}','{jamb_number}','{college}','{dept}','{level}','{matric_number}','{date_of_reg}')"
        )

        self.register_faces()
        self.comp.datab.conn.commit()
        self.close()

    def register_faces(self):
        self.comp.datab.cur.execute("SELECT * FROM Students")

        id_count = 0
        for row in self.comp.datab.cur:
            _id = row[0]
            name = f"{row[3]}_{row[1]}".lower()

        face_cascade = cv2.CascadeClassifier(
            "./assets/classifiers/haarcascade_frontalface_alt2.xml" 
        )

        cam = cv2.VideoCapture(0)
        sample_number = 0

        time.sleep(2.0)

        while True:
            # Capture Image-by-Image
            ret, image = cam.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.5,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE,
            )
            for (x, y, w, h) in faces:
                roi_gray = gray[y : y + h, x : x + w]
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 1)

            cv2.imshow("Register Face", image)

            if cv2.waitKey(1) & 0xFF == 255:
                sample_number += 1
                if not os.path.exists(f"./assets/face_data/student/{str(name)}"):
                    os.makedirs(f"./assets/face_data/student/{str(name)}")
                cv2.imwrite(
                    f"./assets/face_data/student/{str(name)}/{str(name)}.{str(sample_number)}.jpg",
                    roi_gray,
                )
            elif sample_number == 20:
                break

        cam.release()
        train(_id,name)
        cv2.destroyAllWindows()
        self.comp.datab.conn.close()
