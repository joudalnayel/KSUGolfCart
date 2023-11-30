import hashlib #for passwerd
import sqlite3
import tkinter
import tkinter as tk
from tkinter import ttk, messagebox, END, filedialog as fd
import csv
import re
from datetime import datetime, timedelta
import datetime
import logging
from datetime import datetime
logging.basicConfig(filename='KSUGolfCarts.log',
                   filemode='w',
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   level=logging.DEBUG)

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
# Create the table for storing user reservations
KSUdb.execute('''
    CREATE TABLE IF NOT EXISTS Reservations (
        UserID        CHAR(10)     NOT NULL,
        Cart          CHAR(20)     NOT NULL,
        StartDate     DATETIME         NOT NULL,
        EndDate       DATETIME         NOT NULL,
        PRIMARY KEY ( StartDate, EndDate)
    );
''')
KSUdb.commit()
# admin info
FirstName_admin = 'Areej'
LastName_Admin = 'Saad'
AdminClass='Admin'
ID_Admin = '123456'
Password = '000qqq'
password = hashlib.sha256(Password.encode()).hexdigest()
Email = 'Areej@ksu.edu.sa'
Phone_Number = '0512345678'
#insert admin info to database
with KSUdb:
    KSUdb.execute("INSERT OR IGNORE INTO PERSON (FirstName, LastName, user_class, SID_Number, password, EmailAdress, Phone_Number) VALUES(?,?,?,?,?,?,?)",
                  (FirstName_admin, LastName_Admin, AdminClass, ID_Admin, password, Email, Phone_Number))

KSUdb.commit()
#gui
class GUI:
    def __init__(self):
        # SignUp
        # SignUp window
        self.Signup()
        print("registration form  seccussfully created...")
        self.root.mainloop()

    # SignUp window
    def Signup(self):
        self.root = tk.Tk()
        self.root.title("KSU GolfCartsn System")
        self.root.geometry('500x600')
        self.root.configure(bg="light blue")
        tk.Label(self.root, text="Welcom to ksu Golf Cartsn system!")
        self.root.iconphoto(False, tk.PhotoImage(file='logo2'))

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
        # Login button
        self.SWallet = tk.Button(self.root, text='Login', width=20, bg='brown', fg='white',
                                 command=self.goLogin).place(x=180, y=490)
        # it is use for display the registration form on the window

        print("registration form  seccussfully created...")

        self.root.mainloop()

    #  check and Submit all user info
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
                # 'Faculty', 'Employee' id
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
            if len(found_id.fetchall()) == 0:#no doublaction
                sql = """INSERT INTO PERSON VALUES('{}','{}','{}','{}','{}','{}','{}')
                """.format(firstname, lastname,Class, ID, password, email, phoneNum,)
                c.execute(sql)
                conn.commit()


            else:# ther isdoublaction
                ID = ''
                messagebox.showinfo("ID already exist", "Reenter the correct ID again,"
                                                        "\rplease review your information and enter it correctly")
            conn.close()
        except sqlite3.Error:
            messagebox.showinfo("database error", "DataBase ERROR")

        except:
            messagebox.showinfo("ADD MISSION FAILED", "Due to incorrect or incompelte inputs,"
                                                      "\rplease review your information and enter it correctly")

# login
    def goLogin(self):
        self.root.destroy()
        self.login()#login window
