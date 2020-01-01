import os
import face_recognition
import cv2
import numpy as np
from database.db import Database


class RECOGNIZE:
    datab = Database()

    def __init__(self, image_other):
        super().__init__()

        self.profile = None

        self.verified = False

        self.image = image_other

        self.datab.cur.execute("SELECT * FROM recognize_staff")
        self.stud_list_all = self.datab.cur.fetchall()

        self.known_face_encodings = []
        self.known_face_id = []

        for row in self.stud_list_all:
            self._id = row[0]
            self.name = f"{row[3]}_{row[1]}".lower()

            self._load_faces()

    def _load_faces(self):
        # Load a sample picture and learn how to recognize it.
        for image in os.listdir(f"./face_recog_android/media/image/staff/{self.name}"):
            _image = face_recognition.load_image_file(
                f"./face_recog_android/media/image/staff/{self.name}/{image}"
            )
            _image_face_encoding = face_recognition.face_encodings(_image)[0]

            # Create arrays of known face encodings and their ids
            self.known_face_encodings.append(_image_face_encoding)
            self.known_face_id.append(self._id)

        self.verify()

    def verify(self):

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_id = []

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(self.image, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations
        )

        # Display the results
        for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings
        ):

            matches = face_recognition.compare_faces(
                self.known_face_encodings, face_encoding
            )
            _id = None

            face_distances = face_recognition.face_distance(
                self.known_face_encodings, face_encoding
            )

            best_match_index = np.argmin(face_distances)

            for row in self.stud_list_all:
                self.profile = row
                if matches[best_match_index]:
                    _id = self.known_face_id[best_match_index]

                    if self.profile[0] == _id:
                        self.verified = True
                else:
                    # Scale back up face locations since the self.image we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # Draw a box around the face
                    cv2.rectangle(
                        self.image, (left, top), (right, bottom), (0, 0, 255), 1
                    )

                    # Draw a label with a name below the face
                    cv2.rectangle(
                        self.image,
                        (left, bottom - 35),
                        (right, bottom),
                        (0, 0, 255),
                        cv2.FILLED,
                    )

                    cv2.putText(
                        self.image,
                        f"Unknown",
                        (left + 6, bottom - 6),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0,
                        (255, 255, 255),
                        2,
                        cv2.LINE_AA,
                    )
