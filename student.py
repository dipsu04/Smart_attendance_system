# ========sample from user=========
from tkinter import messagebox
import cv2

#======Validate the fillup boxes=======

def generate_data(self):
    if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            pass