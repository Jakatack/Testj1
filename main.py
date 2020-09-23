
from tkinter import *
master = Tk()
master.title("test window")
master.geometry("250x250")  # Width x Height
master.configure(background='gray20')

def test():
    print("test")

def print_box_val():
    var1_val = var1.get()
    var2_val = var2.get()
    if var1_val == True:
        print("var1 value = True")
    else:
        print("var1 value = False")

#buttons
Button(master, text='box_check', command=print_box_val, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=7, column = 1)
Button(master, text='print_test', command=test, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=7, column =0)

# check box
var1 = IntVar()
Checkbutton(master, text='male', bg="gray20", fg="lime green", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', bg="gray20", fg="lime green", variable=var2).grid(row=1, sticky=W)

#Lables with entry boxes
Label(master, text='First Name').grid(row=3)
Label(master, text='Last Name').grid(row=4)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=3, column=1)
e2.grid(row=4, column=1)

master.mainloop()