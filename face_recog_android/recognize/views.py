import os
from PIL import Image
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import viewsets
from django.conf import settings as django_settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import STUDENT_SERIALIZERS, STAFF_SERIALIZERS
from .details.recognize import _recog_stud, _recog_staf
from .models import STUDENTS, STAFF
from django.conf import settings as django_settings


# create views
@api_view(["GET"])
def index(request):
    students = STUDENTS.objects.all()

    serializer = STUDENT_SERIALIZERS(students, many=True, context={"request": request})

    return Response(serializer.data)


@api_view(["POST"])
@csrf_exempt
def _verify_stud(request):
    students = STUDENTS.objects.all()

    serializer = STUDENT_SERIALIZERS(students, many=True, context={"request": request})

    if request.method == "POST":
        image_file = request.FILES["image"]

        count = -1
        for student in students:
            count += 1

            image_processed = _recog_stud(student, image_file)

            if image_processed == serializer.data[count]["id"]:
                return Response(serializer.data[count])
            else:
                photo = f"{django_settings.MEDIA_ROOT}unknown_user.jpeg"
                response = HttpResponse(
                    open(photo, "rb").read(), content_type="image/jpeg"
                )
                return response


@api_view(["POST"])
@csrf_exempt
def _verify_staff(request):
    staff = STAFF.objects.all()

    serializer = STAFF_SERIALIZERS(staff, many=True, context={"request": request})

    if request.method == "POST":
        image_file = request.FILES["image"]

        count = -1
        for staf in staff:
            count += 1

            image_processed = _recog_staf(staff, image_file)

            if image_processed == serializer.data[count]["id"]:
                return Response(serializer.data[count])
            else:
                photo = f"{django_settings.MEDIA_URL}unknown_user.jpeg"
                response = HttpResponse(
                    open(photo, "rb").read(), content_type="image/jpeg"
                )
                return response


def show_full_details_student(request):
    if request.method == "GET":
        pdf = f"{django_settings.MEDIA_URL}pdf/student_detail.pdf"
        response = HttpResponse(pdf, content_type="application/pdf")
        response[
            "Content-Disposition"
        ] = 'attachment;filename="student_full_details.pdf"'
        return response


def show_full_details_staff(request):
    if request.method == "GET":
        pdf = f"{django_settings.MEDIA_URL}pdf/staff_detail.pdf"
        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = 'attachment;filename="staff_full_details.pdf"'
        return response
