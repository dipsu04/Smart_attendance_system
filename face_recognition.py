from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import mysql.connector
import os


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x1000+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_label = Label(
            self.root,
            text="FACE RECOGNITION",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_label.place(x=0, y=0, width=1530, height=45)

        # First Image
        img_top = Image.open(r"/Users/deepkhanal/Desktop/smart attendance/images/face.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        lbl_img_top = Label(self.root, image=self.photoimg_top)
        lbl_img_top.place(x=0, y=55, width=650, height=700)

        # Second Image
        img_bottom = Image.open(r"/Users/deepkhanal/Desktop/smart attendance/images/facedect.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        lbl_img_bottom = Label(self.root, image=self.photoimg_bottom)
        lbl_img_bottom.place(x=650, y=55, width=950, height=700)

        # Face Recognition Button
        face_recognition_btn = Button(
            lbl_img_bottom,
            text="Face Recognition",
            font=("times new roman", 30, "bold"),
            bg="red",
            fg="white",
            command=self.face_recognition,
            cursor="hand2",
        )
        face_recognition_btn.place(x=400, y=600, width=300, height=60)

    def get_student_details(self, student_id):
        """
        Fetch student details from the database by student ID.
        Returns: Tuple of (name, roll, department) or None if not found.
        """
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="deep@123",
                database="Face_recognition_system",
            )
            cursor = conn.cursor()
            cursor.execute("SELECT Name, Roll, Department FROM student WHERE student_id = %s", (student_id,))
            result = cursor.fetchone()
            return result
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, clf):
        """
        Detect faces and annotate them with information from the database.
        """
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 500)))

            if confidence > 94:
                student_details = self.get_student_details(id)
                if student_details:
                    name, roll, department = student_details
                    cv2.putText(img, f"Name: {name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Roll: {roll}", (x, y - 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Dept: {department}", (x, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            else:
                cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        return img

    def face_recognition(self):
        """
        Perform face recognition using the LBPH algorithm and Haarcascade classifier.
        """
        haarcascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        classifier = cv2.CascadeClassifier(haarcascade_path)

        # Ensure Haarcascade file exists
        if not os.path.exists(haarcascade_path):
            messagebox.showerror("Error", "Haarcascade file not found.")
            return

        # Load pre-trained face recognition model
        model_path = r"/Users/deepkhanal/Desktop/smart attendance/classifier.xml"
        if not os.path.exists(model_path):
            messagebox.showerror("Error", "Trained model file not found.")
            return

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(model_path)

        # Start video capture
        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Unable to access the camera.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = self.draw_boundary(img, classifier, 1.1, 10, clf)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    app = FaceRecognition(root)
    root.mainloop()
