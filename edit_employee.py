from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import mysql.connector
from subprocess import call

def system():
    root = Tk()
    root.geometry("900x750")
    root.title("Admin Mood")

    ############database###########
    def Database():
        global conn, cursor
        # creating system database
        conn = sqlite3.connect("rms.db")
        cursor = conn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS edit_employee(Employee_Name,Contact_Number,Address,Designation)")

    def back():
        root.destroy()
        call(['python', "after_admin_login_pg.py"])

    # variable datatype assignment
    e1 = StringVar()
    e2 = StringVar()
    e3 = StringVar()
    e4 = StringVar()

    def reset():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)

    def exit():
        root.destroy()

    # Topframe
    topframe = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
    topframe.pack(side=TOP)
    # Leftframe
    leftframe = Frame(root, width=900, height=700, relief=SUNKEN)
    leftframe.pack(side=LEFT)
    # rightframe
    rightframe = Frame(root, width=600, height=700, relief=SUNKEN)
    rightframe.pack(side=RIGHT)

    ################## display data ####################
    def DisplayData():

        connect = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
        conn = connect.cursor()
        conn.execute("SELECT * FROM `edit_employee`")

        i = 0
        for ro in conn:
            my_tree.insert('', i, text="", values=(ro[0], ro[1], ro[2]))
            i = i + 1


    # add some style
    style = ttk.Style()
    style.theme_use("classic")

    style.configure("Treeview",
                    background="#ffd699",
                    foregroung="black",
                    rowheight=30,
                    fieldbackground="white"
                    )
    style.map('Treeview',
              background=[('selected', '#e67f30')])

    ###########  Creating table #############
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("Employee name", "Contact Number", "Address", "Designation")
    ############ creating  for table ################
    hsb = ttk.Scrollbar(rightframe, orient="horizontal")
    hsb.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    vsb = ttk.Scrollbar(rightframe, orient="vertical")
    vsb.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)
    # defining column for table
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("Employee name", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("Contact Number", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("Address", anchor=CENTER, width=60, minwidth=25)
    my_tree.column("Designation", anchor=CENTER, width=60, minwidth=25)

    # defining  headings for table
    my_tree.heading("Employee name", text="Employee Name", anchor=CENTER)
    my_tree.heading("Contact Number", text="Contact Number", anchor=CENTER)
    my_tree.heading("Address", text="Address", anchor=CENTER)
    my_tree.heading("Designation", text="Designation", anchor=CENTER)




    my_tree.pack()
    DisplayData()

    def add():
        Database()

        Employeename = e1.get()
        Contactno = e2.get()
        Address = e3.get()
        Designation = e4.get()


        if Employeename == "" or Contactno == "" or Address == "" or Designation == "":
            messagebox.showinfo("Warning", "fill the empty field!!!")
        else:

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
            cursor = mysqldb.cursor()
            sql = "INSERT INTO edit_employee (Employee_Name, Contact_Number, Address, Designation) VALUES (%s,%s,%s,%s)"
            val = (Employeename,Contactno,Address,Designation)
            cursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("Message", "Stored successfully")

        DisplayData()
        conn.close()

    # access data from sqlite
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = conn.execute("SELECT * FROM edit_employee")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    # defining function to delete record
    def Delete():
        # open database
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                            icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)


            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
            mycursor = mysqldb.cursor()
            sql = "DELETE FROM edit_employee WHERE Designation =" + str(selecteditem[2]) + ""
            mycursor.execute(sql)
            mysqldb.commit()


    localtime = time.asctime(time.localtime(time.time()))

    infolb = Label(topframe, font=('vardana', 30, 'bold'), text="Edit Employee", fg="pink", bd=10,
                   anchor=W)
    infolb.grid(row=0, column=0)
    infolb = Label(topframe, font=('varadana', 20,), text=localtime, fg="black", anchor=W)
    infolb.grid(row=1, column=0)

    #Employeename
    empnmlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Employee Name", fg="black", bd=10, anchor=W).grid(row=1,
                                                                                                             column=0)

    #Contactnumber
    catlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Contact Number", fg="black", bd=10, anchor=W).grid(row=2,
                                                                                                               column=0)

    #Address
    prilbl = Label(leftframe, font=('aria', 16, 'bold'), text="Address", fg="black", bd=10, anchor=W).grid(row=3,
                                                                                                         column=0)

    #Designation
    prilbl = Label(leftframe, font=('aria', 16, 'bold'), text="Designation", fg="black", bd=10, anchor=W).grid(row=4,
                                                                                                           column=0)

    e1 = Entry(root, font=40, bg="pink")
    e1.place(x=250, y=280)
    e2 = Entry(root, font="40", bg="pink")
    e2.place(x=250, y=320)
    e3 = Entry(root, font=40, bg="pink")
    e3.place(x=250, y=360)
    e4 = Entry(root, font=40, bg="pink")
    e4.place(x=250, y=400)


    # ---button--

    # clearbutton
    clearbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Clear", bg="white", fg="red", bd=10, padx=5,
                      pady=5, width=10, command=reset).grid(row=8, column=0)
    # exitbutton
    exitbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Exit", bg="white", fg="black", bd=10, padx=5,
                     pady=5, width=10, command=exit).grid(row=8, column=3)
    # Add  recordbutton
    addbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Add", bg="white", fg="blue", bd=10, padx=5, pady=5,
                    width=10, command=add).grid(row=10, column=0)
    # Deleterecordbutton
    deletebtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Delete Record", bg="white", fg="red", bd=10,
                       padx=5, pady=5, width=10, command=Delete).grid(row=10, column=3)
    # BackButton
    backdbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Back", fg="green", bg="white", bd=10, padx=10,
                    pady=10, width=10,command=back).grid(row=10, column=1, columnspan=2)


    root.mainloop()


system()