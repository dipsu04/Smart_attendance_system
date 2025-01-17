from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbh = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbh.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"images/tree1.jpeg")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Display Image
        lbl_img = Label(self.root, image=self.photoimg_top)
        lbl_img.place(x=0, y=55, width=1530, height=325)

        # Train Button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="blue", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        # Bottom Image
        img_bottom = Image.open(r"images/tree1.jpeg")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        lbl_img = Label(self.root, image=self.photoimg_bottom)
        lbl_img.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.png', '.jpg', '.jpeg'))]

        faces = []
        ids = []
        count = 0

        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')  # Convert to NumPy array
                id = int(os.path.split(image)[1].split('.')[1])  # Extract ID
                faces.append(imageNp)
                ids.append(id)
                count += 1

                cv2.imshow("Training Image", imageNp)
                cv2.waitKey(1)
            except Exception as e:
                print(f"Error processing {image}: {e}")

        ids = np.array(ids)

        # Train and save the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("Result", f"Training completed! Total images processed: {count}")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
