
# Face Recognition with OpenCV and Flask

This project implements real-time face recognition using OpenCV and Flask. The application captures video from a webcam, processes the frames to detect and recognize faces, and displays the video stream with labeled faces in a web interface.





## Features

- Real-time face detection and recognition.
- Uses OpenCV for video capture and face drawing.
- Utilizes face_recognition library for face encoding and comparison.
- Simple Flask web application to display the video stream.


## Requirements

- Python 3.x
- Flask
- opencv
- face_recognition
- Numpy
## Acknowledgements

- The face_recognition library by Adam Geitgey for the robust face recognition functionality.

- OpenCV community for the comprehensive computer vision library.

- Flask community for the lightweight web framework.


## Installation

1)To run tests, run the following command

```bash
  git clone https://github.com/SadabAli/Face-recognition-by-using-opencv.git
```
```bash
  cd face-recognition-flask
```
 2)Install the required packages:
```bash
  pip install -r requirements.txt

```
3)Add your face image for recognition. Save the image in the project directory with the name <photoname>.jpg.

## Usage
1)Run the Flask application
```bash
  python app.py

```
2)Open your web browser and go to http://127.0.0.1:5000/ to view the live video stream with face recognition.



## Reference

- https://pypi.org/project/face-recognition/


## License

[MIT](https://choosealicense.com/licenses/mit/)

