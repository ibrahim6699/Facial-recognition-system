import face_recognition as fr
import numpy as np
import cv2
import os



def get_encoded_faces():
    encoded={}
    for _, _,file_names in os.walk("./faces"):
        for file in file_names:
            if file.endswith('.jpg') or file.endswith('.png'):
                face=fr.load_image_file(f'faces/{file}')
                encoding=[fr.face_encodings(face)[0]]
                encoded[file.split('.')[0]]=encoding
    return encoded




print(get_encoded_faces())

