from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import subprocess
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x1000+0+0")

        self.root.title("Face Recognition System")


        # title_lbl=Label(self.root,text="Train data set",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        # title_lbl.place(x=0,y=0,width=1275,height=45)
        # img_top = Image.open(r"/Users/sudippokharel/Downloads/sas1.jpg")
        # img_top = img_top.resize((680, 130), Image.LANCZOS)  # Adjusted size
        # self.photoimg_top = ImageTk.PhotoImage(img_top)
       
       
       
       
       
       
        #just button

        b1_1=Button(self.root,text="Train Data Here",cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=300,y=380,width=200,height=60)
    def train_classifier(self):
        data_dir=("/Users/sudippokharel/Desktop/Backend/data")#variable ma image stored bhayp
        path=[ os.path.join(data_dir,file)for file in os.listdir(data_dir)]# data folder ko sabai image lai full path deko

        faces=[]
        id=[]

        for image in path: #all images in directory is in image variable
            img=Image.open(image).convert('L')# gray scale image
            imageNp=np.array(img,'uint8')#array ko data type uint8,,,image lai numpy array ma convert gareko
            id=int(os.path.split(image)[1].split('.'[1]))

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training the dataset",imageNp)
            cv2.waitkey(1)==13

        ids=np.array(ids)




        
        
        # f_lbl2 = Label(self.root, image=self.photoimg_top)
        # f_lbl2.place(x=5, y=0, width=680, height=130)
















if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()