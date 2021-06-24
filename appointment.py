# import modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox

# connect to the databse.
conn = sqlite3.connect('database2.db')
# cursor to move around the databse
cursor = conn.cursor()

# empty list to later append the ids from the database
ids = []

# tkinter window
class Application:
    # conn = sqlite3.connect('database1.db')
    # initialising the constructor
    
    def __init__(self, master):
        # conn = sqlite3.connect('database1.db')
        
        self.master = master

        # creating the frames in the master

        self.left = Frame(master, width=1080, height=1920, bg='lightblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=1080, height=1920, bg='lightblue')
        self.right.pack(side=RIGHT)

        # Title of the window
        self.master.title('MAV Hospital')

        # labels for the window
        self.heading = Label(self.left, text="MAV Hospital Appointments", font=('arial 30 bold'), fg='black', bg='lightblue')
        self.heading.place(x=500, y=0)
       
        # patients name
        self.name = Label(self.left, text="Patient's Name", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.name.place(x=400, y=200)

        # age
        self.age = Label(self.left, text="Age", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.age.place(x=400, y=260)

        # gender
        self.gender = Label(self.left, text="Gender", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.gender.place(x=400, y=320)

        # location
        self.location = Label(self.left, text="Location", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.location.place(x=400, y=380)

        # appointment time
        self.time = Label(self.left, text="Appointment Time", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.time.place(x=400, y=440)
        

        # phone
        self.phone = Label(self.left, text="Phone Number", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.phone.place(x=400, y=500)
        
        # available doctor
        self.doctor = Label(self.left, text="Available Doctor", font=('arial 20 bold'), fg='black', bg='lightblue')
        self.doctor.place(x=400, y=560)
        
 ######################################################################################################################################################      

        # Entries for all labels============================================================
        self.name_ent = Entry(self.left, width=50, font=('arial 17'))
        self.name_ent.place(x=670, y=200)

        self.age_ent = Entry(self.left, width=50, font=('arial 17'))
        self.age_ent.place(x=670, y=260)
    
        self.gender_ent = Entry(self.left, width=50, font=('arial 17'))
        self.gender_ent.place(x=670, y=320)

        self.location_ent = Entry(self.left, width=50, font=('arial 17'))
        self.location_ent.place(x=670, y=380)

        self.c = StringVar()
        list1 = ['10:00 AM','10:30 AM','11:00 AM','11:30 AM','12:00 AM','12:30 AM'];
        droplist1=OptionMenu(root,self.c, *list1)
        droplist1.config(width=61)
        self.c.set('Select your Appointment time') 
        droplist1.place(x=670,y=440)
        
        self.d = StringVar()
        list2 = ['Dr. Alex','Dr. Suzan','Dr. Brandon','Dr. Elizabeth'];
        droplist2=OptionMenu(root,self.d, *list2)
        droplist2.config(width=61)
        self.d.set('Select your Doctor') 
        droplist2.place(x=670,y=560)
        #time_available = ttk.Combobox(root, width= 50, textvariable = my_str_var, values=['10:00','10:30','11:00','11:30','12:00','12:30'])

        self.phone_ent = Entry(self.left, width=50, font=('arial 17'))
        self.phone_ent.place(x=670, y=500)
        
        # self.doctor_ent = Entry(self.left, width=50, font=('arial 17'))
        # self.doctor_ent.place(x=670, y=440)

        # button to perform a command
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, fg = 'yellow' ,bg='black', command=self.add_appointment)
        self.submit.place(x=400, y=650) # x = 680
        
        self.display = Button(self.left, text="Display", width=20, height=2, fg = 'yellow' ,bg='black', command=self.display_page)
        self.display.place(x=650, y=650)
        
        self.update = Button(self.left, text="Update", width=20, height=2, fg = 'yellow' ,bg='black', command=self.update_page)
        self.update.place(x=900, y=650)

        # getting the number of appointments fixed to view in the log
        # sql2 = "SELECT ID FROM appointments "
        # self.result = cursor.execute(sql2)
        # for self.row in self.result:
        #     self.id = self.row[0]
        #     ids.append(self.id)
        
        # # ordering the ids
        # self.new = sorted(ids)
        # self.final_id = self.new[len(ids)-1]
        # conn.close()
    
        # displaying the logs in our right frame
##        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
##        self.logs.place(x=0, y=0)

##        self.box = Text(self.right, width=50, height=40)
##        self.box.place(x=20, y=60)
##        self.box.insert(END, "Total Appointments till now :  " + str(self.final_id))

    def display_page(self):
        # conn = sqlite3.connect('database1.db')
        root.destroy()
        import display
        # conn.close()
        
    def update_page(self):
        # conn = sqlite3.connect('database1.db')
        root.destroy()
        import update
        # conn.close()
    
    
    # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user 
        #conn = sqlite3.connect('database1.db')
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.c.get()
        self.val6 = self.phone_ent.get()
        self.val7 = self.d.get()
        
        
        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '' or self.val7 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        elif len(self.val6) != 10:    
            tkinter.messagebox.showinfo("Warning", "Please Enter 10 Digits in Phone")    
        
        else:
            try:
                #cursor.execute('CREATE TABLE IF NOT EXISTS appoint (name TEXT, age INT, gender TEXT, location TEXT, scheduled_time TEXT, phone TEXT, doctors TEXT)')
                cursor.execute('INSERT INTO appointments (name, age, gender, location, scheduled_time, phone, doctors) VALUES(?, ?, ?, ?, ?, ?, ?)',(self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7))
                #cursor.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7))
                conn.commit()
                tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1) + " has been created")
                self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))
                root.destroy()
                import display
            except sqlite3.IntegrityError as err:
                print(err)
                #c.execute('SELECT scheduled_time FROM appointments WHERE scheduled_time=?', (scheduled_time))
                tkinter.messagebox.showwarning("Time Slot", "Appointment Not Available")    
            
        
# try:
#         		# now we add to the database
# 				sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
# 				c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
# 				conn.commit()
# 				tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1) + " has been created" )
#                 c.execute('SELECT scheduled_time FROM appointments WHERE scheduled_time=?', (scheduled_time))
# 	            self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))
#             except:
#                 tkinter.messagebox.showwarning("showwarning", "Time Taken")
        			
        

# creating the object
root = tk.Tk()
b = Application(root)

# c = tk.StringVar()
# list1 = ['10:00','10:30','11:00','11:30','12:00','12:30'];
# droplist1=OptionMenu(root,c, *list1)
# droplist1.config(width=61)
# c.set('Select your Appointment time') 
# droplist1.place(x=670,y=440)


# d = tk.StringVar()
# list2 = ['Dr. Alex','Dr. Suzan','Dr. Brandon','Dr. Elizabeth'];
# droplist2=OptionMenu(root,d, *list2)
# droplist2.config(width=61)
# d.set('Select your Doctor') 
# droplist2.place(x=670,y=560)


# my_str_var = tk.StringVar()
# time_available = ttk.Combobox(root, width= 30, state="readonly", textvariable = my_str_var, font=('arial 17'), values=['10:00 AM','10:30 AM','11:00 AM','11:30 AM','12:00 AM','12:30 AM'])
# time_available.place(x=670,y=440)

# str_var = tk.StringVar()
# doctor_available = ttk.Combobox(root, width= 30, state="readonly", textvariable = str_var, font=('arial 17'), values=['Dr. Alex','Dr. Suzan','Dr. Brandon','Dr. Elizabeth'])
# doctor_available.place(x=670,y=560)

# resolution of the window
root.geometry("1920x1080+0+0")

# preventing the resize feature
root.resizable(True, True)

# end the loop
root.mainloop()
