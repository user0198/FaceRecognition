import cv2
import dlib
import numpy as np 

# Get a reference to webcam #0 (the default one)
capture = cv2.VideoCapture(0)
#  Import detector
detector = dlib.get_frontal_face_detector()

while True:
    # Grab a single frame of video
    _, frame = capture.read()
    # Convert BGR color-scheme to GRAY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in a list
    faces = detector(gray)
    for face in faces:
        # Get coords
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

    # Display the resulting image
    cv2.imshow("Frame", frame)

    # Hit 'esc' on the keyboard to quit!
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release handle to the webcam
capture.release()
cv2.destroyAllWindows()