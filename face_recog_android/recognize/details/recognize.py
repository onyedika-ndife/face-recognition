import cv2
import os
import json
from django.conf import settings as django_settings
import face_recognition
from .create_pdf import _create_pdf


def _recog(students, img):

    known_face_encodings = []
    known_face_id = []

    for student in students:
        known_id = student.id
        name = f"{student.last_name}_{student.first_name}".lower()

        for image in os.listdir(f"{django_settings}student/{name}"):
            _image = face_recognition.load_image_file(
                f"{django_settings}student/{name}/{image}"
            )
            _image_face_encoding = face_recognition.face_encodings(_image)[0]

            # Create arrays of known face encodings and their ids
            known_face_encodings.append(_image_face_encoding)
            known_face_id.append(known_id)

        unknown_image = face_recognition.load_image_file(img)
        unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings
        ):

            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding
            )

            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding
            )

            _id = None

            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                _id = known_face_id[best_match_index]

                if student.id == _id:
                    _create_pdf(student)
                    return json.dumps(f"{django_settings.MEDIA_URL}pdf/detail.pdf")
                else:
                    # Scale back up face locations since the self.image we detected in was scaled to 1/4 size

                    # Draw a box around the face
                    cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 1)

                    # Draw a label with a name below the face
                    cv2.rectangle(
                        img,
                        (left, bottom - 35),
                        (right, bottom),
                        (0, 0, 255),
                        cv2.FILLED,
                    )

                    cv2.putText(
                        img,
                        f"Unknown",
                        (left + 6, bottom - 6),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0,
                        (255, 255, 255),
                        2,
                        cv2.LINE_AA,
                    )

                    cv2.imwrite(
                        f"{django_settings.MEDIA_URL}image/unknown_user.jpg", img
                    )
                    return json.dumps(
                        f"{django_settings.MEDIA_URL}image/unknown_user.jpg"
                    )
