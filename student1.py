from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x2000+0+0")

        self.root.title("Face Recognition System")
        
        
        # First Image
        img = Image.open(r"C:\Users\Janak_Joshi\OneDrive\Desktop\UI SAS\images\sas1.jpg")
        img = img.resize((500, 130), Image.LANCZOS)  # Adjusted size
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open(r"C:\Users\Janak_Joshi\OneDrive\Desktop\UI SAS\images\sas1.jpg")
        img1 = img1.resize((400, 130), Image.LANCZOS)  # Adjusted size
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=400, height=130)

        # Third Image
        img2 = Image.open(r"C:\Users\Janak_Joshi\OneDrive\Desktop\UI SAS\images\sas1.jpg")
        img2 = img2.resize((530, 130), Image.LANCZOS)  # Adjusted size
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=900, y=0, width=530, height=130)


        
         # bg Image
        img3 = Image.open(r"C:\Users\Janak_Joshi\OneDrive\Desktop\UI SAS\images\bgimage.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)  # Adjusted size
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)


        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1275,height=45)
        
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1500,height=650)
        
        
        # left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=690,height=750)
        
        
        
        img_left = Image.open(r"C:\Users\Janak_Joshi\OneDrive\Desktop\UI SAS\images\sas1.jpg")
        img_left = img_left.resize((680, 130), Image.LANCZOS)  # Adjusted size
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        
        f_lbl2 = Label(Left_frame, image=self.photoimg_left)
        f_lbl2.place(x=5, y=0, width=680, height=130)


         # current course
        
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=680,height=120)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width="20",state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),width="20",state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),width="17",state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=1,pady=15,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),width="17",state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Studeent Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=260,width=680,height=242)

        #student id
        studentId_label=Label(class_Student_frame,text="StudentId:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #student division
        class_div_label=Label(class_Student_frame,text="Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #dob
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #teacher name
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        radionbtn1=ttk.Radiobutton(class_Student_frame,text="Take photo sample",value="yes")
        radionbtn1.grid(row=6,column=0)
        
        radionbtn2=ttk.Radiobutton(class_Student_frame,text="No photo sample",value="no")
        radionbtn2.grid(row=6,column=1)

        #bbuttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=50,y=195,width=700,height=100)

        #save
        save_btn=Button(btn_frame,text="Save",font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #update
        update_btn=Button(btn_frame,text="Update",font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #delete
        delete_btn=Button(btn_frame,text="Delete",font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

         #reset
        delete_btn=Button(btn_frame,text="Reset",font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=3)

        #take photo
        take_photo_btn=Button(btn_frame,text="Take Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4)

         #Update photo
        update_photo_btn=Button(btn_frame,text="Update Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=5)


        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=705,y=10,width=560,height=580)

        img_right = Image.open(r"C:\Users\Janak_Joshi\OneDrive\Desktop\UI SAS\images\sas1.jpg")
        img_right = img_left.resize((680, 130), Image.LANCZOS)  # Adjusted size
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        
        f_lbl2 = Label(Right_frame, image=self.photoimg_right)
        f_lbl2.place(x=5, y=0, width=680, height=130)

        #---------search system---------
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=550,height=80)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),width="15",state="readonly")
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=10,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(search_frame,text="Search",width="8",font=("times new roman",8,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width="8",font=("times new roman",8,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #---------------table frame-------------
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=230,width=550,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)

        self.student_table.pack(fill=BOTH,expand=1)     

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
