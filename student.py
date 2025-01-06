# ========sample from user=========
from tkinter import messagebox
import mysql.connector
import cv2

#======Validate the fillup boxes=======

def generate_data(self):
    if self.var_Department.get()=="Select Department" or self.var_name.get()=="" or self.va_student_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root) #shows in parent box
    else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sudip@123",database="Face_recognition_system")
                my_cursor=conn.cursor()   #to execute query
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                            self.var_Department.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_semester.get(),
                                                                                                                            self.va_studentd_id.get(),
                                                                                                                            self.var_Name.get(),
                                                                                                                            self.var_Division.get(),
                                                                                                                            self.var_Roll.get(),
                                                                                                                            self.var_Gender.get(),
                                                                                                                            self.var_DOB.get(),
                                                                                                                            self.var_Email.get(),
                                                                                                                            self.var_phone.get(),
                                                                                                                            self.var_Address.get(),
                                                                                                                            self.var_Teacher.get(),
                                                                                                                            self.var_radio1.get()
                                                                                                                        ))
                        
            except Exception as e:
             messagebox.showerror("Error",f"due to:{str(e)}",parent=self.root)

            conn.commit()
            conn.close()
            messagebox.showinfo("success","Student details has been added succesfully",parent=self.root)