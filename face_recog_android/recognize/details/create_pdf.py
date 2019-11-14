import io
import os

from PyPDF2 import PdfFileReader, PdfFileWriter
from django.conf import settings as django_settings
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


def _create_pdf(student):
    packet_1 = io.BytesIO()
    packet_2 = io.BytesIO()
    can_1 = canvas.Canvas(packet_1, pagesize=A4)
    can_2 = canvas.Canvas(packet_2, pagesize=A4)

    for image in os.listdir(f"{django_settings.STATIC_ME}student"):
        name = f"{student.last_name}_{student.first_name}".lower()
        folder_name = image
        if folder_name == name:
            pic = f"{django_settings.STATIC_ME}student/{folder_name}/{folder_name}.jpg"

            can_1.drawInlineImage(pic, 453, 550, width=3.7 * cm, height=3.7 * cm)

    can_1.setFont("Helvetica", 10)
    # Matric no
    can_1.drawString(234, 640, student.matric_number)

    # # Jamb no
    can_1.drawString(234, 610, student.jamb_number)

    # # college
    can_1.drawString(234, 583, student.college)

    # # level
    can_1.drawString(234, 523, student.level)

    # # last_name
    can_1.drawString(370, 494, student.last_name)

    # # middle_name
    can_1.drawString(370, 464, student.middle_name)

    # # first_name
    can_1.drawString(370, 435, student.first_name)

    # # age
    can_1.drawString(234, 406, student.age)

    # # gender
    can_1.drawString(234, 376, student.gender)

    # # dob
    can_1.drawString(234, 331, student.date_of_birth[8:])
    can_1.drawString(343, 331, student.date_of_birth[5:7])
    can_1.drawString(453, 331, student.date_of_birth[:4])

    # # nationality
    can_1.drawString(234, 290, student.nationality)

    # # state of origin
    can_1.drawString(234, 259, student.state_of_origin)

    # # Marital status
    can_1.drawString(234, 218, student.marital_status)

    # # cell phone
    can_1.drawString(240, 102, student.phone_number)

    # # email
    can_1.drawString(240, 76, student.email)

    can_1.setFont("Helvetica", 9)
    # # dept
    can_1.drawString(234, 553, student.department)

    # # lga_origin
    can_1.drawString(399, 260, student.lga_origin)

    # # home address
    can_1.drawString(240, 130, student.address)

    can_1.save()

    # # set font
    can_2.setFont("Helvetica", 10)

    # # parent's name
    can_2.drawString(240, 772, student.parent_name)

    # # parent's email
    can_2.drawString(240, 744, student.parent_email)

    # # parent's cell phone
    can_2.drawString(240, 715, student.parent_phone)

    # m dor
    can_2.drawString(214, 656, student.date_of_registration)

    can_2.save()

    # move to the beginning of the StringIO buffer
    packet_1.seek(0)
    packet_2.seek(0)
    new_pdf_1 = PdfFileReader(packet_1)
    new_pdf_2 = PdfFileReader(packet_2)

    # read your existing PDF
    existing_pdf = PdfFileReader(
        open(f"{django_settings.STATIC_ME}doc/details/student-details.pdf", "rb")
    )
    output = PdfFileWriter()

    # add the "watermark" (which is the new pdf) on the existing page
    page_1 = existing_pdf.getPage(0)
    page_2 = existing_pdf.getPage(1)

    page_1.mergePage(new_pdf_1.getPage(0))
    page_2.mergePage(new_pdf_2.getPage(0))

    output.addPage(page_1)
    output.addPage(page_2)

    outputStream = open(f"{django_settings.MEDIA_ROOT}pdf/detail.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

