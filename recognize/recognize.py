import cv2

from database import db


class RECOGNIZE:
    datab = db.Database()

    def __init__(self):
        super().__init__()

        self.faceDetect = cv2.CascadeClassifier(
            "./assets/classifiers/haarcascade_frontalface_alt2.xml"
        )
        self.cam = cv2.VideoCapture(0)

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

        self.datab.cur.execute("SELECT * FROM Students")

        name_lst = list()

        for row in self.datab.cur:
            name = f"{row[3]}_{row[1]}".lower()
            name_lst.append(name)

        self.verify()

    def verify(self):
        def get_profile():
            profile = None
            for row in self.datab.cur:
                profile = row
            return profile

        for name in name_lst:
            self.recognizer.read(f"./assets/training_data/{name}-training_data.yml")

        Id = 0
        while True:
            ret, image = self.cam.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.faceDetect.detectMultiScale(
                gray,
                scaleFactor=1.5,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE,
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 1)
                Id, conf = self.recognizer.predict(gray[y : y + h, x : x + w])
                profile = get_profile()
                # print()
                if profile != None:
                    if profile[0] == Id:
                        cv2.putText(
                            image,
                            f"Name: {profile[3]}\n{profile[2]}\n{profile[1]}",
                            (x, y + h + 20),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            1,
                            cv2.LINE_AA,
                        )
                    else:
                        cv2.putText(
                            image,
                            f"Individual Unknown",
                            (x, y + h + 20),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            1,
                            (0, 0, 255),
                        )
                else:
                    break
            cv2.imshow("Recognize", image)
            if cv2.waitKey(1) == ord("q"):
                break
        cam.release()
        cv2.destroyAllWindows()
