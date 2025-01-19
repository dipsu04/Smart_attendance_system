from tkinter import *
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x1000+0+0")
        self.root.title("Face Recognition System") 

        # Button to start face recognition
        b1 = Button(self.root, text="Face Recognition", cursor="hand2", command=self.face_recognition, bg="darkgreen", fg="white", font=("times new roman", 20, "bold"))
        b1.place(x=300, y=350, width=300, height=100)

    def face_recognition(self):
        # Function to draw boundary and recognize faces
        def draw_boundary(img, classifier, scalefactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
            features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbors)  # Detect faces
            coordinates = []  # Store face coordinates

            for (x, y, w, h) in features:
                # Draw rectangle around face
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                
                # Predict the face
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 490))
                                          # Calculate confidence
                print(f"ID: {id}, Predict Score: {predict}, Confidence: {confidence}")


                # Database connection
                conn = None
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="sudip@123",
                        database="Face_recognition_system"
                    )
                    my_cursor = conn.cursor()

                    # Check confidence threshold
                    if confidence > 93:
                        # Fetch student name from the database
                        my_cursor.execute("SELECT Name FROM student WHERE student_id = %s", (id,))
                        result = my_cursor.fetchone()

                        if result:
                            student_name = "+".join(result)  # Convert tuple to string
                            cv2.putText(img, f"Student Name: {student_name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                        else:
                            cv2.putText(img, "Unknown Face (No Data)", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    else:
                        # Mark face as unknown
                        cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                except mysql.connector.Error as e:
                    print(f"Database Error: {e}")
                    cv2.putText(img, "Database Error", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                finally:
                    if conn:
                        conn.close()

                coordinates = [x, y, w, h]  # Store coordinates

            return coordinates

        # Function to recognize faces
        def recognize(img, clf, faceCascade):
            coordinates = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        # Load Haar Cascade and LBPH classifier
        haarcascade_path = r"/Users/sudippokharel/Desktop/Backend/myenv/lib/python3.12/site-packages/cv2/data/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(haarcascade_path)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"/Users/sudippokharel/Desktop/Backend/classifier.xml")

        # Open webcam
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture image. Exiting...")
                break

            # Recognize faces in the video frame
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition System", img)

            # Exit on pressing 'Enter'
            if cv2.waitKey(1) == 13:
                break

        # Release resources
        video_cap.release()
        cv2.destroyAllWindows()
       


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
