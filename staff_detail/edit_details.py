import io

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from register.register_main import REGISTER_MAIN
from register.register_students import REGISTER_STUDENT
from database.db import Database

class EDIT_DETAILS(QMainWindow):
    datab = Database()
    def __init__(self, title, prev_scrn, profile, main_layout):
        super().__init__()
        self.title = title
        self.title.setWindowTitle("EDIT STUDENT DETAILS")
        
        self.main_layout = main_layout

        self.previous = prev_scrn

        self.MAIN_VIEW(profile)

    def MAIN_VIEW(self, profile):
        self.comp = REGISTER_MAIN.components()

        self.comp.datab.cur.execute(f"SELECT * FROM recognize_staff WHERE id = '{profile[0]}'")
        self.profile = self.comp.datab.cur.fetchone()

        self.main_menu = self.menuBar()
        self.toolbar = QToolBar()

        self.file_menu = self.main_menu.addMenu("File")

        self.save_action = QAction(
            QIcon("./assets/img/Save.png"), "Save File", self
        )
        self.save_action.setShortcut("Ctrl+S")

        self.exit_action = QAction(
            QIcon("./assets/img/Exit.png"), "Exit", self
        )
        self.exit_action.setShortcut("Ctrl+Q")

        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.exit_action)

        self.save_action.triggered.connect(self._save_as_file)
        self.exit_action.triggered.connect(lambda: self.previous())

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(self.exit_action)
        self.toolbar.addAction(self.save_action)

        self.main_widget = QWidget()
        self.vbox = QVBoxLayout()

        self.personal_details()

        self.contact_details()

        self.parent_detail()

        self.other_detail()

        self.main_widget.setLayout(self.vbox)


        self.scroll = QScrollArea()
        self.scroll.setWidget(self.main_widget)
        self.scroll.setWidgetResizable(True)

        self.setCentralWidget(self.scroll)

        self.main_layout.addWidget(self)
        self.main_layout.setCurrentWidget(self)

    def personal_details(self):
        _group_box = QGroupBox("Personal Details")
        _grid = QGridLayout()

        _group_box.setLayout(_grid)

        # for views containing school detail of student
        self.sd_view = QHBoxLayout()
        self.sd_detail_view = QGridLayout()

        _grid.addLayout(self.sd_view, 0, 0, 1, 0)

        self.sd_view.addLayout(self.sd_detail_view)
        self.sd_view.addWidget(self.comp.profile_pic)
        self.comp.profile_pic.setMaximumWidth(220)

        self.sd_detail_view.addWidget(self.comp.m_num, 0, 0)
        self.sd_detail_view.addWidget(self.comp.m_num_input , 0, 1)
        self.comp.m_num_input.setText(self.profile[15])

        self.sd_detail_view.addWidget(self.comp.j_num, 1, 0)
        self.sd_detail_view.addWidget(self.comp.j_num_input, 1, 1)
        self.comp.j_num_input.setText(self.profile[11])

        self.sd_detail_view.addWidget(self.comp.college, 2, 0)
        self.sd_detail_view.addWidget(self.comp.college_select, 2, 1)
        self.comp.college_select.setCurrentText(self.profile[12])
        self.school()
        self.comp.college_select.currentIndexChanged.connect(lambda:REGISTER_STUDENT.school(self,self.comp.college_select.currentIndex()))

        self.sd_detail_view.addWidget(self.comp.dept, 3, 0)
        self.sd_detail_view.addWidget(self.comp.dept_select, 3, 1)
        self.comp.dept_select.setCurrentText(self.profile[13])

        self.sd_detail_view.addWidget(self.comp.level, 4, 0)
        self.sd_detail_view.addWidget(self.comp.level_select, 4, 1)
        self.comp.level_select.setCurrentText(self.profile[14])

        self.pd_detail_view = QGridLayout()
        self.name = QLabel("Name:")
        self.name.setObjectName('Label')

        _grid.addWidget(self.name, 1, 0)

        self.pd_detail_view.addWidget(self.comp.l_name, 0, 0)
        self.pd_detail_view.addWidget(self.comp.l_name_input, 0, 1)
        self.comp.l_name_input.setText(self.profile[3])


        self.pd_detail_view.addWidget(self.comp.m_name, 1, 0)
        self.pd_detail_view.addWidget(self.comp.m_name_input, 1, 1)
        self.comp.m_name_input.setText(self.profile[2])


        self.pd_detail_view.addWidget(self.comp.f_name, 2, 0)
        self.pd_detail_view.addWidget(self.comp.f_name_input, 2, 1)
        self.comp.f_name_input.setText(self.profile[1])

        _grid.addLayout(self.pd_detail_view, 1, 1)

        _grid.addWidget(self.comp.age, 2, 0)
        _grid.addWidget(self.comp.age_input, 2, 1)
        self.comp.age_input.setText(str(self.profile[4]))

        _grid.addWidget(self.comp.gender, 3, 0)
        _grid.addLayout(self.comp.gender_layout, 3, 1)
        if self.comp.gender_1.text() == self.profile[6].upper():
            self.comp.gender_1.setChecked(True)
        else:
            self.comp.gender_2.setChecked(True)


        _grid.addWidget(self.comp.dob_label, 4, 0)
        _grid.addLayout(self.comp.dob_layout, 4, 1)
        self.comp.dob_date_label.setText(self.profile[5])


        _grid.addWidget(self.comp.nationality, 5, 0)
        _grid.addWidget(self.comp.nationality_input, 5, 1)
        self.comp.nationality_input.setText(self.profile[7])


        _grid.addWidget(self.comp.state_origin, 6, 0)
        _grid.addWidget(self.comp.state_origin_input, 6, 1)
        self.comp.state_origin_input.setText(self.profile[8])


        _grid.addWidget(self.comp.lga_origin, 7, 0)
        _grid.addWidget(self.comp.lga_origin_input, 7, 1)
        self.comp.lga_origin_input.setText(self.profile[9])


        _grid.addWidget(self.comp.marital, 8, 0)
        _grid.addWidget(self.comp.marital_select, 8, 1)
        self.comp.marital_select.setCurrentText(self.profile[10])

        self.vbox.addWidget(_group_box)

    def contact_details(self):
        _group_box = QGroupBox('Contact Details')
        _grid = QGridLayout()

        _group_box.setLayout(_grid)

        _grid.addWidget(self.comp.address, 0,0)
        _grid.addWidget(self.comp.address_input, 0,1)
        self.comp.address_input.setText(self.profile[12])

        _grid.addWidget(self.comp.phone, 1,0)
        _grid.addWidget(self.comp.phone_input, 1,1)
        self.comp.phone_input.setText(self.profile[13])


        _grid.addWidget(self.comp.email, 2,0)
        _grid.addWidget(self.comp.email_input, 2,1)
        self.comp.email_input.setText(self.profile[14])

        self.vbox.addWidget(_group_box)

    def work_details(self):
        _group_box = QGroupBox('Work Details')
        _grid = QGridLayout()

        _group_box.setLayout(_grid)

        _grid.addWidget(self.comp.profession, 0,0)
        _grid.addWidget(self.comp.profession_input, 0,1)
        self.comp.profession_input.setText(self.profile[11])

    def other_detail(self):
        _grid = QGridLayout()

        _grid.addWidget(self.comp.dor, 0,0)
        self.dor_text = QLabel()
        _grid.addWidget(self.dor_text, 0,1)
        self.dor_text.setText(self.profile[15])

        _group_box.setLayout(_grid)


        self.vbox.addWidget(_group_box)

        self.save_2_db = QPushButton('SAVE')
        self.save_2_db.setIcon(QIcon('./assets/img/Save_DB.png'))
        self.save_2_db.setIconSize(QSize(20,20))

        self.vbox.addWidget(self.save_2_db)

        self.save_2_db.clicked.connect(self._save)


    def _save_2_db(self):
        _id = int(self.profile[0])

        # Assigning Variables
        first_name = self.comp.f_name_input.text()
        middle_name = self.comp.m_name_input.text()
        last_name = self.comp.l_name_input.text()
        age = int(self.comp.age_input.text())
        date_of_birth = self.comp.dob_date_label.text()
        gender = (
            self.comp.gender_1.text()
            if self.comp.gender_1.isChecked()
            else self.comp.gender_2.text()
        )
        nationality = self.comp.nationality_input.text()
        state_of_origin = self.comp.state_origin_input.text()
        lga_origin = self.comp.lga_origin_input.text()
        marital = self.comp.marital_select.currentText()
        # Assigning Variables
        profession = self.comp.profession_input.text()
        # Assigning Variables
        address = self.comp.address_input.text()
        phone = self.comp.phone_input.text()
        email = self.comp.email_input.text()
        

        self.comp.datab.cur.execute(f"UPDATE recognize_staff SET first_name = '{first_name}', middle_name = '{middle_name}', last_name = '{last_name}',age = '{age}',date_of_birth = '{date_of_birth}', gender = '{gender}', nationality = '{nationality}', state_of_origin = '{state_of_origin}', lga_origin = '{lga_origin}',marital_status = '{marital}', profession = '{profession}',address = '{address}',phone_number = '{phone}',email = '{email}' WHERE ID = '{_id}'")

        self.comp.datab.conn.commit()
        self.comp.datab.cur.close()

    def _save(self):
        self._save_2_db()
        self.previous()

    def _save_as_file(self):
        self._save_2_db()
        self._verify_screen()

    def _verify_screen(self):
        from student_detail.view_details import VIEW_DETAILS

        view_details = VIEW_DETAILS(self.title, self.previous, self.profile, self.main_layout)
