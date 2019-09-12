import os
import cv2
import numpy as np
from PIL import Image


def train(Id, name):
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    path = f"./assets/face_data/student/{name}"

    if not os.path.exists("./assets/training_data"):
        os.makedirs("./assets/training_data")
    else:
        pass

    def get_images_with_id(path):
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        _ids = []
        for image_path in image_paths:
            face_img = Image.open(image_path).convert("L")
            face_array = np.array(face_img, "uint8")
            _id = Id
            faces.append(face_array)
            _ids.append(_id)
        return np.array(_ids), faces

    Ids, faces = get_images_with_id(path)
    recognizer.train(Ids, faces)
    recognizer.save(f"./assets/training_data/{name}-training_data.yml")
