import io
import os

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

from register.register_main import REGISTER_MAIN
from database.db import Database

class VIEW_DETAILS(QMainWindow):
    datab = Database()
    def __init__(self, title,prev_scrn, profile, main_layout):
        super().__init__()
        self.title = title
        self.title.setWindowTitle("VIEW STAFF DETAILS")

        self.main_layout = main_layout

        self.previous = prev_scrn

        self.MAIN_VIEW(profile)   

    def MAIN_VIEW(self, profile):
        components = REGISTER_MAIN.components

        comp = REGISTER_MAIN.components()

        comp.datab.cur.execute(f"SELECT * FROM recognize_staff WHERE id = '{profile[0]}'")
        
        self.profile = comp.datab.cur.fetchone()

        self.main_menu = self.menuBar()
        self.toolbar = QToolBar()

        self.file_menu = self.main_menu.addMenu("File")
        self.edit_menu = self.main_menu.addMenu("Edit")

        self.save_action = QAction(
            QIcon("./assets/img/Save.png"), "Save File", self
        )
        self.save_action.setShortcut("Ctrl+S")

        self.edit_action = QAction(
            QIcon("./assets/img/Edit Details.png"), "Edit Student Details", self
        )

        self.exit_action = QAction(
            QIcon("./assets/img/Exit.png"), "Exit", self
        )
        self.exit_action.setShortcut("Ctrl+Q")

        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.exit_action)

        self.edit_menu.addAction(self.edit_action)

        self.save_action.triggered.connect(self._save_file)
        self.edit_action.triggered.connect(self._edit_screen)
        self.exit_action.triggered.connect(self.previous)

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(self.exit_action)
        self.toolbar.addAction(self.edit_action)
        self.toolbar.addAction(self.save_action)

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
        self.l_name_text.setText(self.profile[3])


        self.pd_detail_view.addWidget(comp.m_name, 1, 0)
        self.m_name_text = QLabel()
        self.pd_detail_view.addWidget(self.m_name_text, 1, 1)
        self.m_name_text.setText(self.profile[2])

        self.pd_detail_view.addWidget(comp.f_name, 2, 0)
        self.f_name_text = QLabel()
        self.pd_detail_view.addWidget(self.f_name_text, 2, 1)
        self.f_name_text.setText(self.profile[1])

        self.pd_detail_view.addWidget(comp.profession, 3, 0)
        self.profession_text = QLabel()
        self.pd_detail_view.addWidget(self.profession_text, 3, 1)
        self.profession_text.setText(self.profile[11])

        self.pd_detail_view.addWidget(comp.age, 4, 0)
        self.age_text = QLabel()
        self.pd_detail_view.addWidget(self.age_text, 4, 1)
        self.age_text.setText(str(self.profile[4]))

        for image in os.listdir('./face_recog_android/media/image/staff'):
            name = f"{self.profile[3]}_{self.profile[1]}".lower()
            folder_name = image
            if folder_name == name:
                pic = QImage(f'./face_recog_android/media/image/staff/{folder_name}/{folder_name}.jpg')
                comp.profile_pic.setPixmap(QPixmap.fromImage(pic))


        comp.main_grid.addWidget(comp.dob_label, 1, 0)
        self.dob_text = QLabel()
        comp.main_grid.addWidget(self.dob_text, 1, 1)
        self.dob_text.setText(str(self.profile[5]))

        comp.main_grid.addWidget(comp.gender, 2, 0)
        self.gender_text = QLabel()
        comp.main_grid.addWidget(self.gender_text, 2, 1)
        self.gender_text.setText(self.profile[6])


        comp.main_grid.addWidget(comp.nationality, 3, 0)
        self.nationality_text = QLabel()
        comp.main_grid.addWidget(self.nationality_text, 3, 1)
        self.nationality_text.setText(self.profile[7])


        comp.main_grid.addWidget(comp.state_origin, 4, 0)
        self.state_origin_text = QLabel()
        comp.main_grid.addWidget(self.state_origin_text, 4, 1)
        self.state_origin_text.setText(self.profile[8])


        comp.main_grid.addWidget(comp.lga_origin, 5, 0)
        self.lga_origin_text = QLabel()
        comp.main_grid.addWidget(self.lga_origin_text, 5, 1)
        self.lga_origin_text.setText(self.profile[9])


        comp.main_grid.addWidget(comp.marital, 6, 0)
        self.marital_text = QLabel()
        comp.main_grid.addWidget(self.marital_text, 6, 1)
        self.marital_text.setText(self.profile[10])

        self.vbox.addWidget(comp.main_group_box)

    def contact_details(self,component):
        comp = component()

        comp.main_group_box.setTitle('Contact Details')

        comp.main_grid.addWidget(comp.address, 0,0)
        self.address_text = QLabel()
        comp.main_grid.addWidget(self.address_text, 0,1)
        self.address_text.setText(self.profile[12])

        comp.main_grid.addWidget(comp.phone, 1,0)
        self.phone_text = QLabel()
        comp.main_grid.addWidget(self.phone_text, 1,1)
        self.phone_text.setText(self.profile[13])


        comp.main_grid.addWidget(comp.email, 2,0)
        self.email_text = QLabel()
        comp.main_grid.addWidget(self.email_text, 2,1)
        self.email_text.setText(self.profile[14])

        self.vbox.addWidget(comp.main_group_box)



    def other_detail(self, component):
        comp = component()

        comp.main_grid.addWidget(comp.dor, 0,0)
        self.dor_text = QLabel()
        comp.main_grid.addWidget(self.dor_text, 0,1)
        self.dor_text.setText(str(self.profile[15]))


        self.vbox.addWidget(comp.main_group_box)

    def _create_pdf(self):
        packet_1 = io.BytesIO()
        can_1 = canvas.Canvas(packet_1, pagesize=A4)

        for image in os.listdir('./face_recog_android/media/image/staff'):
            name = f"{self.profile[3]}_{self.profile[1]}".lower()
            folder_name = image
            if folder_name == name:
                pic = f'./face_recog_android/media/image/staff/{folder_name}/{folder_name}.jpg'
                can_1.drawInlineImage(pic,446,540, width=3.7*cm,height=3.7*cm)

        can_1.setFont("Helvetica", 10)
        # # last_name
        can_1.drawString(270, 626, self.l_name_text.text())
        
        # # middle_name
        can_1.drawString(270, 588, self.m_name_text.text())
        
        # # first_name
        can_1.drawString(270, 550, self.f_name_text.text())

        # # profession
        can_1.drawString(158, 510, self.profession_text.text())

        # # age
        can_1.drawString(158, 480, self.age_text.text())
        
        # # gender
        can_1.drawString(158, 448, self.gender_text.text())
        
        # # dob
        can_1.drawString(158, 404, self.dob_text.text()[8:])
        can_1.drawString(295, 404, self.dob_text.text()[5:7])
        can_1.drawString(429, 404, self.dob_text.text()[:4])
        
        # # nationality
        can_1.drawString(158, 360, self.nationality_text.text())
        
        # # state of origin
        can_1.drawString(158, 328, self.state_origin_text.text())
        
        # # Marital status
        can_1.drawString(158, 284, self.marital_text.text())

        # # cell phone
        can_1.drawString(240, 160, self.phone_text.text())

        # m dor
        can_1.drawString(216, 56, self.dor_text.text())


        can_1.setFont("Helvetica", 9)
        # # lga_origin
        can_1.drawString(364, 328, self.lga_origin_text.text())
        # # home address
        can_1.drawString(240, 190, self.address_text.text())
        # # email
        can_1.drawString(240, 130, self.email_text.text())


        can_1.save()

        # move to the beginning of the StringIO buffer
        packet_1.seek(0)
        new_pdf_1 = PdfFileReader(packet_1)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("./face_recog_android/assets/doc/staff_details.pdf", "rb"))
        self.output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page_1 = existing_pdf.getPage(0)

        page_1.mergePage(new_pdf_1.getPage(0))

        self.output.addPage(page_1)

    def _save_file(self):
        self._create_pdf()

        name = QFileDialog.getSaveFileName(self, filter='(*.pdf)')

        file_name = f"{name[0]}"

        if file_name.endswith('.pdf'):
            file = file_name.replace('.pdf','')
        else:
            file = file_name

        outputStream = open(f"{file}.pdf", "wb")
        self.output.write(outputStream)
        outputStream.close()

    def _edit_screen(self):
        from staff_detail.edit_details import EDIT_DETAILS

        edit_details = EDIT_DETAILS(self.title, self.previous, self.profile, self.main_layout)