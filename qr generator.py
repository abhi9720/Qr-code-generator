from tkinter import *
import pyqrcode
from tkinter import messagebox
import png
import os
root = Tk()
root.title("QR code generator")
root.config(bg="#0df3da")  # 006A4E
root.resizable(0, 0)
root.geometry("700x500+400+60")
global myqr

def generate():
    if len(subject.get()) != 0:
        global myqr
        myqr = pyqrcode.create(subject.get())
# print(myqr.text())
        # print(myqr.terminal())

        # 1 xbm file format is simple black and white image formate
        qrImage = myqr.xbm(scale=5 )
        # xbm natively supported by tkinter

        global photo
        # make generate the bitmap image from the rendered code
        photo = BitmapImage(data=qrImage)

    else:
        messagebox.showinfo("Error", "please enter the subject".title())
    try:
        showcode()
    except:
        pass

# code showing


def showcode():
    global photo
    global sublabel
    sublabel = Label(root, text="Showing QR code for :" +subject.get(), bg="#0df3da", font=("times new roman ", 12))
    sublabel.place(x=200, y=180)

    global notificationLabel
    notificationLabel = Label(root, image=photo, bg="#0df3da")
    notificationLabel.place(x=250, y=220)

def save():

    path1 = os.getcwd()+"\\QR code"
    if not os.path.exists(path1):
        os.makedirs(path1)
    # try:
    global myqr
    if len(name.get()) != 0:
        x = messagebox.askquestion("Save", 'Do you want to save')
        if x == 'yes':
            # print(myqr, type(myqr))
            myqr.png(path1+'\\'+name.get()+".png")
    else:
        messagebox.showinfo("Error", "file name can not be empty".title())
        reset()
    # except():
    #     messagebox.showinfo("Error", "please generate the code first".title())
    #     reset()


qr = Frame(root, bg='#106bbb', height=16, bd=3,)
qr.place(x=0, y=0, relwidth=1, height=50)                      # #218492
title = Label(qr, text="QR CODE GENERATOR ", font=(
    "Helvetica", 20, "bold", "bold"), bg='#106bbb', fg='black',)
title.place(x=10, y=2)
qr = Frame(root, bg='red', height=16, bd=3,)
qr.place(x=0, y=55, relwidth=1, height=1)

lab1 = Label(root, text="Enter Subject ", bg="#0df3da", font=(
    "Helvetica", 15, "bold", "italic"), fg='black')
lab1.place(x=90, y=80)
lab2 = Label(root, text="Enter File Name", bg="#0df3da", font=(
    "Helvetica", 15, "bold", "italic",), fg='black')
lab2.place(x=82, y=140)
name = StringVar()
name1 = Entry(root, textvariable=name, border=6,
              bg="light gray", font=("Helvetica"))
subject = StringVar()

subject1 = Entry(root, textvariable=subject, border=6,
                 bg="light gray", font=("Helvetica"))
subject1.focus()
name1.place(x=250, y=140)
subject1.place(x=250, y=80)


def exitwindow():
    root.destroy()


def reset():
    global photo
    global sublabel
    
    name1.delete(0, 'end')
    subject1.delete(0, 'end')
    photo = ""
    sublabel.destroy()

   

    global notificationLabel
    notificationLabel = Label(root, image=photo, bg="#1974D2")
    notificationLabel.place(x=250, y=220)


qrbutton = Button(root, text="create Qr code", cursor='hand2', activebackground='green',
                  border=5, command=generate, fg="red", bg="black", font=("times new roman ", 12))
qrbutton.place(x=530, y=80)

pngbutton = Button(root, text="  Save as PNG ", border=5, activebackground='green',
                   cursor='hand2', fg="red", bg="black", command=save, font=("times new roman ", 12))
pngbutton.place(x=530, y=140)
exit1 = Button(root,width=5, text="Exit", border=0, underline=1, fg="red", cursor='hand2',
               activebackground='green', bg="black", command=exitwindow, font=("times new roman ", 16))
exit1.place(x=600, y=440)
reset1 = Button(root, text="Reset", border=0, fg="red", bg="black", activeforeground='khaki',
                activebackground='green', cursor='hand2', command=reset, font=("times new roman ", 16))
reset1.place(x=500, y=440)
logo = Label(root, text=" @abhishek_tiwari ", bg="#0df3da",fg="red", font=("times new roman ", 14))
logo.place(x=250, y=450)

root.mainloop()
