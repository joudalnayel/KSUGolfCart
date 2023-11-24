import hashlib #for passwerd
import sqlite3
import tkinter
import tkinter as tk
from tkinter import ttk, messagebox, END, filedialog as fd
import csv
import re

#dataBase:
KSUdb = sqlite3.connect('KSUGolfCarts.db')
KSUdb.execute(''' Create table IF NOT EXISTS PERSON
(
FirstName     CHAR (20)    NOT NULL,
LastName      CHAR (30)    NOT NULL,
user_class    CHAR (10)    NOT NULL,
SID_Number    CHAR(10)     PRIMARY KEY,
password      CHAR (15)    NOT NULL,
EmailAdress   CHAR (30)    NOT NULL,
Phone_Number  CHAR(15)     NOT NULL
); ''')

KSUdb.commit()
KSUdb.close()

#gui
class GUI:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("KSU GolfCartsn System")
        self.main.geometry('400x200')
        self.main.configure(bg="light blue")
        tk.Label(self.main,text="Welcom to ksu Golf Cartsn system!")

        self.ID = tk.StringVar()
        self.pas = tk.StringVar()
        self.idLabel = tk.Label(self.main, text="Enter your ID :", width=20, font=("bold", 10))
        self.idLabel.place(x=0, y=60)
        self.idEntry = tk.Entry(self.main, textvariable=self.ID)
        self.idEntry.place(x=170, y=60)

        self.passLabel = tk.Label(self.main, text="Password :", width=20, font=("bold", 10))
        self.passLabel.place(x=0, y=90)
        self.passEntry = tk.Entry(self.main, textvariable=self.pas, show='*')
        self.passEntry.place(x=170, y=90)

        login = tk.Button(self.main, text="Login", width=10, command=self.goLogin)
        login.place(x=120, y=130)
        signup = tk.Button(self.main, text="Sign up", width=10, command=self.sign_up)
        signup.place(x=220, y=130)
        self.main.mainloop()



    def sign_up(self):
        self.root = tk.Tk()
        self.root.geometry('400x350')
        self.root.title("Student Registration")





     # login (done)
    def goLogin(self):
        self.main.destroy()
        self.login()
# login window (done)
    def login(self):

        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title("KSU GolfLogin System")
        self.root.configure(bg="light blue")

        self.label_0 = tk.Label(self.root, text="log in ", width=20, font=("bold", 20))
        self.label_0.place(x=90, y=53)

        self.label_1L = tk.Label(self.root, text="ID :", width=20, font=("bold", 10))
        self.label_1L.place(x=90, y=130)
        self.entry_1L = tk.Entry(self.root)
        self.entry_1L.place(x=240, y=130)

        self.label_2P = tk.Label(self.root, text="Password :", width=20, font=("bold", 10))
        self.label_2P.place(x=90, y=180)
        self.entry_2P = tk.Entry(self.root,show='*')
        self.entry_2P.place(x=240, y=180)

        login = tk.Button(self.root, text="log in", command=self.logintodb)
        login.place(x=240, y=300)
        self.root.mainloop()
# login Button
    def logintodb(self):
        self.validId()# to check validity id
        self.validPass()  # to check validity pass
        id1 = str(self.entry_1L.get())
        countid = 0
        for x in id1:
            countid += 1
        if countid == 6: #go to admin window
            self.admin()
        elif countid == 10:#go to user window
            self.user()

    # validate ID (done)
    def validId( self):
        try:
            digit1 = int(self.entry_1L.get())
        except ValueError:
            tkinter.messagebox.showinfo('Erorr', 'ID should be 6 or 10 digits')
        id1 = str(self.entry_1L.get())
        countid = 0
        for x in id1:
            countid += 1
        if countid != 6 and countid != 10:
            tkinter.messagebox.showinfo('Erorr', 'ID should be 6 or 10 digit')
    # valid pass (not done)
    def validPass(self):
        conn = sqlite3.connect('KSUGolfCarts.db')
        temp = False
        passwerd = str(self.entry_2P.get())
        result = hashlib.sha256(passwerd.encode()).hexdigest()
        check=c.execute('SELECT password FROM PERSON ')
        print(check)
        for row in check:
            if row[0] == id:
                temp = True
        if temp !=True :
            messagebox.showinfo("Error", "Invalid password ")

    def admin(self):
        print()
    def user(self):
        print()


#to see the test
conn = sqlite3.connect('KSUGolfCarts.db')
c = conn.cursor()
c.execute("Select * from PERSON")
print(c.fetchall())
gui=GUI()
conn.commit()
print("************")
c.execute("Select * from PERSON")
print(c.fetchall())
conn.commit()
conn.close()

