import cv2
import face_recognition

# Load known face encodings and names
known_face_encodings = []
known_face_names = []

# Load known faces and their names here
known_person1_image = face_recognition.load_image_file("C:/Users/Kwabena/Desktop/Face recognition/images/T1.jpeg")
known_person2_image = face_recognition.load_image_file("C:/Users/Kwabena/Desktop/Face recognition/images/K1.jpeg")

known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)

known_face_names.append("Jackie")
known_face_names.append("Kwabena")

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Default hyperparameters
tolerance = 0.6

# Create a window for the trackbars
cv2.namedWindow("Hyperparameters")

# Define a callback function for the trackbars
def nothing(x):
    pass

# Create trackbars for hyperparameters
cv2.createTrackbar("Tolerance", "Hyperparameters", int(tolerance * 100), 100, nothing)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Get current positions of the trackbars
    tolerance = cv2.getTrackbarPos("Tolerance", "Hyperparameters") / 100

    # Find all face locations and face encodings in the current frame using the CNN model
    face_locations = face_recognition.face_locations(frame, model="cnn")
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=tolerance)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face and label with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Break the loop when the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close OpenCV window
video_capture.release()
cv2.destroyAllWindows()
