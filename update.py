# update the appointments
from tkinter import *
import tkinter.messagebox 
import sqlite3

conn = sqlite3.connect('database2.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master

        self.left = Frame(master, width=1080, height=1920, bg='lightblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=1080, height=1920, bg='lightblue')
        self.right.pack(side=RIGHT)

        #title of the window
        self.master.title('MAV HOSPTIAL')
        
        # heading label
        self.heading = Label(master, text="Update Appointments",  fg='black', bg ='lightblue', font=('arial 40 bold'))
        self.heading.place(x=550, y=0)

        # search criteria -->name 
        self.name = Label(master, text="Enter Patient's Name", fg='black', bg ='lightblue', font=('arial 18 bold'))
        self.name.place(x=450, y=80)  ##0, 60

        # entry for  the name
        self.namenet = Entry(master, width=30, font=('arial 20'))
        self.namenet.place(x=730, y=82)    ##280, 62

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=720, y=142)

    # function to search
    def search_db(self):
        self.input = self.namenet.get()
        # execute sql 

        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        # creating the update form
        self.uname = Label(self.master, text="Patient's Name", fg='black', bg ='lightblue', font=('arial 18 bold'))
        self.uname.place(x=450, y=200) ##0, 140

        self.uage = Label(self.master, text="Age", fg='black', bg ='lightblue', font=('arial 18 bold'))
        self.uage.place(x=450, y=260) ##0, 180

        self.ugender = Label(self.master, text="Gender", fg='black', bg ='lightblue', font=('arial 18 bold'))
        self.ugender.place(x=450, y=320)    ##0, 220

        self.ulocation = Label(self.master, text="Location", fg='black', bg ='lightblue', font=('arial 18 bold'))
        self.ulocation.place(x=450, y=380)   ##0, 260

        self.utime = Label(self.master, text="Appointment Time", fg='black', bg ='lightblue', font=('arial 18 bold'))
        self.utime.place(x=450, y=440)   ##0, 300

        self.uphone = Label(self.master, text="Phone Number", fg='black', bg ='lightblue', font=('arial 18 bold'))
        self.uphone.place(x=450, y=500)  ##0, 340

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=25, font=('arial 18'))
        self.ent1.place(x=750, y=200)   ##300, 200
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master,  width=25, font=('arial 18'))
        self.ent2.place(x=750, y=260)   ##300, 180
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master,  width=25, font=('arial 18'))
        self.ent3.place(x=750, y=320)   ##300, 220
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=25, font=('arial 18'))
        self.ent4.place(x=750, y=380)  ##300, 260
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master,  width=25, font=('arial 18'))
        self.ent5.place(x=750, y=440)  ##300, 300
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master,  width=25, font=('arial 18'))
        self.ent6.place(x=750, y=500)  ##300, 340
        self.ent6.insert(END, str(self.phone))

        # button to execute update
        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=540, y=600)

        # button to delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=860, y=600)
        
        self.display = Button(self.master, text="Display", width=20, height=2, bg='blue', command=self.display_page)
        self.display.place(x=700, y=700)
        
    def display_page(self):
        root.destroy()
        import display
        
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated age
        self.var3 = self.ent3.get() #updated gender
        self.var4 = self.ent4.get() #updated location
        self.var5 = self.ent5.get() #updated phone
        self.var6 = self.ent6.get() #updated time

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
# creating the object
root = Tk()
b = Application(root)
root.geometry("1920x1080+0+0")
root.resizable(True, True)
root.mainloop()
