import os

import requests
from PIL import Image
from PyQt5.Qt import QFileInfo
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QSize, QTimer, QUrl
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import (
    QAction,
    QFileDialog,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QToolBar,
    QVBoxLayout,
    QWidget,
    QTextEdit,
    QDialog,
)

from register.register_main import REGISTER_MAIN

APP_URL = "http://127.0.0.1:8000"
# APP_URL = "https://face-recog-server.herokuapp.com"
class VIEW_DETAILS(QMainWindow):
    def __init__(self, title, prev_scrn, profile, main_layout):
        super().__init__()
        self.title = title
        self.title.setWindowTitle("VIEW STAFF DETAILS")

        self.main_layout = main_layout

        self.previous = prev_scrn

        self.MAIN_VIEW(profile)

    def MAIN_VIEW(self, profile):
        components = REGISTER_MAIN.components

        comp = REGISTER_MAIN.components()

        _id = int(profile["id"])

        r = requests.get(url=f"{APP_URL}/users/staff/{_id}")

        self.profile = r.json()

        self.main_menu = self.menuBar()
        self.toolbar = QToolBar()

        self.file_menu = self.main_menu.addMenu("File")
        self.edit_menu = self.main_menu.addMenu("Edit")

        self.export = QAction(
            QIcon("./assets/icons/export_pdf.png"), "Export PDF", self
        )
        self.export.setShortcut("Ctrl+S")

        self.edit_action = QAction(
            QIcon("./assets/icons/edit_profile.png"), "Edit Student Details", self
        )

        self.exit_action = QAction(QIcon("./assets/icons/exit.png"), "Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")

        self.file_menu.addAction(self.export)
        self.file_menu.addAction(self.exit_action)

        self.edit_menu.addAction(self.edit_action)

        self.export.triggered.connect(self._save_file)
        self.edit_action.triggered.connect(self._edit_screen)
        self.exit_action.triggered.connect(self.previous)

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(self.exit_action)
        self.toolbar.addAction(self.edit_action)
        self.toolbar.addAction(self.export)

        self.main_widget = QWidget()
        self.vbox = QVBoxLayout()

        self.personal_details(components)

        self.contact_details(components)

        self.other_detail(components)

        self.main_widget.setLayout(self.vbox)

        self.scroll = QScrollArea()
        self.scroll.setWidget(self.main_widget)
        self.scroll.setWidgetResizable(True)

        self.setCentralWidget(self.scroll)

        self.main_layout.addWidget(self)
        self.main_layout.setCurrentWidget(self)

    def personal_details(self, component):
        comp = component()

        comp.main_group_box.setTitle("Personal Details")

        # for views containing school detail of student
        self.pd_view = QHBoxLayout()
        self.pd_detail_view = QGridLayout()

        comp.main_grid.addLayout(self.pd_view, 0, 0, 1, 0)

        self.pd_view.addLayout(self.pd_detail_view)
        self.pd_view.addWidget(comp.profile_pic)

        self.pd_detail_view.addWidget(comp.l_name, 0, 0)
        self.l_name_text = QLabel()
        self.pd_detail_view.addWidget(self.l_name_text, 0, 1)
        self.l_name_text.setText(self.profile["last_name"])

        self.pd_detail_view.addWidget(comp.m_name, 1, 0)
        self.m_name_text = QLabel()
        self.pd_detail_view.addWidget(self.m_name_text, 1, 1)
        self.m_name_text.setText(self.profile["middle_name"])

        self.pd_detail_view.addWidget(comp.f_name, 2, 0)
        self.f_name_text = QLabel()
        self.pd_detail_view.addWidget(self.f_name_text, 2, 1)
        self.f_name_text.setText(self.profile["first_name"])

        self.pd_detail_view.addWidget(comp.profession, 3, 0)
        self.profession_text = QLabel()
        self.pd_detail_view.addWidget(self.profession_text, 3, 1)
        self.profession_text.setText(self.profile["profession"])

        self.pd_detail_view.addWidget(comp.age, 4, 0)
        self.age_text = QLabel()
        self.pd_detail_view.addWidget(self.age_text, 4, 1)
        self.age_text.setText(str(self.profile["age"]))

        r = requests.get(url=self.profile["pic"], stream=True)

        pic = QImage()
        pic.loadFromData(r.content)

        comp.profile_pic.setPixmap(QPixmap.fromImage(pic))

        comp.main_grid.addWidget(comp.dob_label, 1, 0)
        self.dob_text = QLabel()
        comp.main_grid.addWidget(self.dob_text, 1, 1)
        self.dob_text.setText(str(self.profile["date_of_birth"]))

        comp.main_grid.addWidget(comp.gender, 2, 0)
        self.gender_text = QLabel()
        comp.main_grid.addWidget(self.gender_text, 2, 1)
        self.gender_text.setText(self.profile["gender"])

        comp.main_grid.addWidget(comp.nationality, 3, 0)
        self.nationality_text = QLabel()
        comp.main_grid.addWidget(self.nationality_text, 3, 1)
        self.nationality_text.setText(self.profile["nationality"])

        comp.main_grid.addWidget(comp.state_origin, 4, 0)
        self.state_origin_text = QLabel()
        comp.main_grid.addWidget(self.state_origin_text, 4, 1)
        self.state_origin_text.setText(self.profile["state_of_origin"])

        comp.main_grid.addWidget(comp.lga_origin, 5, 0)
        self.lga_origin_text = QLabel()
        comp.main_grid.addWidget(self.lga_origin_text, 5, 1)
        self.lga_origin_text.setText(self.profile["lga_origin"])

        comp.main_grid.addWidget(comp.marital, 6, 0)
        self.marital_text = QLabel()
        comp.main_grid.addWidget(self.marital_text, 6, 1)
        self.marital_text.setText(self.profile["marital_status"])

        self.vbox.addWidget(comp.main_group_box)

    def contact_details(self, component):
        comp = component()

        comp.main_group_box.setTitle("Contact Details")

        comp.main_grid.addWidget(comp.address, 0, 0)
        self.address_text = QLabel()
        comp.main_grid.addWidget(self.address_text, 0, 1)
        self.address_text.setText(self.profile["address"])

        comp.main_grid.addWidget(comp.phone, 1, 0)
        self.phone_text = QLabel()
        comp.main_grid.addWidget(self.phone_text, 1, 1)
        self.phone_text.setText(self.profile["phone_number"])

        comp.main_grid.addWidget(comp.email, 2, 0)
        self.email_text = QLabel()
        comp.main_grid.addWidget(self.email_text, 2, 1)
        self.email_text.setText(self.profile["email"])

        self.vbox.addWidget(comp.main_group_box)

    def other_detail(self, component):
        comp = component()

        comp.main_grid.addWidget(comp.dor, 0, 0)
        self.dor_text = QLabel()
        comp.main_grid.addWidget(self.dor_text, 0, 1)
        self.dor_text.setText(str(self.profile["date_of_registration"]))

        self.vbox.addWidget(comp.main_group_box)

    def _save_file(self):
        r = requests.get(url=f"{APP_URL}/recognize/d_staf/")

        name = QFileDialog.getSaveFileName(self, "Export PDF", filter="(*.pdf)")

        file_name = f"{name[0]}"

        if file_name.endswith(".pdf"):
            file = file_name.replace(".pdf", "")
        else:
            file = file_name

        if file != "":
            with open(f"{file}.pdf", "wb") as outputStream:
                outputStream.write(r.content)
                outputStream.close()
        else:
            file = "Staff_Details"

    def _edit_screen(self):
        from staff_detail.edit_details import EDIT_DETAILS

        edit_details = EDIT_DETAILS(
            self.title, self.previous, self.profile, self.main_layout
        )

