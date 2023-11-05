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

        login = tk.Button(self.main, text="Login", width=10, command=self.login)
        login.place(x=120, y=130)
        signup = tk.Button(self.main, text="Sign up", width=10, command=self.sign_up)
        signup.place(x=220, y=130)
        self.main.mainloop()



    def sign_up(self):
        self.root = tk.Tk()
        self.root.geometry('400x350')
        self.root.title("Student Registration")





    def login(self):
        print("hiii")
