import mediapipe as mp
import numpy as np
import cv2
import pickle
import webbrowser

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def choose_url():
    print("Choose an option to open after successful authentication:")
    print("1. GitHub")
    print("2. LinkedIn")
    
    while True:
        choice = input("Enter your choice (1/2): ")
        if choice == "1":
            return "https://github.com/NikhilGupta20"
        elif choice == "2":
            return "https://www.linkedin.com/in/nikhillguptaa/"
        else:
            print("Invalid choice. Please enter 1 or 2.")

def register_face():
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Could not open camera.")
        return None

    print("Please position your face in front of the camera for registration and press 'r' to register...")

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Failed to capture video. Exiting...")
                break

            results = face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(frame, detection)

            cv2.imshow("Video", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('r') and results.detections:
                for detection in results.detections:
                    keypoints = np.array([
                        (kp.x, kp.y)
                        for kp in detection.location_data.relative_keypoints
                    ])

                    try:
                        with open("registered_face.pkl", "wb") as f:
                            pickle.dump(keypoints, f)
                        print("Face registered successfully!")
                    except Exception as e:
                        print(f"Error saving registered face: {e}")
                    
                    video_capture.release()
                    cv2.destroyAllWindows()
                    return keypoints

            if key == ord('q'):
                break

    video_capture.release()
    cv2.destroyAllWindows()
    print("No face detected, registration failed.")
    return None

def compare_faces(registered_keypoints, new_keypoints, threshold=0.1):
    distances = np.linalg.norm(registered_keypoints - new_keypoints, axis=1)
    avg_distance = np.mean(distances)
    return avg_distance < threshold

def authenticate_user():
    try:
        with open("registered_face.pkl", "rb") as f:
            registered_keypoints = pickle.load(f)
    except FileNotFoundError:
        print("No registered face found. Please register first.")
        return

    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Could not open camera.")
        return

    authenticated = False

    print("Please position your face in front of the camera for authentication...")

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Failed to capture video. Exiting...")
                break

            results = face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            if results.detections:
                for detection in results.detections:
                    new_keypoints = np.array([
                        (kp.x, kp.y)
                        for kp in detection.location_data.relative_keypoints
                    ])

                    if compare_faces(registered_keypoints, new_keypoints):
                        print("Authentication Successful")
                        selected_url = choose_url()
                        webbrowser.open(selected_url)
                        authenticated = True
                        break

                    mp_drawing.draw_detection(frame, detection)

            cv2.imshow("Video", frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or authenticated:
                break

    video_capture.release()
    cv2.destroyAllWindows()

    if not authenticated:
        print("Authentication Failed")

def main():
    print("1. Register Face\n2. Authenticate Face")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        register_face()
    elif choice == "2":
        authenticate_user()
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()
