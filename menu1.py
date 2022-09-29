from tkinter import *
from PIL import ImageTk , Image
from subprocess import call

def exit():
    root.destroy()

def back():
    root.destroy()
    call(['python', "main.py"])

root = Tk()
root.title("Menu-List")
root.geometry("1700x900")

mylabel=Label(root, text="Menu-List",font='Times 35 bold',bg="white").place(x=650,y=0)

canv = Canvas(root, width=400, height=300, bg='white')
canv.place(x=0,y=60)
img = ImageTk.PhotoImage(Image.open("burger.jpg"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)
lbl1=Label(root, text="Burger\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=60,y=370)


canv1 = Canvas(root, width=400, height=300, bg='white')
canv1.place(x=500,y=60)
img1 = ImageTk.PhotoImage(Image.open("pizza.jpg"))  # PIL solution
canv1.create_image(0,0, anchor=NW, image=img1)
lbl2=Label(root, text="Pizza\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=575,y=370)

canv2 = Canvas(root, width=400, height=300, bg='white')
canv2.place(x=1000,y=60)
img2 = ImageTk.PhotoImage(Image.open("french fries.jpg"))  # PIL solution
canv2.create_image(0,0, anchor=NW, image=img2)
lbl3=Label(root, text="French-Fries\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=1075,y=370)

canv3 = Canvas(root, width=400, height=300, bg='white')
canv3.place(x=0,y=440)
img3 = ImageTk.PhotoImage(Image.open("noodles.webp"))  # PIL solution
canv3.create_image(0,0, anchor=NW, image=img3)
lbl4=Label(root, text="Noodles\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=60,y=740)

canv4 = Canvas(root, width=400, height=300, bg='white')
canv4.place(x=500, y=440)
img4 = ImageTk.PhotoImage(Image.open("ice cream.jpg"))  # PIL solution
canv4.create_image(0, 0, anchor=NW, image=img4)
lbl5=Label(root, text="Ice-Cream\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=575,y=740)

canv5 = Canvas(root, width=400, height=300, bg='white')
canv5.place(x=1000, y=440)
img5 = ImageTk.PhotoImage(Image.open("drinks.jpg"))  # PIL solution
canv5.create_image(0, 0, anchor=NW, image=img5)
lbl6=Label(root, text="Drinks\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=1075,y=740)


Button(root, font=('vardana', 16, 'bold'), text="Back", bg="white", fg="blue", bd=10, padx=10,pady=10, width=7, command=back).place(x=0,y=0)
Button(root, font=('vardana', 16, 'bold'), text="Exit", bg="white", fg="red", bd=10, padx=10,pady=10, width=7, command=exit).place(x=1390, y=0)

root.mainloop()