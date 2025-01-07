# ========sample from user=========
from tkinter import messagebox
import mysql.connector
import cv2


self.student_table.bind("<ButtonRelease>",self.get_cursor)
self.fetch_data()
#======Validate the fillup boxes=======
       
def add_data(self):
    if self.var_Department.get()=="Select Department" or self.var_name.get()=="" or self.va_student_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root) #shows in parent box and my sql connection
    else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sudip@123",database="Face_recognition_system")
                print("Connection successful")
                my_cursor=conn.cursor()   #to execute query
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                            self.var_Department.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_semester.get(),
                                                                                                                            self.va_student_id.get(),
                                                                                                                            self.var_name.get(),
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
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","Student details has been added succesfully",parent=self.root)

            #data lai fetch gareko

            def fetch_data(self):
                 conn=mysql.connector.connect(host="localhost",username="root",password="sudip@123",database="Face_recognition_system")
                 my_cursor=conn.cursor()
                 my_cursor.execute("select * from student")
                 data=my_cursor.fetchall()

                 if len()!=0:
                     self.student_table.delete(*self.student_table.get_children())
                     for i in data:
                         self.student_table.insert("",END,values=i)
                         conn.commit()
                 conn.close()
                 
            #get cursor
            def get_cursor(self,event=""):
                cursor_focus=self.student_table.focus()
                content=self.student_table.item(cursor_focus)
                data=content["values"]

                self.var_Department.set(data[0]),
                self.var_course.set(data[1]),
                self.var_year.set(data[2]),
                self.var_semester.set(data[3]),
                self.va_student_id.set(data[4]),
                self.var_name.set(data[5]),
                self.var_Division.set(data[6]),
                self.var_Roll.set(data[7]),
                self.var_Gender.set(data[8]),
                self.var_DOB.set(data[9]),
                self.var_Email.set(data[10]),
                self.var_phone.set(data[11]),
                self.var_Address.set(data[12]),
                self.var_Teacher.set(data[13]),
                self.var_radio1.set(data[14])