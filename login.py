from tkinter import *
import sqlite3
import tkinter.messagebox
from tkinter import messagebox

def login():
    conn = sqlite3.connect('database1.db')
    
    email=user_input.get()
    passwd=pass_input.get()

    
    conn.execute('CREATE TABLE IF NOT EXISTS login(email TEXT, password TEXT)')
    conn.execute('INSERT INTO login(email, password) VALUES(?,?)',(email, passwd))
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM register WHERE email=? AND password=?",(user_input.get(), pass_input.get()))
    row=cursor.fetchone()
    if row:
        messagebox.showinfo('info', 'Login Success')
        root.destroy()
        import appointment
    elif email == '' or passwd == '':
        tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
    else:
        messagebox.showinfo('info', 'Login FAILED')
    cursor.connection.commit()
    conn.close()    

def appointment_page():
    conn = sqlite3.connect('database1.db')
    root.destroy()
    import appointment
    conn.close()
        
            
root=tkinter.Tk()
root.title('Login')
root.geometry('1920x1080')
root.configure(bg = 'lightblue')
padd=20
root['padx']=padd

user_input=tkinter.StringVar()
pass_input=tkinter.StringVar()

info_label = tkinter.Label(root, text="Login form",width=20,font=("bold", 23), bg = 'lightblue')
info_label.place(x=600,y=53)
# info_label=tkinter.Label(root, text='Login')
# info_label.grid(row=0,column=0, pady=20)

info_user =tkinter.Label(root, text="Email", width=20, font=("bold", 15), bg = 'lightblue')
info_user.place(x=520,y=150)
# info_user=tkinter.Label(root, text='Username')
# info_user.grid(row=1,column=0)

info_user =tkinter.Entry(root,textvar=user_input, width=40)
info_user.place(x=720,y=155)
# userinput=tkinter.Entry(root, textvariable=user_input)
# userinput.grid(row=1,column=1)

info_pass = tkinter.Label(root, text="Password",width=20,font=("bold", 15), bg = 'lightblue')
info_pass.place(x=520,y=250)
# info_pass=tkinter.Label(root, text='Password')
# info_pass.grid(row=2,column=0, pady=20)

passinput = tkinter.Entry(root,textvar=pass_input, width=40, show='*')
passinput.place(x=720,y=255)
# passinput=tkinter.Entry(root, textvariable=pass_input)
# passinput.grid(row=2,column=1)

Button(root, text='Login',width=20,bg='brown',fg='white', command=login).place(x=720,y=380)
# login_btn=tkinter.Button(text='Login', command=login)
# login_btn.grid(row=3,column=1)
root.mainloop()

#lambda:[login(), appointment_page()]