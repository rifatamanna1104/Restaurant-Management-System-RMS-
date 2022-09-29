from tkinter import *
from subprocess import call
from tkinter import messagebox
from tkinter.font import BOLD

from PIL import ImageTk, Image
win = Tk()
win.title("Admin Mood")
win.configure(bg="#FFE6E8")
win.geometry('650x600')
canv = Canvas(win, width=650, height=600, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("resta-back.jpg"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(win, text="Admin-Mood",font='Times 35 bold',bg="white").place(x=175,y=10)

#Exit action
def quit():
   win.quit()
   win.destroy()
   exit()

def ok():
   if ok:
      call(['python', "add item.py"])
      win.quit()
      return True

def ok1():
   if ok1:
      call(['python', "edit_employee.py"])
      win.quit()
      return True

def ok2():
   if ok2:
      call(['python', "feed.py"])
      win.quit()
      return True

def back():
    win.destroy()
    call(['python', "test.py"])

Button(win, text="Edit Item", command=ok, height=2, width=15, font='Times 18 bold', bg="white").place(x=50, y=100)
Button(win, text="Edit Employee", command=ok1, height=2, width=15, font='Times 18 bold', bg="white").place(x=300, y=100)
Button(win, text="Feedback", command=ok2, height=2, width=15, font='Times 18 bold', bg="white").place(x=200,y=250)
Button(win, text="Back", command=back, height=2, width=10, font='Times 18 bold', bg="white").place(x=100,y=400)
Button(win, font='Time 18 bold', text="Exit", bg="white", width=10,height=2, command=quit).place(x=300,y=400)
# #Create Menu Bar
# menuBar=Menu(win)
# win.config(menu=menuBar)
#
# #File Menu
# fileMenu= Menu(menuBar, tearoff=0)
# fileMenu.add_command(label="Edit Item",command=ok)
# fileMenu.add_separator()
# fileMenu.add_command(label="Edit Employee",command=ok1)
# menuBar.add_cascade(label="Edit", menu=fileMenu)
#
# #Help Menu
# helpMenu= Menu(menuBar, tearoff=0)
# menuBar.add_cascade(label="Feedback", menu=helpMenu,command=ok2)
# menuBar.add_command(label="Exit", command=_quit)

#Calling Main()
win.mainloop()