from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img = Image.open(r"/Users/manishyogi/Desktop/fronted/image/attendance.jpg")
        img = img.resize((500, 130), Image.LANCZOS)  # Adjusted size
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open(r"/Users/manishyogi/Desktop/fronted/image/developers.jpg")
        img1 = img1.resize((400, 130), Image.LANCZOS)  # Adjusted size
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=400, height=130)

        # Third Image
        img2 = Image.open(r"/Users/manishyogi/Desktop/fronted/image/developers.jpg")
        img2 = img2.resize((530, 130), Image.LANCZOS)  # Adjusted size
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=900, y=0, width=530, height=130)


        # bg Image
        img3 = Image.open(r"/Users/manishyogi/Desktop/fronted/image/sas1.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)  # Adjusted size
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1275,height=45)


        #student button
        img4 = Image.open(r"/Users/manishyogi/Desktop/fronted/image/sas1.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)  # Adjusted size
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=100,y=100,width=200,height=175)


        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=255,width=200,height=35)


         #detect face button
        img5 = Image.open(r"/Users/manishyogi/Desktop/fronted/image/attendance.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)  # Adjusted size
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=400,y=100,width=200,height=175)


        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=260,width=200,height=35)


         #attendance face button
        img6 = Image.open(r"/Users/manishyogi/Desktop/fronted/image/attendance.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)  # Adjusted size
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=700,y=100,width=200,height=175)


        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=260,width=200,height=35)


        #help button
        img7 = Image.open(r"/Users/manishyogi/Desktop/fronted/image/attendance.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)  # Adjusted size
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1000,y=100,width=200,height=175)


        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=260,width=200,height=35)


         #train button
        img8 = Image.open(r"C:\Users\Janak_Joshi\OneDrive\Desktop\UI SAS\images\train.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)  # Adjusted size
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=100,y=350,width=200,height=175)


        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=510,width=202,height=35)


          #photos button
        img9 = Image.open(r"C:\Users\Janak_Joshi\OneDrive\Desktop\UI SAS\images\photo.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)  # Adjusted size
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=400,y=350,width=200,height=175)


        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=510,width=200,height=35)


          #developer button
        img10 = Image.open(r"C:\Users\Janak_Joshi\OneDrive\Desktop\UI SAS\images\developers.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)  # Adjusted size
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=700,y=350,width=200,height=175)


        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=510,width=200,height=35)


        #Exit button
        img11 = Image.open(r"C:\Users\Janak_Joshi\OneDrive\Desktop\UI SAS\images\exit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)  # Adjusted size
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1000,y=350,width=200,height=175)


        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=510,width=200,height=35)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()