# login window
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
        if id1=='123456':#go to admin window
            self.admin()
        countid = 0
        for x in id1:
            countid += 1
        if countid == 6 or countid == 10: #go to user window
            self.user(id1)

    # validate ID
    def validId( self):
        try:
            digit1 = int(self.entry_1L.get())
        except ValueError:#if enter letters
            tkinter.messagebox.showinfo('Erorr', 'ID should be 6 or 10 digits')
        id1 = str(self.entry_1L.get())
        conn = sqlite3.connect('KSUGolfCarts.db')
        temp = False
        check = c.execute('SELECT SID_Number FROM PERSON ')
        for row in check:
            if row[0] == id1:
                temp = True
        if temp != True:
            messagebox.showinfo("Error", "Invalid id ")
            self.root.mainloop()
    # valid pass
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
            self.root.mainloop()

    #admin window
    def admin(self):
        self.root.destroy()
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

        submit_button = tk.Button(frame1, text="Create", command=self.create)
        submit_button.pack()

        logout_button = tk.Button(frame1, text="Logout", command=self.logout)
        logout_button.pack()

        backup_button = tk.Button(frame1, text="Backup", command=self.backup)
        backup_button.pack()

        frame1.pack()

        self.root.mainloop()
    #create Button
    def create(self):
        plate_number = self.plate_entry.get()
        college = str(self.college_entry.get())
        # Send information to the central database
        with KSUdb:
            KSUdb.execute(
                "INSERT OR IGNORE INTO GulfCarts (plate_number, college) VALUES(?,?)",
                (plate_number, college))
        print("Sending data to database: plate_number= ", plate_number, "college= ", college)

    # logout Button
    def logout(self):
        self.root.destroy()
        self.Signup()
        print("Returning to sign-up window")

    # backup Button
    def backup(self):
        # Backup all information of the central database into a CSV file format
        # backing up user's information
        conn = sqlite3.connect('KSUGolfCarts.db')
        file = open('GulfCartDB.csv', "w", newline="")
        csvwiter = csv.writer(file)
        cursor = conn.execute("SELECT * from PERSON")
        fields = "First_Name,Last_Name,Class,ID,Password,Email,Phone_Number"
        csvwiter.writerow(fields.split(","))
        for row in cursor:
            csvwiter.writerow(row)
        # backing up gulf carts information
        cursor2 = conn.execute("SELECT * from GulfCarts")
        fields = "plate_number,college"
        csvwiter.writerow(fields.split(","))
        for row in cursor2:
            csvwiter.writerow(row)
        # backing up Reservations information
        cursor3 = conn.execute("SELECT * from Reservations")
        fields = "UserID,Cart,StartDate,EndDate"
        csvwiter.writerow(fields.split(","))
        for row in cursor3:
            csvwiter.writerow(row)

        print("Backing up data to CSV file")

    # user window
    def user(self, userid):
        self.root.destroy()
        self.userid = userid
        self.reservations = []  # Store user reservations

        self.userWindow = tk.Tk()
        self.userWindow.title("User Window")
        self.userWindow.iconphoto(False, tk.PhotoImage(file='logo2'))

        self.notebook = ttk.Notebook(self.userWindow)# to manage many tabs
        self.reserve_tab = ttk.Frame(self.notebook)#reserve_tab
        self.view_tab = ttk.Frame(self.notebook)#view_tab


        self.notebook.add(self.reserve_tab, text='Reserve a Cart')
        self.notebook.add(self.view_tab, text='View my Reservations')

        self.setup_reserve_tab()# go to reserve tab
        self.setup_view_tab()# go to view tap

        self.notebook.pack(expand=1, fill='both')
        self.userWindow.mainloop()

    def setup_reserve_tab(self):
        label = tk.Label(self.reserve_tab, text="Select a golf cart and enter reservation details:")
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Widgets for Reserve a Cart tab
        self.cart_listbox = tk.Listbox(self.reserve_tab, selectmode=tk.SINGLE)
        self.cart_listbox.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)

        self.load_cart_list()# file the list box

        #Start Time & Date
        tk.Label(self.reserve_tab, text="Start Time & Date:").grid(row=2, column=0, pady=5, padx=10, sticky=tk.W)
        self.start_entry = tk.Entry(self.reserve_tab)
        self.start_entry.grid(row=2, column=1, pady=5, padx=10, sticky=tk.W)

        # End Time & Date
        tk.Label(self.reserve_tab, text="End Time & Date:").grid(row=3, column=0, pady=5, padx=10, sticky=tk.W)
        self.end_entry = tk.Entry(self.reserve_tab)
        self.end_entry.grid(row=3, column=1, pady=5, padx=10, sticky=tk.W)

        # reserve button
        reserve_button = tk.Button(self.reserve_tab, text="Reserve", command=self.reserve_cart)
        reserve_button.grid(row=4, column=0, pady=10, padx=10, sticky=tk.W)

        # logout button
        logout_button = tk.Button(self.reserve_tab, text="Logout", command=self.logout2)
        logout_button.grid(row=4, column=1, pady=10, padx=10, sticky=tk.W)

    def setup_view_tab(self):
        label = tk.Label(self.view_tab, text="View your active reservations:")
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Widgets for View my Reservations tab
        self.reservations_listbox = tk.Listbox(self.view_tab)
        self.reservations_listbox.grid(row=1, column=0, pady=5, padx=10, columnspan=2, sticky=tk.W)

        # show button
        show_button = tk.Button(self.view_tab, text="Show Reservations", command=self.view_reservations)
        show_button.grid(row=2, column=0, pady=10, padx=10, sticky=tk.W)

        # logout button
        logout_button = tk.Button(self.view_tab, text="Logout", command=self.logout2)
        logout_button.grid(row=2, column=1, pady=10, padx=10, sticky=tk.W)

    # load cart list
    def load_cart_list(self):

        #git plate_numbers and colleges frome database
        with KSUdb:
            plate_numbers = KSUdb.execute("SELECT plate_number FROM GulfCarts").fetchall()
            colleges = KSUdb.execute("SELECT college FROM GulfCarts").fetchall()

            # combination plate_numbers and colleges togather
            carts = [f"{plate[0]} - {college[0]}" for plate, college in zip(plate_numbers, colleges)]

        # Clear existing items in the listbox
        self.cart_listbox.delete(0, tk.END)
        # Populate the listbox with the retrieved carts
        for cart in carts:
            self.cart_listbox.insert(tk.END, cart)

    # reserve button
    def reserve_cart(self):
        selected_cart = self.cart_listbox.get(tk.ACTIVE)
        start_time = self.start_entry.get()
        end_time = self.end_entry.get()


        # Placeholder logic, replace with actual reservation logic
        if not selected_cart or not start_time or not end_time:# if did not fill in all fields
            messagebox.showerror("Error", "Please fill in all fields.")
            logging.info(
                f'{self.userid} {selected_cart} {start_time} {end_time} did not fill in all fields.')
        else:
            # Check reservation time validity based on user class
            user_class = self.get_user_class(self.userid)
            if not self.validate_reservation_time(user_class, start_time, end_time):#Reservation duration ok or not
                logging.info(
                f'{self.userid} {selected_cart} {start_time} {end_time} fill')
                return

            # Placeholder: Check availability and reserve the cart
            if self.check_cart_availability(selected_cart, start_time, end_time):#Check if there are any reservations for the selected cart during the specified time
                self.reservations.append({
                    "cart": selected_cart,
                    "start_time": start_time,
                    "end_time": end_time
                })
                messagebox.showinfo("Success", "Cart reserved successfully.")
                logging.info(f'{self.userid} {selected_cart} {start_time} {end_time} Cart reserved successfully.')


                # Convert date strings to datetime objects
                start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
                end_datetime = datetime.strptime(end_time, "%Y-%m-%d %H:%M")
                entry_1d=str(self.userid)

                #  INSERT Reservations in database
                conn = sqlite3.connect('KSUGolfCarts.db')
                c = conn.cursor()
                print(entry_1d, selected_cart, start_datetime, end_datetime)
                with KSUdb:
                    KSUdb.execute(
                        "INSERT OR IGNORE INTO Reservations (UserID, Cart, StartDate, EndDate) VALUES(?,?,?,?)",
                        (entry_1d, selected_cart, start_datetime, end_datetime)
                    )
                conn.commit()

            else:
                messagebox.showerror("Error", "Cart is not available during the specified time.")
                logging.info(f'{self.userid} {selected_cart} {start_time} {end_time} not available during the specified time.')

    # Validate reservation time based on user class
    def validate_reservation_time(self, user_class, start_time, end_time):
        reservation_duration = datetime.strptime(end_time, "%Y-%m-%d %H:%M") - datetime.strptime(start_time,
                                                                                                 "%Y-%m-%d %H:%M")

        if user_class == "student" and reservation_duration > timedelta(minutes=30):
            messagebox.showerror("Error", "Reservation duration cannot exceed 30 minutes for students.")
            return False
        elif user_class == "employee" and reservation_duration > timedelta(hours=1):
            messagebox.showerror("Error", "Reservation duration cannot exceed 1 hour for employees.")
            return False
        elif user_class == "faculty" and reservation_duration > timedelta(hours=1, minutes=30):
            messagebox.showerror("Error", "Reservation duration cannot exceed 1 hour and 30 minutes for faculty.")
            return False

        return True

    # check if  cart is availability
    def check_cart_availability(self, cart, start_time, end_time):
        # Check cart availability

            try:
                conn = sqlite3.connect('KSUGolfCarts.db')
                c = conn.cursor()
                start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
                end_datetime = datetime.strptime(end_time, "%Y-%m-%d %H:%M")

                # Check if there are any reservations for the selected cart during the specified time range
                c.execute('''
                            SELECT * FROM Reservations
                            WHERE Cart = ? AND (
                                (StartDate <= ? AND EndDate >= ?)
                                OR (StartDate <= ? AND EndDate >= ?)
                                OR (StartDate >= ? AND StartDate <= ? AND EndDate >= ?)
                            )
                                ''', (cart, start_datetime, start_datetime, end_datetime,end_datetime, start_datetime,
                                    end_datetime,start_datetime,
                                         ))

                reservations = c.fetchall()

                if reservations:
                    messagebox.showinfo("Cart Not Available",
                                        "The selected cart is not available during the specified time.")
                    return False
                else:
                    return True

            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Error reading data from the database: {str(e)}")
                return False
            finally:
                conn.close()

    # view reservations
    def view_reservations(self):
        self.reservations_listbox.delete(0, tk.END)
        for reservation in self.reservations:
            self.reservations_listbox.insert(tk.END,
                                             f"{reservation['cart']} - {reservation['start_time']} to {reservation['end_time']}")

    # Determine user class based on user ID
    def get_user_class(self, user_id):
        # Determine user class based on user ID
        conn = sqlite3.connect('KSUGolfCarts.db')
        c = conn.cursor()
        check = c.execute('SELECT user_class FROM PERSON WHERE SID_Number = ?', (user_id,))
        user_class = check.fetchone()
        conn.close()  # Close the connection after fetching results

        if user_class:
            user_class = user_class[0].lower()  # Convert to lowercase
            if user_class == "student":
                print("Student")
                return "student"
            elif user_class == "faculty":
                print("Faculty")
                return "faculty"
            elif user_class == "employee":
                print("Employee")
                return "employee"

    def logout2(self):
        self.userWindow.destroy()
        self.Signup()

#to see the test
conn = sqlite3.connect('KSUGolfCarts.db')
c = conn.cursor()
c.execute("Select * from PERSON")
print(c.fetchall())
c.execute("Select * from GulfCarts")
print(c.fetchall())
c.execute("Select * from Reservations")
print(c.fetchall())
conn.commit()
gui=GUI()
conn.commit()
conn.close()

