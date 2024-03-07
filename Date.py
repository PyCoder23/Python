from tkinter import *
from tkinter import ttk
import tkinter as tk

from datetime import date
from tkcalendar import Calendar
from tkinter import messagebox

root = tk.Tk()
root.title("Date Finder")
root.geometry("350x250")
root.config(bg = "cyan")
ds = tk.StringVar()
n = tk.StringVar()
curdate = date.today()
curdate = str(curdate)

global DOB
DOB = ""

global COB
COB = ""

def Submit():
    global DOB
    days = ds.get()
    if DOB != "":
        if days != "":
            div(DOB)
            global curdate
            try:
                days = int(days)
            except ValueError:
                messagebox.showerror("Invalid Interval days Input!", "Please enter interval of days as natural numbers only!")
            else:
                global COB
                print("Origin Date is => "+str(DOB))
                print("Interval days are => "+str(days))
                print("Date finded is => "+str(COB))
                print("")
        else:
            messagebox.showerror("No Interval days Input!", "Please enter Interval days")
    else:
        messagebox.showerror("No Date Input!", "Please select origin date")
    
def label_clicked(event):
    global z
    cal.place(x= 175, y=140, anchor = CENTER)
    sub_dob.place(x = 195, y = 60, anchor = CENTER)
    lab2.place_forget()
    ent1.place_forget()
    sub.place_forget()
    z = 1

def dob_clicked(event):
    global DOB
    global z
    DOB = cal.get_date()
    date.config(text = DOB)
    lab2.place(x= 175, y=120, anchor = CENTER)
    ent1.place(x = 175, y = 153, anchor = CENTER)
    sub.place(x=175, y=207, anchor = CENTER)
    cal.place_forget()
    sub_dob.place_forget()
    z = 2

def div(DOB):
    global y
    global mn
    global dy
    if len(str(DOB)) == 8:
        mn = ""
        for i in range(0, 2):
            mn += curdate[i]
        mn = int(mn)
        print(mn)

        dy = ""
        for i in range(3, 5):
            dy += curdate[i]
        dy = int(dy)
        print(dy)

        y = ""
        for i in range(6, 8):
            y += curdate[i]
        y = int(y)
        print(y)
        
    else:
        mn = ""
        for i in range(0, 1):
            mn += curdate[i]
        mn = int(mn)
        print(mn)

        dy = ""
        for i in range(2, 4):
            dy += curdate[i]
        dy = int(dy)
        print(dy)

        y = ""
        for i in range(5, 7):
            y += curdate[i]
        y = int(y)
        print(y)

y = ""
for i in range(0, 4):
    y += curdate[i]
y = int(y)
print(y)

mn = ""
for i in range(5, 7):
    mn += curdate[i]
mn = int(mn)
print(mn)

dy = ""
for i in range(8, 10):
    dy += curdate[i]
dy = int(dy)
print(dy)
print("")

Title = Label(root, text = "Date Finder", fg = 'blue2', bg = 'cyan' , font = ('Comic Sans MS', 19, 'bold'))
Title.place(x=175, y=25, anchor = CENTER)

lab1 = Label(root, text = "Origin Date", fg = 'blue2', bg = 'cyan' , font = ('Comic Sans MS', 12, 'bold'))
lab1.place(x=175, y=65, anchor = CENTER)

date = Label(root, text = " Click to Select date ", fg = "white", bg = "blue", font = ("Comic Sans MS", 12, "bold"))
date.place(x = 175, y = 95, anchor = CENTER)
date.bind("<Button-1>", label_clicked)
cal = Calendar(root, selectmode = 'day', year = y, month = mn, day = dy)
sub_dob = Label(root, text = "Submit", fg = "white", bg = "blue", font = ("Comic Sans MS", 8, "bold"))
sub_dob.bind("<Button-1>", dob_clicked)
             
lab2 = Label(root, text = "Interval in the Dates", fg = 'blue2', bg = 'cyan' , font = ('Comic Sans MS', 12, 'bold'))
lab2.place(x=175, y=125, anchor = CENTER)

ent1 = Entry(root, textvariable = ds, font = ('Comic Sans MS', 10, 'bold'))
ent1.place(x=175, y=158, anchor = CENTER)

sub = Button(root, text = "Submit", fg = 'white', bg = 'blue3', font = ('Comic Sans MS', 12, 'bold'), command = Submit)
sub.place(x=175, y=207, anchor = CENTER)
root.mainloop()
