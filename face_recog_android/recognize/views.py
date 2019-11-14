import json
import os
import urllib
import face_recognition

import cv2
import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings as django_settings
from .models import STUDENTS
from .details.recognize import _recog


# create views


@csrf_exempt
def _upload(request):
    students = STUDENTS.objects.all()

    if request.method == "POST":
        image_file = request.FILES["image"]

        image = cv2.imdecode(
            np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED
        )

        image_processed = _recog(students, image)

        return JsonResponse(image_processed)

