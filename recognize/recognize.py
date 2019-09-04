import cv2
import numpy as np
import mysql.connector
from mysql.connector import errorcode
try:
    conn = mysql.connector.connect(
        host="localhost", user="root", password="C!$c@123", database="FaceBase"
    )
    if conn.is_connected():
        print("Database Connected")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cur = conn.cursor()


faceDetect = cv2.CascadeClassifier("./classifiers/haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)


rec = cv2.face.LBPHFaceRecognizer_create()

cur.execute("SELECT * FROM Users")
count = 0
id_lst = list()
for row in cur:
    id_num = count + 1
    id_lst.append(id_num)


def getProfile():
    profile = None

    cur.execute("SELECT * FROM Users")
    for row in cur:
        profile = row
    return profile


for _id in id_lst:
    rec.read(f"./data/trainingData-User_{_id}.yaml")

Id = 0
while True:
    ret, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 1)
        Id, conf = rec.predict(gray[y : y + h, x : x + w])
        profile = getProfile()
        # print()
        if profile != None:
            if profile[0] == Id:
                cv2.putText(
                    image,
                    f"Name: {profile[3]} {profile[2]} {profile[1]}",
                    (x, y + h + 20),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    1,
                    (255, 255, 255),
                )
    cv2.imshow("Face", image)
    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
