"""
Face Recognition Script
This script captures video from the default webcam and performs face recognition
using pre-encoded images of authorized persons. It draws bounding boxes around
detected faces and labels them with the recognized names.
"""
import os
import cv2
import numpy as np
import face_recognition

# Directories for authorized and unauthorized persons' images
known_images = "images"

# Get a reference to webcam #0 (the default one)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Create arrays of known face encodings and their names
known_face_encodings = []
known_face_names = []

if os.path.exists(known_images):
    imagesList = os.listdir(known_images)
    for imageName in imagesList:
        image_path = os.path.join(known_images, imageName)
        image = cv2.imread(image_path)
        
        if image is not None:
            # Convert the image to RGB format
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Encode the face in the image
            encodedFace = face_recognition.face_encodings(rgb_image)
            
            if encodedFace:
                known_face_encodings.append(encodedFace[0])
                known_face_names.append(os.path.splitext(imageName)[0])

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
distance_threshold = 0.512

while True:
    try:
        # Grab a single frame of video
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame from webcam.")
            break

        # Only process every other frame of video to save time
        if process_this_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index] and face_distances[best_match_index] < distance_threshold:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face and label it
            box_color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), box_color, 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), box_color, cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print(f"Exception: {e}")
        break

# Release handle to the webcam and close windows
cap.release()
cv2.destroyAllWindows()
