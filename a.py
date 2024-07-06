from flask import Flask , Responce , render_template
import cv2
import face_recognition
import numpy as np

app=Flask(__name__)
camera = cv2.VideoCapture(0)
sadab_img = face_recognition.load_image_file("WIN_20240706_11_13_21_Pro.jpg")
sadab_face_encoding = face_recognition.face_encodings(sadab_img)[0]

known_face_encoding=[
    sadab_face_encoding
]
known_face_name =[
    "sadab ali"
]
face_location = []
face_encoding=[]
face_name =[]
process_this_frame=True
def Generate_frame():
    pass
if __name__ == "__main__":
    app.run(debug=True)
