import os
import cv2
import numpy as np
from PIL import Image


class TRAINER:
    def __init__(self, Id, name):
        super().__init__()

        self.train(Id, name)

    def train(self, Id, name):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

        self._dir = (
            f"./face_recognition/face_recognition/assets/student/{name}/{name}.jpg"
        )

        if not os.path.exists(
            "./face_recognition/face_recognition/assets/training_data"
        ):
            os.makedirs("./face_recognition/face_recognition/assets/training_data")
        else:
            pass

        def get_images_with_id(_dir):
            faces = []
            _ids = []
            face_img = Image.open(_dir).convert("L")
            face_array = np.array(face_img, "uint8")
            _id = Id
            faces.append(face_array)
            _ids.append(_id)
            return np.array(_ids), faces

        Ids, faces = get_images_with_id(self._dir)
        self.recognizer.train(faces, Ids)
        self.recognizer.save(
            f"./face_recognition/face_recognition/assets/training_data/{name}-training_data.yml"
        )
