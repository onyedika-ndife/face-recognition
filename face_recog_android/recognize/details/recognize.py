import cv2
import numpy as np
import os
import json

from imutil import Image
from django.conf import settings as django_settings
import face_recognition
from .create_pdf import _create_stud_pdf


def _recog_stud(student, image):

    img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    known_face_encodings = []
    known_face_id = []

    known_id = student.id
    name = f"{student.last_name}_{student.first_name}".lower()

    for image in os.listdir(f"{django_settings.MEDIA_ROOT}image/student/{name}"):
        _image = face_recognition.load_image_file(
            f"{django_settings.MEDIA_ROOT}image/student/{name}/{image}"
        )
        _image_face_encoding = face_recognition.face_encodings(_image)[0]

        # Create arrays of known face encodings and their ids
        known_face_encodings.append(_image_face_encoding)
        known_face_id.append(known_id)

    # img = cv2.resize(in_img, (0, 0), fx=0.25, fy=0.25)

    unknown_image = img[:, :, ::-1]
    # unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(
        face_locations, face_encodings
    ):

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(
            known_face_encodings, face_encoding
        )

        _id = None

        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            _id = known_face_id[best_match_index]

            if student.id == _id:
                _create_stud_pdf(student)
                return student.id
        else:
            # Scale back up face locations since the self.image we detected in was scaled to 1/4 size
            # top *= 4
            # right *= 4
            # bottom *= 4
            # left *= 4

            # Draw a box around the face
            a = cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 1)

            # Draw a label with a name below the face
            b = cv2.rectangle(
                img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED
            )

            c = cv2.putText(
                img,
                f"Unknown",
                (left + 6, bottom - 6),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

            d = cv2.imwrite(f"{django_settings.MEDIA_ROOT}unknown_user.jpeg", img)

            return "Unknown Individual"


def _recog_staf(staff, image):

    img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    known_face_encodings = []
    known_face_id = []

    known_id = staff.id
    name = f"{staff.last_name}_{staff.first_name}".lower()

    for image in os.listdir(f"{django_settings.MEDIA_ROOT}image/staff/{name}"):
        _image = face_recognition.load_image_file(
            f"{django_settings.MEDIA_ROOT}image/staff/{name}/{image}"
        )
        _image_face_encoding = face_recognition.face_encodings(_image)[0]

        # Create arrays of known face encodings and their ids
        known_face_encodings.append(_image_face_encoding)
        known_face_id.append(known_id)

    # img = cv2.resize(in_img, (0, 0), fx=0.25, fy=0.25)

    unknown_image = img[:, :, ::-1]
    # unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(
        face_locations, face_encodings
    ):

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(
            known_face_encodings, face_encoding
        )

        _id = None

        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            _id = known_face_id[best_match_index]

            if staff.id == _id:
                _create_stud_pdf(staff)
                return staff.id
        else:
            # Scale back up face locations since the self.image we detected in was scaled to 1/4 size
            # top *= 4
            # right *= 4
            # bottom *= 4
            # left *= 4

            # Draw a box around the face
            a = cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 1)

            # Draw a label with a name below the face
            b = cv2.rectangle(
                img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED
            )

            c = cv2.putText(
                img,
                f"Unknown",
                (left + 6, bottom - 6),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

            d = cv2.imwrite(f"{django_settings.MEDIA_ROOT}unknown_user.jpeg", img)

            return "Unknown Individual"
