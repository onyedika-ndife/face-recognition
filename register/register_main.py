import os
import sys
import time

import cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from database import db

from .register_staff import REGISTER_STAFF
from .register_students import REGISTER_STUDENT


class REGISTER_MAIN(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.initial_layout = QVBoxLayout()

        self.reg_staf = QPushButton("Register Staff")
        self.reg_stud = QPushButton("Register Student")

        self.initial_layout.addWidget(self.reg_stud)
        self.initial_layout.addWidget(self.reg_staf)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.initial_layout)

        self.reg_stud.clicked.connect(lambda: self.reg_stud_win(self.components))

        self.reg_staf.clicked.connect(lambda: self.reg_staf_win(self.components))

    @classmethod
    def reg_stud_win(self, components):
        self.stud_dialog = REGISTER_STUDENT(components)
        self.flags = Qt.WindowFlags(Qt.WindowStaysOnTopHint)
        self.stud_dialog.setWindowFlags(self.flags)
        self.stud_dialog.show()

    @classmethod
    def reg_staf_win(self, components):
        self.staf_dialog = REGISTER_STAFF(components)
        self.flags = Qt.WindowFlags(Qt.WindowStaysOnTopHint)
        self.staf_dialog.setWindowFlags(self.flags)
        self.staf_dialog.show()

    class components:
        def __init__(self):
            self.datab = db.Database()
            self.main_grid = QGridLayout()

            # FIRST NAME
            self.f_name = QLabel("First Name")
            self.f_name_input = QLineEdit()

            # MIDDLE NAME
            self.m_name = QLabel("Middle Name")
            self.m_name_input = QLineEdit()

            # LAST NAME
            self.l_name = QLabel("Last Name")
            self.l_name_input = QLineEdit()

            # DATE OF BIRTH
            self.dob_label = QLabel("Date of Birth")
            self.dob_date_label = QLabel("Birthday..")
            self.dob_date_label.setStyleSheet("font-style: italic;font-weight: normal;")
            self.dob_date_choose = QPushButton("Choose Date")
            self.dob_layout = QHBoxLayout()
            # self.dob_date_choose.setStyleSheet("border-radius: initial")
            self.dob_date_choose.clicked.connect(self.calender_show)
            self.dob_layout.addWidget(self.dob_date_label)
            self.dob_layout.addWidget(self.dob_date_choose)

            # AGE
            self.age = QLabel("Age")
            self.age_input = QLineEdit()
            self.age_input.setValidator(QIntValidator())
            self.age_input.setMaxLength(3)

            # GENDER
            self.gender = QLabel("Gender")
            self.gender_1 = QRadioButton("Male")
            self.gender_2 = QRadioButton("Female")
            self.gender_1.setChecked(True)
            self.gender_layout = QHBoxLayout()
            self.gender_layout.addWidget(self.gender_1)
            self.gender_layout.addWidget(self.gender_2)

            # JAMB NUMBER
            self.j_num = QLabel("JAMB No.")
            self.j_num_input = QLineEdit()
            self.j_num_input.setMaxLength(10)

            # COLLEGE
            self.college = QLabel("College")
            self.college_select = QComboBox()
            self.college_select.addItems(
                [
                    "CAERSE",
                    "CASAP",
                    "CAFST",
                    "CCSS",
                    "COED",
                    "CEET",
                    "CGSC",
                    "COLMAS",
                    "CNREM",
                    "COLNAS",
                    "COLPAS",
                    "CVM",
                ]
            )

            # DEPARTMENT
            self.dept = QLabel("Department")
            self.dept_select = QComboBox()
            self.dept_select.addItems(
                [
                    "AGRIBUSINESS MANAGEMENT",
                    "AGRICULTURAL ECONOMICS",
                    "AGRICULTURAL EXTENSION AND RURAL SOCIOLOGY",
                ]
            )

            # LEVEL
            self.level = QLabel("Level")
            self.level_select = QComboBox()
            self.level_select.addItems(["100L", "200L", "300", "400L"])

            # MATRIC NUMBER
            self.m_num = QLabel("Matriculation No.")
            self.m_num_input = QLineEdit()

            # DATE OF REGISTRATION
            self.dor = QLabel("Date of Registration")
            self.dor_text = QLineEdit()
            date = QDate.currentDate().toString(Qt.DefaultLocaleShortDate)
            self.dor_text.setText(date)

            # Next
            self._next = QPushButton()

        def calender_show(self):

            self.initial_layout = QVBoxLayout()

            self.calender_view = QWidget()
            self.calender_view.setWindowTitle("Choose Date")

            self.calender = QCalendarWidget()
            self.calender.setGridVisible(True)

            self.flags = Qt.WindowFlags(Qt.WindowStaysOnTopHint)
            self.calender_view.setWindowFlags(self.flags)

            self.initial_layout.addWidget(self.calender)
            self.calender_view.setLayout(self.initial_layout)

            self.calender_view.show()
            self.calender_view.setGeometry(500, 200, 350, 250)

            self.calender.clicked[QDate].connect(self.select_date)

        def select_date(self):
            self.dob_date_label.setText(
                self.calender.selectedDate().toString(Qt.ISODate)
            )
            self.calender_view.hide()
