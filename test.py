import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image
import PIL

def exit():
    root.destroy()

def back():
    root.destroy()
    call (['python', "main.py"])

def ok():
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="",database="rms")
    mycursor= mysqldb.cursor()
    e_id=e1.get()
    e_pass=e2.get()

    sql="select * from log_in where id= %s and pass = %s"
    mycursor.execute(sql,[(e_id), (e_pass)])
    results= mycursor.fetchall()
    #results= sql.fetchall()
    if results:

        call(['python',"after_admin_login_pg.py"])
        root.quit()
        return True

    else:
        messagebox.showinfo("","incorrect username and password")
        return False

root=Tk()
root.title(" Admin login")
root.geometry("600x600")
root.configure(bg="pink")

window_width,window_height=600,600

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

mylabel1=Label(root, text="Admin Login",font=200,bg="white")
mylabel1.pack()

global e1
global e2

Label(root,text="Enter Username",font="40").place(x=50,y=120)
Label(root,text="Enter password",font="40").place(x=50,y=200)

e1=Entry(root,font=40)
e1.place(x=280,y=120)

e2=Entry(root,font="40")
e2.place(x=280,y=200)
e2.config(show="*")


Button(root,text="Log in",command=ok,width=10,bg="white",fg="black",font=('vardana',17,'bold'),bd=10, padx=5,pady=5 ).place(x=100,y=300)
Button(root, font=('vardana', 16, 'bold'), text="Back", bg="white", fg="black", bd=10, padx=10,pady=10, width=10, command=back).place(x=310,y=300)
Button(root, font=('vardana', 16, 'bold'), text="Exit", bg="white", fg="black", bd=10, padx=10,pady=10, width=10, command=exit).place(x=230,y=400)

root.mainloop()