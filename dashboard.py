from tkinter import*
from PIL import Image, ImageTk #from PIL.Image import core as _imaging #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass


class RMS:
  def __init__(self,root):
    self.root=root
    self.root.title("STUDENT RESULT MANAGEMENT SYSTEM")
    self.root.geometry("1370x700+0+0")
    self.root.config(bg="white")

    #===icons=====
    self.logo_dash=ImageTk.PhotoImage(file="./images/logo_p.png")
    
    #===title=====
    title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height="50")
    
    #===Menu======
    M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
    M_Frame.place(x=10,y=70,width=1340,height=80)

    btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
    btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
    btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
    btn_view=Button(M_Frame,text="View Student Results",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
    btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)
    btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1120,y=5,width=200,height=40)

    #===Content_Window====
    self.bg_img=Image.open("./images/bg.png")
    self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
    self.bg_img=ImageTk.PhotoImage(self.bg_img)
    
    self.lb1_bg=Label(self.root,image=self.bg_img).place(x=400,y=100,width=920,height=350)

    #===update_details=====
    self.lb1_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief="RIDGE",bg="#e43b06",fg="white")
    self.lb1_course.place(x=400,y=530,width=300,height=100)

    self.lb1_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief="RIDGE",bg="#0676ad",fg="white")
    self.lb1_student.place(x=710,y=530,width=300,height=100)

    self.lb1_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",20),bd=10,relief="RIDGE",bg="#038074",fg="white")
    self.lb1_result.place(x=1020,y=530,width=300,height=100)


    #===footer=====
    footer=Label(self.root,text="SRMS-Student Result Management System\n Contact Us for any Technical Issue: 816xxxxx34 ",font=("goudy old style",12),bg="#262626",fg="white").pack(side="BOTTOM",fill=X)

  def add_course(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=CourseClass(self.new_win)

  def add_student(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=studentClass(self.new_win)

  def add_result(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=resultClass(self.new_win)

  def add_report(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=reportClass(self.new_win)


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()





#====== this works ========

# from tkinter import*
# class RMS:
#   def __init__(self,root):
#     self.root=root
#     self.root.title("STUDENT RESULT MANAGEMENT SYSTEM")
#     self.root.geometry("1370x700+0+0")
#     self.root.config(bg="white")

# if __name__=="__main__":
#   root=Tk()
#   obj=RMS(root)
#   root.mainloop()

