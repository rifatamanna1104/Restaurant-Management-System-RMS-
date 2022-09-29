from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from subprocess import call

root = Tk()
root.geometry('950x600')
root.title("Feedback System")
frame_header = ttk.Frame(root)
frame_header.pack(side=TOP)
headerlabel = ttk.Label(frame_header, text='FEEDBACK SYSTEM', foreground='blue',font=('Arial', 24))
headerlabel.grid(row=0, column=1)
messagelabel = ttk.Label(frame_header,text='PLEASE TELL US WHAT YOU THINK',foreground='green', font=('Arial', 10))
messagelabel.grid(row=1, column=1)

frame_content = ttk.Frame(root)
frame_content.pack()

myvar = StringVar()
var = StringVar()

namelabel = ttk.Label(frame_content, text='Name')
namelabel.grid(row=0, column=0, padx=5, sticky='sw')
entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
entry_name.grid(row=1, column=0)

emaillabel = ttk.Label(frame_content, text='Email')
emaillabel.grid(row=0, column=1, sticky='sw')
entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
entry_email.grid(row=1, column=1)

commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 10))
commentlabel.grid(row=2, column=0, sticky='sw')
textcomment = Text(frame_content, width=55, height=10)
textcomment.grid(row=3, column=0, columnspan=2)


textcomment.config(wrap ='word')
def clear():
    textcomment.delete(1.0,'end')
def clear():
    global entry_name
    global entry_email
    global textcomment
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


def submit():
    global entry_name
    global entry_email
    global textcomment
    print('Name:{}'.format(myvar.get()))
    print('Email:{}'.format(var.get()))
    print('Comment:{}'.format(textcomment.get(1.0, END)))
    messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)

def quit():
   root .quit()
   root .destroy()
   exit()

def back():
    root.destroy()
    call(['python', "main.py"])

submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0, sticky='e')
clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')
exitbutton = ttk.Button(frame_content, text='Exit', command=quit).grid(row=4, column=2)
backbutton = ttk.Button(frame_content, text='Back', command=back).grid(row=4, column=0, sticky='w')


# frame1 = Frame(root, width=550, height=450, relief=SUNKEN).pack(side=LEFT)
#
# style = ttk.Style()
# style.theme_use("classic")
# style.configure("Treeview",background="#ffd699",foregroung="black",rowheight=40,rowwidth=50,fieldbackground="white")
# style.map('Treeview',background=[('selected', '#e67f30')])
# ###########  Creating table #############
# my_tree = ttk.Treeview(frame1)
# my_tree['columns'] = ("Name", "Email", "Comments")
#
# hsb = ttk.Scrollbar(frame1, orient="horizontal")
# hsb.configure(command=my_tree.xview)
# my_tree.configure(xscrollcommand=hsb.set)
# hsb.pack(fill=X, side=BOTTOM)
#
# vsb = ttk.Scrollbar(frame1, orient="vertical")
# vsb.configure(command=my_tree.yview)
# my_tree.configure(yscrollcommand=vsb.set)
# vsb.pack(fill=Y, side=RIGHT)
# # defining column for table
# my_tree.column("#0", width=0, minwidth=0)
# my_tree.column("Name", anchor=CENTER, width=80, minwidth=25)
# my_tree.column("Email", anchor=CENTER, width=80, minwidth=25)
# my_tree.column("Comments", anchor=CENTER, width=80, minwidth=25)
#
# # defining  headings for table
# my_tree.heading("Name", text="Name", anchor=CENTER)
# my_tree.heading("Email", text="Email", anchor=CENTER)
# my_tree.heading("Comments", text="Comments", anchor=CENTER)
#
# my_tree.pack()

root.mainloop()