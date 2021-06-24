from tkinter import *
import sqlite3
import pyttsx3

# connection to database
conn = sqlite3.connect('database2.db')
c = conn.cursor()

# empty lists to append later
number = []
patients = []
time = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    times = r[6]
    number.append(ids)
    patients.append(name)
    time.append(times)

# window
class Application:
    def __init__(self, master):
        self.master = master

        self.x = 0

        #Frame

        self.left = Frame(master, width=1080, height=1920, bg='skyblue')
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=1080, height=1920, bg='skyblue')
        self.right.pack(side=RIGHT)

        #title of the window
        self.master.title('MAV HOSPTIAL')
        
        # heading
        self.heading = Label(master, text="Appointments", font=('arial 60 bold'), fg='black', bg = 'skyblue')
        
        self.heading.place(x=500, y=0)
        

        # button to change patients
        self.change = Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.func)
        self.change.place(x=700, y=650)

        # empty text labels to later config
        self.n = Label(master, text="", font=('arial 60 bold'),fg='black', bg = 'skyblue')
        self.n.place(x=500, y=300)
        
        self.pname = Label(master, text="", font=('arial 60 bold'),fg='black', bg = 'skyblue')
        self.pname.place(x=700, y=300)
        
        self.login = Button(master, text="Login Page", width=25, height=2, bg='steelblue', command=self.login_page)
        self.change.place(x=700, y=650)
        
        self.sch_time = Label(master, text="", font=('arial 60 bold'),fg='black', bg = 'skyblue')
        self.sch_time.place(x=1100, y=300)
        

    def login_page(self):
        root.destroy()
        import update
        
            
    # function to speak the text and update the text
    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        self.sch_time.config(text=str(time[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x] + 'at' + str(time[self.x])))
        engine.runAndWait()
        self.x += 1
root = Tk()
b = Application(root)
root.geometry("1920x1080")
root.resizable(True, True)
root.mainloop()
