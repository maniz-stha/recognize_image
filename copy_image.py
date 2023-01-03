import face_recognition
import glob
from shutil import copy

image = face_recognition.load_image_file("known_images/image.jpg")
known_face_encoding = face_recognition.face_encodings(image)[0]

unknown_images = glob.glob('unknown_images/*')

for image in unknown_images:
    faces = face_recognition.load_image_file(image)

    face_locations = face_recognition.face_locations(faces)
    face_encodings = face_recognition.face_encodings(faces, face_locations)
    for face_encoding in face_encodings:
        result = face_recognition.compare_faces([known_face_encoding], face_encoding, 0.5)
        if True in result:
            file_name = image.split('/')[-1]
            print('matched image' + file_name)
            copy(image, 'matched_images/' + file_name)
