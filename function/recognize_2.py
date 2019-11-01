import face_recognition
import cv2
import numpy as np
import 
from database.db import Database


class RECOGNIZE_2:
    datab = Database()

    def __init__(self, image_other):
        super().__init__()

        self.profile = None

        self.verified = False

        self.image = image_other

        self.verify()

    def verify(self):
        self.datab.cur.execute("SELECT * FROM Students")
        self.student_list_all = self.datab.cur.fetchall()
        
        known_face_encodings = []
        known_face_ids = []
        
        # Load a sample picture and learn how to recognize it.
        for image in os.listdir('./assets/student'):
            stored_image = face_recognition.load_image_file(
                f"{image}/{image}.jpg"
            )
            stored_face_encoding = face_recognition.face_encodings(stored_image)[0]

            # Create arrays of known face encodings and their names
            known_face_encodings.append(stored_face_encoding)
            
            for profile in self.student_list_all:
                known_face_ids.append(profile[0])

        # Initialize some variables
        face_locations = []
        face_encodings = []

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
        for (top, right, bottom, left) in face_locations:
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(self.image, (left, top), (right, bottom), (255, 255, 255), 1)

            # face_names = []
            for face_encoding in face_encodings:
                for row in self.student_list_all:
                    self.profile = row
                    profile = self.profile

                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(
                        known_face_encodings, face_encoding
                    )
                    _id = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_ids[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(
                        known_face_encodings, face_encoding
                    ) 
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        _id = known_face_ids[best_match_index]

                        if profile[0] == _id:
                            self.verified = True

                            # Draw a label with a name below the face
                            cv2.rectangle(
                                self.image,
                                (left, bottom - 35),
                                (right, bottom),
                                (0, 255, 0),
                                cv2.FILLED,
                            )
                            font = cv2.FONT_HERSHEY_DUPLEX
                            cv2.putText(
                                self.image,
                                profile[3],
                                (left + 6, bottom - 6),
                                font,
                                1.0,
                                (255, 255, 255),
                                1,
                            )
                        else:
                            cv2.rectangle(
                                self.image,
                                (left, bottom - 35),
                                (right, bottom),
                                (0, 0, 255),
                                cv2.FILLED,
                            )
                            cv2.putText(
                                self.image,
                                f"Individual Unknown",
                                (left + 6, bottom - 6),
                                font,
                                1.0,
                                (255, 255, 255),
                            )
