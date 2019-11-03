import cv2
import os
from database.db import Database


class RECOGNIZE:
    datab = Database()

    def __init__(self, image_other):
        super().__init__()
        self.profile = None
        # self.staff_profile = None

        self.verified = False

        self.image = image_other

        self.faceDetect = cv2.CascadeClassifier(
            "./assets/classifiers/haarcascade_frontalface_alt2.xml"
        )
        # self.cam = cv2.VideoCapture(0)

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

        self.verify_student()

    def verify_student(self):
        self.datab.cur.execute("SELECT * FROM Students")
        self.student_list_all = self.datab.cur.fetchall()

        self._dir = "./assets/training_data/"
        self.train_path = [os.path.join(self._dir, f) for f in os.listdir(self._dir)]

        Id = 0
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        faces = self.faceDetect.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 255, 255), 1)
            for train_data in self.train_path:
                self.recognizer.read(train_data)
                for row in self.student_list_all:
                    self.profile = row
                    Id, conf = self.recognizer.predict(gray[y : y + h, x : x + w])
                    profile = self.profile
                    if profile != None:
                        if profile[0] == Id and conf <= 60:
                            self.verified = True
                            # cv2.putText(
                            #     self.image,
                            #     f"Name: {profile[3]}\n{profile[2]}\n{profile[1]}",
                            #     (x, y + h + 20),
                            #     cv2.FONT_HERSHEY_SIMPLEX,
                            #     1,
                            #     (0, 255, 0),
                            #     1,
                            #     cv2.LINE_AA,
                            # )
                        else:
                            cv2.putText(
                                self.image,
                                f"Individual Unknown",
                                (x, y + h + 20),
                                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                1,
                                (0, 0, 255),
                            )
                    else:
                        pass

    # def verify_staff(self):
    #     self.datab.cur.execute("SELECT * FROM Staff")
    #     self.staff_list_all = self.datab.cur.fetchall()

    #     self._dir = "./assets/training_data/"
    #     self.train_path = [os.path.join(self._dir, f) for f in os.listdir(self._dir)]

    #     Id = 0
    #     gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    #     faces = self.faceDetect.detectMultiScale(
    #         gray,
    #         scaleFactor=1.3,
    #         minNeighbors=5,
    #         minSize=(30, 30),
    #         flags=cv2.CASCADE_SCALE_IMAGE,
    #     )

    #     for (x, y, w, h) in faces:
    #         cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 255, 255), 1)
    #         for train_data in self.train_path:
    #             self.recognizer.read(train_data)
    #             for row in self.staff_list_all:
    #                 self.staff_profile = row
    #                 Id, conf = self.recognizer.predict(gray[y : y + h, x : x + w])
    #                 profile = self.staff_profile
    #                 if profile != None:
    #                     if profile[0] == Id and conf <= 60:
    #                         self.verified = True
    #                         # cv2.putText(
    #                         #     self.image,
    #                         #     f"Name: {profile[3]}\n{profile[2]}\n{profile[1]}",
    #                         #     (x, y + h + 20),
    #                         #     cv2.FONT_HERSHEY_SIMPLEX,
    #                         #     1,
    #                         #     (0, 255, 0),
    #                         #     1,
    #                         #     cv2.LINE_AA,
    #                         # )
    #                     else:
    #                         cv2.putText(
    #                             self.image,
    #                             f"Individual Unknown",
    #                             (x, y + h + 20),
    #                             cv2.FONT_HERSHEY_COMPLEX_SMALL,
    #                             1,
    #                             (0, 0, 255),
    #                         )
    #                 else:
    #                     pass
