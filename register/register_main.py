from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *

from database import db

from .register_staff import REGISTER_STAFF
from .register_students import REGISTER_STUDENT


class REGISTER_MAIN(QWidget):
    def __init__(self, main_layout):
        super().__init__()
        self.main_layout = main_layout
        self.UI()

    def UI(self):
        self.initial_layout = QVBoxLayout()

        self.main_widget = QTabWidget()
        self.initial_layout.addWidget(self.main_widget)
        self.setLayout(self.initial_layout)

        self.reg_stud_win(self.main_layout, self.components)
        self.reg_staf_win(self.main_layout, self.components)

    def reg_stud_win(self, main_layout, components):
        self.stud_dialog = REGISTER_STUDENT(main_layout, components)
        self.main_widget.addTab(self.stud_dialog, "Register Student")

    def reg_staf_win(self, main_layout, components):
        self.staf_dialog = REGISTER_STAFF(main_layout, components)
        self.main_widget.addTab(self.staf_dialog, "Register Staff")

    class components:
        def __init__(self):
            self.datab = db.Database()

            self.main_vView = QVBoxLayout()
            self.main_group_box = QGroupBox()
            self.main_grid = QGridLayout()

            self.main_group_box.setLayout(self.main_grid)
            self.main_vView.addWidget(self.main_group_box)

            # PROFILE PICTURE
            self.profile_pic = QLabel()
            self.profile_pic.setAlignment(Qt.AlignCenter)
            self.profile_pic.setMaximumWidth(130)
            self.profile_pic.setMaximumHeight(130)
            self.profile_pic.setScaledContents(True)

            # FIRST NAME
            self.f_name = QLabel("First Name")
            self.f_name.setObjectName("Label")
            self.f_name_input = QLineEdit()

            # MIDDLE NAME
            self.m_name = QLabel("Middle Name")
            self.m_name.setObjectName("Label")
            self.m_name_input = QLineEdit()

            # LAST NAME
            self.l_name = QLabel("Last Name")
            self.l_name.setObjectName("Label")
            self.l_name_input = QLineEdit()

            # DATE OF BIRTH
            self.dob_label = QLabel("Date of Birth")
            self.dob_label.setObjectName("Label")
            self.dob_date_label = QLabel("Choose Date..")
            self.dob_date_label.setStyleSheet("font-weight: normal;")
            self.dob_date_choose = QPushButton()
            self.dob_date_choose.setIcon(QIcon("./assets/img/Calendar.png"))
            self.dob_date_choose.setIconSize(QSize(25,25))
            self.dob_layout = QHBoxLayout()
            self.dob_date_choose.clicked.connect(self.calender_show)
            self.dob_layout.addWidget(self.dob_date_label)
            self.dob_layout.addWidget(self.dob_date_choose)

            # AGE
            self.age = QLabel("Age")
            self.age.setObjectName("Label")
            self.age_input = QLineEdit()
            self.age_input.setValidator(QIntValidator())
            self.age_input.setMaxLength(3)

            # GENDER
            self.gender = QLabel("Gender")
            self.gender.setObjectName("Label")
            self.gender_1 = QRadioButton("MALE")
            self.gender_2 = QRadioButton("FEMALE")
            self.gender_1.setChecked(True)
            self.gender_layout = QHBoxLayout()
            self.gender_layout.addWidget(self.gender_1)
            self.gender_layout.addWidget(self.gender_2)

            # NATIONAILTY
            self.nationality = QLabel("Nationality")
            self.nationality.setObjectName("Label")
            self.nationality_input = QLineEdit()

            # STATE OF ORIGIN
            self.state_origin = QLabel("State of Origin")
            self.state_origin.setObjectName("Label")
            self.state_origin_input = QLineEdit()

            # LGA OF ORIGIN
            self.lga_origin = QLabel("LGA")
            self.lga_origin.setObjectName("Label")
            self.lga_origin_input = QLineEdit()

            # MARITAL STATUS
            self.marital = QLabel("Marital Status")
            self.marital.setObjectName("Label")
            self.marital_select = QComboBox()
            self.marital_select.addItems(
                ["SINGLE", "SEPERATED", "DIVORCED", "MARRIED", "WIDOWED"]
            )

            self.profession = QLabel("Profession")
            self.profession.setObjectName("Label")
            self.profession_input = QLineEdit()

            # JAMB NUMBER
            self.j_num = QLabel("JAMB No.")
            self.j_num.setObjectName("Label")
            self.j_num_input = QLineEdit()
            self.j_num_input.setMaxLength(10)

            # COLLEGE
            self.college = QLabel("College")
            self.college.setObjectName("Label")
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
            self.dept.setObjectName("Label")
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
            self.level.setObjectName("Label")
            self.level_select = QComboBox()
            self.level_select.addItems(["100L", "200L", "300L", "400L"])

            # MATRIC NUMBER
            self.m_num = QLabel("Matriculation No.")
            self.m_num.setObjectName("Label")
            self.m_num_input = QLineEdit()

            # HOME ADDRESS
            self.address = QLabel("Home Address")
            self.address.setObjectName("Label")
            self.address_input = QLineEdit()

            # CELL PHONE
            self.phone = QLabel("Cell Phone")
            self.phone.setObjectName("Label")
            self.phone_input = QLineEdit()
            # self.phone_input.setValidator(QIntValidator
            self.phone_input.setMaxLength(11)

            # EMAIL
            self.email = QLabel("Email")
            self.email.setObjectName("Label")
            self.email.setObjectName("Label")
            self.email_input = QLineEdit()

            # PARENT NAME
            self.p_name = QLabel("Parent's/Sponsor's Name")
            self.p_name.setObjectName("Label")
            self.p_name_input = QLineEdit()

            # PARENT EMAIL
            self.p_email = QLabel("Parent's/Sponsor's Email")
            self.p_email.setObjectName("Label")
            self.p_email_input = QLineEdit()

            # PARENT PHONE
            self.p_phone = QLabel("Parent's/Sponsor's Phone")
            self.p_phone.setObjectName("Label")
            self.p_phone_input = QLineEdit()
            self.p_phone_input.setMaxLength(11)

            # DATE OF REGISTRATION
            self.dor = QLabel("Date of Registration")
            self.dor.setObjectName("Label")
            self.dor_text = QLineEdit()
            date = QDate.currentDate().toString(Qt.DefaultLocaleShortDate)
            self.dor_text.setText(date)

            # Next
            self._next = QPushButton("Next")

            # Prev
            self._prev = QPushButton("Previous")

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
            self.calender_view.resize(350, 250)

            self.calender.clicked[QDate].connect(self.select_date)

        def select_date(self):
            self.dob_date_label.setText(
                self.calender.selectedDate().toString(Qt.ISODate)
            )
            self.calender_view.hide()
