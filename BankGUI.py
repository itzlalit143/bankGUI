from tkinter import *
from tkinter import messagebox
import random

global balance
balance =random.uniform(0.00,100000.00) #random Balance

w1=Tk()
w1.title("Banking System")
w1.geometry("500x300")
w1.config(bg="DeepSkyBlue2")
lblx = Label(w1, text="copyright reserved @Lalit Jarwal", bg="DeepSkyBlue2", fg="white")
lblx.place(x=320, y=280)

def adbal():

    def quit():
        w2.destroy()
    def Add():
        if txtadbal.get()=="":
            messagebox.showerror("Empty","Please enter Amount")
        else:
            global balance
            balance+=int(txtadbal.get())
            txtcb.config(state=NORMAL)
            txtcb.insert(INSERT,('%.2f')%balance)
            txtcb.config(state=DISABLED)
            messagebox.showinfo("Success","Amount added successfully")

    w2 = Tk()
    w2.title("Add Balance")
    w2.geometry("300x300")
    w2.config(bg="DeepSkyBlue2")

    lbladbal = Label(w2, text="Enter Amount:", bg="DeepSkyBlue2", fg="black", font=('arial', 10, 'bold'))
    lbladbal.place(x=20, y=50)

    lblcb = Label(w2, text="Current Balance:", bg="DeepSkyBlue2", fg="black", font=('arial', 10, 'bold'))
    lblcb.place(x=20, y=100)

    txtadbal = Entry(w2, width=20)
    txtadbal.place(x=150, y=50)

    txtcb = Text(w2,width=15,height=1)
    txtcb.config(state=DISABLED)#####
    txtcb.place(x=150, y=100)

    btn1 = Button(w2, text="Add", bg="powder blue", fg="black",command=Add)
    btn1.place(x=150, y=150)
    btn2 = Button(w2, text="Cancel", bg="powder blue", fg="black", command=quit)
    btn2.place(x=230, y=150)

    w2.mainloop()

def wdrl():
    def withdrawal():
        global balance
        if txt1.get()=="":
            messagebox.showerror("Empty","Please enter Amount")
        elif int(txt1.get())>balance:
            messagebox.showerror("Error"," Sorry! You don't have enough balance")
        else:
            balance -= int(txt1.get())
            txtcb.config(state=NORMAL)
            txtcb.insert(INSERT, ('%.2f') % balance)
            txtcb.config(state=DISABLED)
            messagebox.showinfo("Success", "Amount withdrawn successfully")


    def quit():
        w3.destroy()
    w3 = Tk()
    w3.title("Withdrawal")
    w3.geometry("300x300")
    w3.config(bg="DeepSkyBlue2")

    lbl1 = Label(w3, text="Enter Amount:", bg="DeepSkyBlue2", fg="black", font=('arial', 10, 'bold'))
    lbl1.place(x=20, y=50)

    lblcb = Label(w3, text="Current Balance:", bg="DeepSkyBlue2", fg="black", font=('arial', 10, 'bold'))
    lblcb.place(x=20, y=100)

    txt1 = Entry(w3, width=20)
    txt1.place(x=150, y=50)

    txtcb = Text(w3, width=15, height=1)
    txtcb.config(state=DISABLED)
    txtcb.place(x=150, y=100)

    btn1 = Button(w3, text="Withdrawal", bg="powder blue", fg="black", command=withdrawal)
    btn1.place(x=150, y=150)
    btn2 = Button(w3, text="Cancel", bg="powder blue", fg="black", command=quit)
    btn2.place(x=230, y=150)

    w3.mainloop()

def showbal():

    def quit():
        w4.destroy()
    w4 = Tk()
    w4.title("Current Balance")
    w4.geometry("300x300")
    w4.config(bg="DeepSkyBlue2")

    lblcb = Label(w4, text="Current Balance:", bg="DeepSkyBlue2", fg="black", font=('arial', 10, 'bold'))
    lblcb.place(x=20, y=100)

    txtcb = Text(w4, width=15, height=1)
    txtcb.place(x=150, y=100)
    txtcb.insert(INSERT, ('%.2f') % balance)
    txtcb.config(state=DISABLED)
    btn2 = Button(w4, text="Cancel", bg="powder blue", fg="black", command=quit)
    btn2.place(x=230, y=150)

    w4.mainloop()


def Exit(): #main exit
    exit(messagebox.showinfo("Bye","See You Soon"))

lblttl=Label(w1,text="Welcome!! to Banking System",bg="cyan",fg="black",font=('arial',15,'bold'))
lblttl.place(x=120,y=10)

lbladbal=Label(w1,text="Add Balance:",bg="DeepSkyBlue2",fg="black",font=('arial',13,'bold'))
lbladbal.place(x=50,y=60)

lblwdrl=Label(w1,text="Withdrawal:",bg="DeepSkyBlue2",fg="black",font=('arial',13,'bold'))
lblwdrl.place(x=50,y=110)

lblcb=Label(w1,text="Check Balance:",bg="DeepSkyBlue2",fg="black",font=('arial',13,'bold'))
lblcb.place(x=50,y=160)

lblext=Label(w1,text="Exit:",bg="DeepSkyBlue2",fg="black",font=('arial',13,'bold'))
lblext.place(x=50,y=210)

btn1=Button(w1,text="Click",bg="powder blue",fg="black",command=adbal)
btn1.place(x=200,y=60)

btn2=Button(w1,text="Click",bg="powder blue",fg="black",command=wdrl)
btn2.place(x=200,y=110)

btn3=Button(w1,text="Click",bg="powder blue",fg="black",command=showbal)
btn3.place(x=200,y=160)

btn4=Button(w1,text="Click",bg="powder blue",fg="black",command=Exit)
btn4.place(x=200,y=210)

w1.mainloop()
