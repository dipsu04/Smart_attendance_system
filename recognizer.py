from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import subprocess
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x1000+0+0")

        self.root.title("Face Recognition System") 

        b1=Button(self.root,text="face recognition",cursor="hand2",command=self.face_recognition,bg="darkgreen")
        b1.place(x=300,y=350,width=200,height=175)

        #========face Recognition=============+#


    def face_recognition(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#coverted
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbors)

            coordinates=[]#coordinates for rectangle

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])#predicting the gray scale image
                confidence=int((100*(1-predict/300)))#formuale througb LBPH

                #retreive data from database

                conn=mysql.connector.connect(host="localhost",username="root",password="sudip@123",database="Face_recognition_system")
                print("Connection successful")
                my_cursor=conn.cursor()   #to execute query



                my_cursor.execute("select Name from student where student_id = %s", (id,))

                i=my_cursor.fetchone()
                i="+".join(i)#concatination





                if confidence>80:
                    cv2.putText(img,f"Student Name:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),10)


                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.1,(255,0,0),3)

                coordinates=[x,y,w,h]#passed the coodrinates
            return coordinates
        def recognize(img,clf,faceCascade):
            coordinate=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        haarcascade_path = r"/Users/sudippokharel/Desktop/Backend/myenv/lib/python3.12/site-packages/cv2/data/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(haarcascade_path)
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"/Users/sudippokharel/Desktop/Backend/classifier.xml")


        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            if not ret:
                print("Failed to capture image. Exiting...")
                break
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face recognition system",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


            

if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()