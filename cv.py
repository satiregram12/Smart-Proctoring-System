import cv2
import sys

def start_camera():
    """Initializes the webcam."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        sys.exit()
    return cap

def detect_faces(frame, face_cascade):
    """Detects faces in the current frame."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def main():
    # Load the pre-trained Haar Cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    cap = start_camera()
    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = detect_faces(frame, face_cascade)

        # Draw rectangles and status
        if len(faces) > 0:
            status = "Student Present"
            color = (0, 255, 0) # Green
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        else:
            status = "Alert: Student Missing"
            color = (0, 0, 255) # Red

        cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow('Smart Proctoring', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()