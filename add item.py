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
            "CREATE TABLE IF NOT EXISTS food_list(Itemname,Catagory,Price)")

    # variable datatype assignment
    e1 = StringVar()
    e2 = StringVar()
    e2 = StringVar()

    def reset():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

    def exit():
        root.destroy()

    def back():
        root.destroy()
        call(['python', "test.py"])

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
        conn.execute("SELECT * FROM `food_list`")

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
    my_tree['columns'] = ("Item name", "Catagory", "Price")
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
    my_tree.column("Item name", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("Catagory", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("Price", anchor=CENTER, width=60, minwidth=25)

    # defining  headings for table
    my_tree.heading("Item name", text="Item name", anchor=CENTER)
    my_tree.heading("Catagory", text="Catagory", anchor=CENTER)
    my_tree.heading("Price", text="Price", anchor=CENTER)




    my_tree.pack()
    DisplayData()

    def add():
        Database()

        Itemname = e1.get()
        Catagory = e2.get()
        Price = e3.get()


        if Itemname == "" or Catagory == "" or Price == "" :
            messagebox.showinfo("Warning", "fill the empty field!!!")
        else:

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
            cursor = mysqldb.cursor()
            sql = "INSERT INTO food_list (Itemname, Catagory, Price) VALUES (%s,%s,%s)"
            val = (Itemname, Catagory,Price)
            cursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("Message", "Stored successfully")

        DisplayData()
        conn.close()

    # access data from sqlite
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = conn.execute("SELECT * FROM food_list")
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
            # cursor = conn.execute("DELETE FROM food_list WHERE Price = %s" % selecteditem[2])
            # conn.commit()
            # cursor.close()
            # conn.close()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
            mycursor = mysqldb.cursor()
            sql = "DELETE FROM food_list WHERE Price =" + str(selecteditem[2]) + ""
            mycursor.execute(sql)
            mysqldb.commit()


    localtime = time.asctime(time.localtime(time.time()))

    infolb = Label(topframe, font=('vardana', 30, 'bold'), text="Edit Item", fg="pink", bd=10,
                   anchor=W)
    infolb.grid(row=0, column=0)
    infolb = Label(topframe, font=('varadana', 20,), text=localtime, fg="black", anchor=W)
    infolb.grid(row=1, column=0)

    # items


    Itemlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Item Name", fg="black", bd=10, anchor=W).grid(row=1,
                                                                                                             column=0)
    # Itemtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="pink", justify='right',
    #                ).grid(row=1, column=1)
    # Catagory
    catlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Catagory", fg="black", bd=10, anchor=W).grid(row=2,
                                                                                                               column=0)
    # cattxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="pink", justify='right',
    #               ).grid(row=2, column=1)
    # Price
    prilbl = Label(leftframe, font=('aria', 16, 'bold'), text="Price", fg="black", bd=10, anchor=W).grid(row=3,
                                                                                                         column=0)
    # pritxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="pink", justify='right',
    #                ).grid(row=3, column=1)

    e1 = Entry(root, font=40, bg="pink")

    e1.place(x=250, y=300)
    e2 = Entry(root, font="40", bg="pink")
    e2.place(x=250, y=340)
    e3 = Entry(root, font=40, bg="pink")
    e3.place(x=250, y=380)


    # ---button--

    # clearbutton
    clearbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Clear", bg="white", fg="red", bd=10, padx=5,
                      pady=5, width=10, command=reset).grid(row=8, column=2)
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
    #Button(root, text="Back", command=back, height=2, width=10, font='Times 18 bold', bg="white").place(x=100, y=400)

    # menu
    def menu():
        roott = Tk()
        roott.title("Price Menu")
        roott.geometry("300x400")
        lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="ITEM LIST", fg="black", bd=10)
        lblinfo.grid(row=0, column=0)
        lblprice = Label(roott, font=("Times New Roman", 20, "bold"), text="Prices", fg="black", bd=10)
        lblprice.grid(row=0, column=3)
        lblfries = Label(roott, font=("Times New Roman", 20, "bold"), text=" French Fries", fg="#e67f30", bd=10)
        lblfries.grid(row=1, column=0)
        lblpricef = Label(roott, font=("Times New Roman", 20, "bold"), text="60/-", fg="blue", bd=10)
        lblpricef.grid(row=1, column=3)
        lblpizza = Label(roott, font=("Times New Roman", 20, "bold"), text="Pizza", fg="#e67f30", bd=10)
        lblpizza.grid(row=2, column=0)
        lblpricep = Label(roott, font=("Times New Roman", 20, "bold"), text="220/-", fg="blue", bd=10)
        lblpricep.grid(row=2, column=3)
        lblburger = Label(roott, font=("Times New Roman", 20, "bold"), text="Burger", fg="#e67f30", bd=10)
        lblburger.grid(row=3, column=0)
        lblpriceb = Label(roott, font=("Times New Roman", 20, "bold"), text="120/-", fg="blue", bd=10)
        lblpriceb.grid(row=3, column=3)
        lblnoodles = Label(roott, font=("Times New Roman", 20, "bold"), text="Noodles", fg="#e67f30", bd=10)
        lblnoodles.grid(row=4, column=0)
        lblpricen = Label(roott, font=("Times New Roman", 20, "bold"), text="80/-", fg="blue", bd=10)
        lblpricen.grid(row=4, column=3)
        lblicecream = Label(roott, font=("Times New Roman", 20, "bold"), text="Ice-Cream", fg="#e67f30", bd=10)
        lblicecream.grid(row=5, column=0)
        lblpricei = Label(roott, font=("Times New Roman", 20, "bold"), text="100/-", fg="blue", bd=10)
        lblpricei.grid(row=5, column=3)
        lbldrinks = Label(roott, font=("Times New Roman", 20, "bold"), text="Drinks", fg="#e67f30", bd=10)
        lbldrinks.grid(row=6, column=0)
        lblpriced = Label(roott, font=("Times New Roman", 20, "bold"), text="50/-", fg="blue", bd=10)
        lblpriced.grid(row=6, column=3)
        roott.mainloop()

    # menubutton
    menubtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Menu", bg="white", fg="pink", bd=10, padx=5,
                     pady=5, width=10, command=menu).grid(row=8, column=0)
    root.mainloop()


system()