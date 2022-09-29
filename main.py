from tkinter import *
from subprocess import call
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import ImageTk, Image
import Image
import PIL

win = Tk()
win.title("Restuarent Management System")
win.configure(bg="#F0FFF0")
win.geometry('900x675')
canv = Canvas(win, width=900, height=675, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("rbg.webp"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(win, text="Welcome To Our Restaurent",font='Times 35 bold',bg="white").place(x=175,y=10)

#Exit action
# def quit():
#    win.quit()
#    win.destroy()
#    exit()


def quit():
   response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
   if response:
      win.destroy()


   else:
      messagebox.showinfo("SYSTEM ALERT", "Canceled")

def ok():
   if ok:
      call(['python', "test.py"])
      win.quit()
      return True

def ok1():
   if ok1:
      call(['python', "prac.py"])
      win.quit()
      return True

def ok2():
   if ok2:
      call(['python', "menu1.py"])
      win.quit()
      return True


def ok3():
   if ok3:
      call(['python', "feed.py"])
      win.quit()
      return True

Button(win, text="Admin log in", command=ok, height=2, width=15, font='Times 18 bold', bg="white").place(x=100, y=100)
Button(win, text="Employee log in", command=ok1, height=2, width=15, font='Times 18 bold', bg="white").place(x=100, y=200)
Button(win, text="Menu", command=ok2, height=2, width=10, font='Times 18 bold', bg="white").place(x=600, y=300)
Button(win, text="Feedback", command=ok3, height=2, width=10, font='Times 18 bold', bg="white").place(x=600,y=400)
Button(win, text="Exit", command=quit, height=2, width=10, font='Times 18 bold', bg="white").place(x=600,y=500)


# #Create Menu Bar
# menuBar=Menu(win)
# win.config(menu=menuBar)
#
# #File Menu
# fileMenu= Menu(menuBar, tearoff=0)
# fileMenu.add_command(label="Admin Login",command=ok)
# fileMenu.add_separator()
# fileMenu.add_command(label="Employee Login",command=ok1)
# menuBar.add_cascade(label="Log In", menu=fileMenu)
#
# #Help Menu
# helpMenu= Menu(menuBar, tearoff=0)
# menuBar.add_cascade(label="Feedback", menu=helpMenu,command=ok2)
# menuBar.add_command(label="Menu", command=ok3)
# menuBar.add_command(label="Exit", command=_quit)

#Calling Main()
win.mainloop()