import face_recognition

#  Find faces in pictures
image = face_recognition.load_image_file("./resources/known/Barack Obama.jpg")
face_locations = face_recognition.face_locations(image)

#  Find and manipulate facial features in pictures
image = face_recognition.load_image_file("./resources/known/Barack Obama.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)

#  Identify faces in pictures
known_image = face_recognition.load_image_file("./resources/known/Barack Obama.jpg")
unknown_image = face_recognition.load_image_file("./resources/unknown/don_trump.jpg")
# unknown_image = face_recognition.load_image_file("./resources/unknown/barack_obama.jpg")

barack_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([barack_encoding], unknown_encoding)
