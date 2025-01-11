from tkinter import *
from tkinter import messagebox
import mysql.connector
import cv2
from PIL import Image, ImageTk


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x1000+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbh = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbh.place(x=0, y=0, width=1530, height=45)

        # First Image
        img_top = Image.open(r"/Users/deepkhanal/Desktop/smart attendance/images/face.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Display Image
        lbl_img = Label(self.root, image=self.photoimg_top)
        lbl_img.place(x=0, y=55, width=650, height=700)

        # Second Image
        img_bottom = Image.open(r"/Users/deepkhanal/Desktop/smart attendance/images/facedect.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # Display Image
        lbl_img = Label(self.root, image=self.photoimg_bottom)
        lbl_img.place(x=650, y=55, width=950, height=700)

        # Button for Face Recognition
        b1_1 = Button(lbl_img, text="Face Recognition", cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white", command=self.face_recog)
        b1_1.place(x=400, y=600, width=300, height=60)

    # =========== Face Recognition ==========#
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="deep@123", database="Face_recognition_system")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE student_id = %s", (str(id),))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE student_id = %s", (str(id),))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("SELECT Department FROM student WHERE student_id = %s", (str(id),))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                if confidence >10:
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dept: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        # Load the pre-trained Haar Cascade for face detection
        haarcascade_path =r"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/cv2/data/haarcascade_frontalface_default.xml"
        faceCascade =cv2.CascadeClassifier(haarcascade_path)
        
        # Initialize the face recognizer and load the trained classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"/Users/deepkhanal/Desktop/smart attendance/classifier.xml")

        # Start video capture
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

