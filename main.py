import hashlib #for passwerd
import sqlite3
import tkinter
import tkinter as tk
from tkinter import ttk, messagebox, END, filedialog as fd
import csv
import re
import datetime

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
KSUdb.execute('''
    CREATE TABLE IF NOT EXISTS GulfCarts (
        plate_number VARCHAR(20) PRIMARY KEY,
        college CHAR(30) NOT NULL
    )
''')
KSUdb.commit()
FirstName_admin = 'Areej'
LastName_Admin = 'Saad'
AdminClass='Employee'
ID_Admin = '123456'
Password = '000qqq'
password = hashlib.sha256(Password.encode()).hexdigest()
Email = 'Areej@ksu.edu.sa'
Phone_Number = '0512345678'
with KSUdb:
    KSUdb.execute("INSERT OR IGNORE INTO PERSON (FirstName, LastName, user_class, SID_Number, password, EmailAdress, Phone_Number) VALUES(?,?,?,?,?,?,?)",
                  (FirstName_admin, LastName_Admin, AdminClass, ID_Admin, password, Email, Phone_Number))

KSUdb.commit()
#gui
class GUI:
    def __init__(self):

        # SignUp
        # Create window
        self.root = tk.Tk()
        self.root.title("KSU GolfCartsn System")
        self.root.geometry('500x600')
        self.root.configure(bg="light blue")
        tk.Label(self.root, text="Welcom to ksu Golf Cartsn system!")
        self.root.iconphoto(False, tk.PhotoImage(file='logo2'))
        self.Signup()
        print("registration form  seccussfully created...")
        self.root.mainloop()

    def Signup(self):
        # Sign up label
        self.label_0 = tk.Label(self.root, text="Sign up ", width=20, font=("bold", 20))
        self.label_0.place(x=90, y=53)
        # First name label
        self.label_1 = tk.Label(self.root, text="First Name:", width=20, font=("bold", 10))
        self.label_1.place(x=90, y=130)
        self.entry_1 = tk.Entry(self.root)
        self.entry_1.place(x=240, y=130)
        # Last name label
        self.label_2 = tk.Label(self.root, text="Last Name", width=20, font=("bold", 10))
        self.label_2.place(x=90, y=180)
        self.entry_2 = tk.Entry(self.root)
        self.entry_2.place(x=240, y=180)
        # User class
        self.labelFS = tk.Label(self.root, text="Your Class", width=20, font=("bold", 10))
        self.labelFS.place(x=90, y=230)
        Class = ('Student', 'Faculty', 'Employee')
        self.selected_class = tk.StringVar()
        self.cbs = ttk.Combobox(self.root, textvariable=self.selected_class, width=17)
        self.cbs['values'] = Class
        self.cbs.place(x=240, y=230)
        # ID label
        self.label_6 = tk.Label(self.root, text="ID:", width=20, font=("bold", 10))
        self.label_6.place(x=90, y=280)
        self.entry_3 = tk.Entry(self.root)
        self.entry_3.place(x=240, y=280)
        # Password label
        self.label_4 = tk.Label(self.root, text="Password:", width=20, font=("bold", 10))
        self.label_4.place(x=90, y=330)
        self.entry_4 = tk.Entry(self.root)
        self.entry_4.place(x=240, y=330)
        # Email label
        self.label_5 = tk.Label(self.root, text="Email address:", width=20, font=("bold", 10))
        self.label_5.place(x=90, y=380)
        self.entry_5 = tk.Entry(self.root)
        self.entry_5.place(x=240, y=380)
        # Phone number label
        self.label_6 = tk.Label(self.root, text="Phone number:", width=20, font=("bold", 10))
        self.label_6.place(x=90, y=420)
        self.entry_6 = tk.Entry(self.root)
        self.entry_6.place(x=240, y=420)
        # Submit button
        self.SubmetButton = tk.Button(self.root, text='Submit', width=20, bg='brown', fg='white',
                                      command=self.Submit).place(x=180, y=450)

        self.SWallet = tk.Button(self.root, text='Login', width=20, bg='brown', fg='white',
                                 command=self.goLogin).place(x=180, y=490)
        # it is use for display the registration form on the window

        print("registration form  seccussfully created...")

        self.root.mainloop()
    def Submit(self):
        try:
            conn = sqlite3.connect('KSUGolfCarts.db')
            # validate password
            password = str(self.entry_4.get())
            reg = "^[A-Za-z0-9]{6,100}$"
            pat = re.compile(reg)
            x = re.search(pat, password)
            if not x:
                password = ''
                messagebox.showinfo("password format error!",
                                    "Re-enter a password number properly\rthat consists at least of 6 digits or letters")
            # first &last Name
            firstname = str(self.entry_1.get())
            lastname = str(self.entry_2.get())
            Class = str(self.selected_class.get())
            #selected class
            if self.selected_class.get()=='Student':
                # student id
                ID = str(self.entry_3.get())
                reg = "^[0-9]{10}$"
                pat = re.compile(reg)
                x = re.search(pat,ID)
            # validate studentID
                if not x:
                    ID = ''
                    messagebox.showinfo("ID Number error!", "Re-enter an ID number properly\rthat consists of 10 digits")
            else:
                ID = str(self.entry_3.get())
                reg = "^[0-9]{6}$"
                pat = re.compile(reg)
                x = re.search(pat, ID)
                # validate ID
                if not x:
                    ID = ''
                    messagebox.showinfo("ID Number error!",
                                        "Re-enter an ID number properly\rthat consists of 6 digits")

            # validate phone
            phoneNum = str(self.entry_6.get())
            reg2 = "^(05)[0-9]{8}$"
            pat2 = re.compile(reg2)
            y = re.search(pat2, phoneNum)
            if not y:
                phoneNum = ''
                messagebox.showinfo("Phone Number error!", "Re-enter an phone number properly\rthat "
                                                           "consists of 10 digits and starts with \'05\'")
                # validate email
            email = str(self.entry_5.get())
            reg = "^([a-zA-Z0-9\._-]+){8}(@ksu\.edu\.sa)$"
            pat = re.compile(reg)
            z = re.search(pat, email)
            if not z:
                email = ''
                messagebox.showinfo("Email  error!", "Re-enter Email properly\rthat "
                                                     "it should xxxxxxxx@ksu.edu.sa ")
            # insert,Check for doublaction
            found_id = c.execute(f"SELECT SID_Number FROM PERSON WHERE SID_Number = {ID}")
            password= hashlib.sha256(password.encode()).hexdigest()
            if len(found_id.fetchall()) == 0:
                sql = """INSERT INTO PERSON VALUES('{}','{}','{}','{}','{}','{}','{}')
                """.format(firstname, lastname,Class, ID, password, email, phoneNum,)
                c.execute(sql)
                conn.commit()

                # c.execute("Select * from StudentInfo")
                # print(c.fetchall())
            else:
                ID = ''
                messagebox.showinfo("ID already exist", "Reenter the correct ID again,"
                                                        "\rplease review your information and enter it correctly")
            conn.close()
        except sqlite3.Error:
            messagebox.showinfo("database error", "DataBase ERROR")

        except:
            messagebox.showinfo("ADD MISSION FAILED", "Due to incorrect or incompelte inputs,"
                                                      "\rplease review your information and enter it correctly")

