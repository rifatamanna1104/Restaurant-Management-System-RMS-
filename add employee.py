#add employee code
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def system():
    root = Tk()
    root.geometry("900x650")
    root.title("Add Employee")

    eml_Name = StringVar()
    con = StringVar()
    addr = StringVar()
    desg = StringVar()
    passw = StringVar()

    def clear():
        eml_Name.set('')
        con.set('')
        addr.set('')
        desg.set('')
        passw.set('')

    def add():
        messagebox.showinfo('ADD_PAGE','ADDED')

    def exit():
        root.destroy()

    topframe = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
    topframe.pack(side=TOP)
    leftframe = Frame(root, width=900, height=700, relief=SUNKEN)
    leftframe.pack(side=LEFT)
    rightframe = Frame(root, width=400, height=700, relief=SUNKEN)
    rightframe.pack(side=RIGHT)

    style = ttk.Style()
    style.theme_use("classic")
    style.configure("Treeview",background="#ffd699",foregroung="black",rowheight=30,fieldbackground="white")
    style.map('Treeview',background=[('selected', '#e67f30')])

    infolb = Label(topframe, font=('vardana', 30, 'bold'), text="ADD EMPLOYEE", fg="pink", bd=10,anchor=W)
    infolb.grid(row=0, column=0)

    eml_Name = Label(leftframe, font=('aria', 16, 'bold'), text="Employee Name:", fg="black", bd=10, anchor=W).grid(row=1,
                                                                                                             column=0)
    eml_Name = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="pink", justify='right',
                   textvariable=eml_Name).grid(row=1, column=1)

    con = Label(leftframe, font=('aria', 16, 'bold'), text="Contact Number:", fg="black", bd=10, anchor=W).grid(row=2,
                                                                                                               column=0)
    con = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="pink", justify='right',
                  textvariable=con).grid(row=2, column=1)

    addr = Label(leftframe, font=('aria', 16, 'bold'), text="Address:", fg="black", bd=10, anchor=W).grid(row=3,
                                                                                                         column=0)
    addr = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="pink", justify='right',
                   textvariable=addr).grid(row=3, column=1)

    desg = Label(leftframe, font=('aria', 16, 'bold'), text="Designation:", fg="black", bd=10, anchor=W).grid(row=4,
                                                                                                         column=0)
    desg = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="pink", justify='right',
                  textvariable=desg).grid(row=4, column=1)

    passw = Label(leftframe, font=('aria', 16, 'bold'), text="Pasword:", fg="black", bd=10, anchor=W).grid(row=5,
                                                                                                         column=0)
    passw = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="pink", justify='right',
                  textvariable=passw).grid(row=5, column=1)

    addbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="ADD", bg="white", fg="blue", bd=10, padx=5, pady=5,
                    width=10,command=add).grid(row=10, column=0)

    clearbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="CLEAR", bg="white", fg="red", bd=10, padx=5,
                      pady=5, width=10, command=clear).grid(row=10, column=2)

    exitbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Exit", bg="white", fg="black", bd=10, padx=5,
                     pady=5, width=10, command=exit).grid(row=10, column=3)
    root.mainloop()
system()