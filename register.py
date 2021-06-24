from tkinter import *
import sqlite3
import tkinter.messagebox
import mysql.connector

root = Tk()
root.geometry('1920x1080')
root.title("Registration Form")
root.configure(bg = 'lightblue')
 
Fullname=StringVar()
Email=StringVar()
var = StringVar()
Phone=StringVar()
Password= StringVar()

 
 
def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   phone=Phone.get()
   password=Password.get()
   
   
   conn = sqlite3.connect('database1.db')
   with conn:
      cursor=conn.cursor()
      if  name1 == '' or  email == '' or gender == '' or phone == '' or password == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
 
      else:
        try:
            # cursor.execute('CREATE TABLE IF NOT EXISTS Registration (Fullname TEXT,Email TEXT,Gender TEXT,Phone TEXT, Password TEXT)')
            cursor.execute('INSERT INTO register (FullName,Email,Gender,Phone,Password) VALUES(?,?,?,?,?)',(name1,email,gender,phone,password))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Registration for " +str(name1) + " has been done")
            root.destroy()
            import login 
        
        except sqlite3.IntegrityError as err:
                print(err)
                #c.execute('SELECT scheduled_time FROM appointments WHERE scheduled_time=?', (scheduled_time))
                tkinter.messagebox.showwarning("Already Registered", "User already exists")   
    
def Registration():
    conn = sqlite3.connect('database1.db')
     
    label_0 = Label(root, text="Registration form",width=20,font=("bold", 23), bg = 'lightblue')
    label_0.place(x=620,y=53)
 
 
    label_1 = Label(root, text="Full Name",width=20,font=("bold", 15), bg = 'lightblue')
    label_1.place(x=520,y=130)
    
    entry_1 = Entry(root,textvar=Fullname, width=40)
    entry_1.place(x=720,y=135)
    
    label_2 = Label(root, text="Email",width=20,font=("bold", 15), bg = 'lightblue')
    label_2.place(x=520,y=180)
    
    entry_2 = Entry(root,textvar=Email, width=40)
    entry_2.place(x=720,y=180)
    
    label_3 = Label(root, text="Gender",width=20,font=("bold", 15), bg = 'lightblue')
    label_3.place(x=520,y=230)
    var.set('Female')

    Radiobutton(root, text="Male",padx = 5, variable=var, value="Male", bg = 'lightblue').place(x=735,y=230)
    Radiobutton(root, text="Female",padx = 20, variable=var, value="Female", bg = 'lightblue').place(x=790,y=230)
    Radiobutton(root, text="Other",padx = 20, variable=var, value="Other", bg = 'lightblue').place(x=875,y=230)
    
    label_4 = Label(root, text="Phone Number",width=20,font=("bold", 15), bg = 'lightblue')
    label_4.place(x=520,y=280)

    entry_4 = Entry(root,textvar=Phone, width=40)
    entry_4.place(x=720,y=285)
    
    label_5 = Label(root, text="Password",width=20,font=("bold", 15), bg = 'lightblue')
    label_5.place(x=520,y=330)

    entry_5 = Entry(root,textvar=Password, show='*', width=40)
    entry_5.place(x=720,y=335)
    
    Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=720,y=480)
    conn.close()

       

# list1 = ['Philippines','Japan','Korea','China','Singapore','Hong kong'];
 
# droplist=OptionMenu(root,c, *list1)
# droplist.config(width=15)
# c.set('select your country') 
# droplist.place(x=240,y=280)
 
# label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
# label_4.place(x=85,y=330)
# var2= IntVar()
# Checkbutton(root, text="java", variable=var1).place(x=235,y=330)
 
# Checkbutton(root, text="python", variable=var2).place(x=290,y=330)
 

c = Registration()
root.mainloop()