# login (done)
    def goLogin(self):
        self.root.destroy()
        self.login()
# login window (done)
    def login(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title("KSU GolfLogin System")
        self.root.configure(bg="light blue")
        self.root.iconphoto(False,tk.PhotoImage(file='logo2'))

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
            self.submita()
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
    # valid pass ( done)
    def validPass(self):
        conn = sqlite3.connect('KSUGolfCarts.db')
        temp = False
        passwerd = str(self.entry_2P.get())
        result = hashlib.sha256(passwerd.encode()).hexdigest()
        check=c.execute('SELECT password FROM PERSON ')
        for row in check:
            if row[0] == result:
                temp = True
        if temp !=True :
            messagebox.showinfo("Error", "Invalid password ")

    def submita(self):
        self.root = tk.Tk()
        self.root.title("KSU Golf Carts System")
        self.root.geometry('500x500')
        self.root.configure(bg='light blue')
        self.root.iconphoto(False, tk.PhotoImage(file='logo2'))

        frame1 = tk.Frame(self.root)
        frame1.place(x=90, y=6)

        plateNum_label = tk.Label(frame1, text="Enter golf cart plate number: ", width=20, font=("bold", 10))
        plateNum_label.pack()
        self.plate_entry = tk.Entry(frame1)
        self.plate_entry.configure(width=15)
        self.plate_entry.pack()

        college_label = tk.Label(frame1, text="Enter golf cart's college:", width=20, font=("bold", 10))
        college_label.pack()
        self.college_entry = tk.Entry(frame1)
        self.college_entry.configure(width=15)
        self.college_entry.pack()

        submit_button = tk.Button(frame1, text="Submit", command=self.submittt)
        submit_button.pack()

        logout_button = tk.Button(frame1, text="Logout", command=self.Signup)
        logout_button.pack()

        backup_button = tk.Button(frame1, text="Backup", command=self.backup)
        backup_button.pack()

        frame1.pack()

        self.root.mainloop()

    def submittt(self):
        # plate_number = plate_entry.get()
        # college = college_entry.get()
        # Send information to the central database

        plate_number = self.plate_entry.get()
        college = str(self.college_entry.get())
        print("Sending data to database: plate_number= ", plate_number, "college= ", college)

    def logout(self):
        self.root.destroy()
        # sing_up()
        print("Returning to sign-up window")

    def backup(self):
        # Backup all information of the central database into a CSV file format
        conn = sqlite3.connect('KSUGolfCarts.db')
        file = open('GulfCartDB.csv', "w", newline="")
        csvwiter = csv.writer(file)
        cursor = conn.execute("SELECT * from PERSON")
        fields = "First_Name,Last_Name,Class,ID,Password,Email,Phone_Number"
        csvwiter.writerow(fields.split(","))
        for row in cursor:
            csvwiter.writerow(row)
        print("Backing up data to CSV file")

    def user(self):
        print()


#to see the test
conn = sqlite3.connect('KSUGolfCarts.db')
c = conn.cursor()
c.execute("Select * from PERSON")
print(c.fetchall())
gui=GUI()
conn.commit()
conn.close()
