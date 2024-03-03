from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
# import pymysql
import sqlite3
class Register:
  def __init__(self,root):
    self.root=root
    self.root.title("Registration Window")
    self.root.geometry("1350x700+0+0")
    self.root.config(bg="white")
    #=====Bg Image=========
    self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
    bg=Label(self.root,image=self.bg).place()

