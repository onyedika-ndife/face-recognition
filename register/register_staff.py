from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class REGISTER_STAFF(QDialog):
    def __init__(self, components):
        super().__init__()
        self.setStyleSheet(open("./assets/css/main.css").read())
        self.setWindowTitle("REGISTER STAFF")
        self.resize(550, 400)

        self.comp = components()

        self.setupUI()

    def setupUI(self):

        # ADDING WIDGETS
        self.comp.main_grid.addWidget(self.comp.f_name, 0, 0)
        self.comp.main_grid.addWidget(self.comp.f_name_input, 0, 1)

        self.comp.main_grid.addWidget(self.comp.m_name, 1, 0)
        self.comp.main_grid.addWidget(self.comp.m_name_input, 1, 1)

        self.comp.main_grid.addWidget(self.comp.l_name, 2, 0)
        self.comp.main_grid.addWidget(self.comp.l_name_input, 2, 1)

        self.comp.main_grid.addWidget(self.comp.age, 3, 0)
        self.comp.main_grid.addWidget(self.comp.age_input, 3, 1)

        self.comp.main_grid.addWidget(self.comp.gender, 4, 0)
        self.comp.main_grid.addLayout(self.comp.gender_layout, 4, 1)

        self.comp.main_grid.addWidget(self.comp.dor, 5, 0)
        self.comp.main_grid.addWidget(self.comp.dor_text, 5, 1)

        self.comp.main_grid.addWidget(self.comp._next, 6, 0, 1, 0)

        self.comp._next.setText("Next")

        self.setLayout(self.comp.main_grid)

        # When next button is clicked
        self.comp._next.clicked.connect(self.register_staff_details)

    def register_staff_details(self):
        first_name = self.f_name_input.text()
        middle_name = self.m_name_input.text()
        last_name = self.l_name_input.text()
        age = self.age_input.text()
        gender = self.gender_select.text()
        date_of_reg = self.dor_text.text()

        # self.datab.cur.execute(
        #     "CREATE TABLE IF NOT EXISTS Staffs (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255) NOT NULL, middle_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL, age INT(3) NOT NULL, gender VARCHAR(6) NOT NULL, date_of_reg VARCHAR(255) NOT NULL)"
        # )
        # self.datab.cur.execute(
        #     f"INSERT INTO Users(first_name, middle_name, last_name, age, gender, jamb_number,matric_number,date_of_reg) VALUES('{first_name}','{middle_name}','{last_name}',{int(age)},'{gender}','{date_of_reg}')"
        # )
        # self.datab.conn.commit()
        print(first_name)

