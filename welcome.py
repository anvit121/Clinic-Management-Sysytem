from tkinter import *
import sqlite3
import tkinter.messagebox
from tkinter import messagebox
 
 
root = Tk()
root.geometry('1920x1080')
root.title("MAV Clinic")
root.configure(bg = 'lightblue')

def register_user():
    root.destroy()
    import register
    
def login_user():
    root.destroy()
    import login
    
    
label_0 = Label(root, text="WELCOME TO MAV CLINIC!!!", width=40, font=("bold", 25), bg = 'lightblue')
label_0.place(x=420,y=53)

Button(root, text="Register", width=35, height=4, bg="lightblue", command = register_user).place(x=520,y=203)

Button(root, text="Login", width=35, height=4, bg="lightblue", command = login_user).place(x=820,y=203)


root.mainloop()