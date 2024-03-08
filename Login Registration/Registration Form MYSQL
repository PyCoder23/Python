from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar

import tkinter as tk
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="USERNAME",
    password="PASSWORD",
    database="DATABASE_NAME",
    charset="utf8")

root = tk.Tk()
root.title("Registration Form")
root.geometry("350x450")
root.config(bg = "cyan")
root.resizable(False, False)

name =tk.StringVar()
email =tk.StringVar()
pas =tk.StringVar()
repas =tk.StringVar()

coun =tk.StringVar()
hob =tk.StringVar()
city =tk.StringVar()

global z
z = 0
global y
y = 0

def struD(DOB):
    dob = ""
    for i in range(0, len(DOB)):
        if DOB[i] == "/":
            dob += "-"
        else:
            dob += DOB[i]
    return dob

def Submit():
    global DOB
    DOB = struD(DOB)

    global z
    global y
    if z != 2:
        messagebox.showerror("No DOB!", "You have not entered Date of Birth")
    else:  
        Name = name.get()
        g = v.get()
        Email = email.get()
        Pass = pas.get()
        Repass = repas.get()
        if Pass != Repass :
            messagebox.showerror("Invalid Match!", "Your password does not match with confirm password")
        Coun = coun.get()
        Hob = hob.get()
        City = city.get()
        if g == 1:
            Gen = "Male"
        elif g == 2:
            Gen = "Female"
        else:
            messagebox.showerror("No Gender selected!", "You have not selected Gender")
        if g == 1 or g == 2:
            if Pass == Repass :
                mycursor = mydb.cursor() 
                sql = "INSERT INTO CREDENTIALS (Name, Email, Password, Gender, Dob, Hobby, Country, City)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (Name, Email, Pass, Gen, DOB, Hob, Coun, City)
                   
                mycursor.execute(sql, val)
                mydb.commit()

                name.set("")
                email.set("")
                pas.set("")
                repas.set("")
                coun.set("")
                hob.set("")
                city.set("")
                date.config(text = " Click to Select DOB ")
                status.config(text = "Registration Successful!")
                
                print(Name)
                print(Gen)
                print(Email)
                print(Pass)
                print(Repass)
                print(DOB)
                print(Coun)
                print(Hob)
                print(City)
                print("")
    
    
def label_clicked(event):
    global z
    cal.place(x= 225, y=240, anchor = CENTER)
    sub_dob.place(x = 246, y = 160, anchor = CENTER)
    ent_nat.place_forget()
    ent_sta.place_forget()
    z = 1

def dob_clicked(event):
    global DOB
    global z
    DOB = cal.get_date()
    date.config(text = DOB)
    ent_nat.place(x= 125, y=280, anchor = W)
    ent_sta.place(x = 125, y = 320, anchor = W)
    cal.place_forget()
    sub_dob.place_forget()
    z = 2

lab_na = Label(root, text = "Name", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_na.place(x = 20, y = 40, anchor = W)
ent_na = Entry(root, textvariable = name, width = 25, font = ("Comic Sans MS", 10, "bold"))
ent_na.place(x = 125, y = 40, anchor = W)

lab_gen = Label(root, text = "Gender", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_gen.place(x = 20, y = 80, anchor = W)
v = tk.IntVar()
M = tk.Radiobutton(root, bg = "cyan", text="Male", font = ("Comic Sans MS", 12, "bold"), variable=v, value=1)
M.place(x= 170, y=80, anchor = CENTER)
F = tk.Radiobutton(root, bg = "cyan", text="Female", font = ("Comic Sans MS", 12, "bold"), variable=v, value=2)
F.place(x= 270, y=80, anchor = CENTER)

lab_em = Label(root, text = "Email", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_em.place(x = 20, y = 120, anchor = W)
ent_em = Entry(root, textvariable = email, width = 25, font = ("Comic Sans MS", 10, "bold"))
ent_em.place(x = 125, y = 120, anchor = W)

lab_pa = Label(root, text = "Password", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_pa.place(x = 20, y = 160, anchor = W)
ent_pa = Entry(root, textvariable = pas, width = 25, font = ("Comic Sans MS", 10, "bold"))
ent_pa.place(x = 125, y = 160, anchor = W)

lab_rep_pa = Label(root, text = "Confirm", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_rep_pa.place(x = 20, y = 200, anchor = W)
ent_pa = Entry(root, textvariable = repas, width = 25, font = ("Comic Sans MS", 10, "bold"))
ent_pa.place(x = 125, y = 200, anchor = W)

lab_dob = Label(root, text = "DOB", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_dob.place(x = 20, y = 240, anchor = W) 

date = Label(root, text = " Click to Select DOB ", fg = "white", bg = "blue", font = ("Comic Sans MS", 12, "bold"))
date.place(x = 225, y = 240, anchor = CENTER)
date.bind("<Button-1>", label_clicked)
cal = Calendar(root, selectmode = 'day', year = 2020, month = 5, day = 22)
sub_dob = Label(root, text = "Submit", fg = "white", bg = "blue", font = ("Comic Sans MS", 8, "bold"))
sub_dob.bind("<Button-1>", dob_clicked)

lab_nat = Label(root, text = "Hobby", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_nat.place(x = 20, y = 280, anchor = W)
ent_nat = Entry(root, textvariable = hob, width = 25, font = ("Comic Sans MS", 10, "bold"))
ent_nat.place(x = 125, y = 280, anchor = W)

lab_sta = Label(root, text = "Country", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_sta.place(x = 20, y = 320, anchor = W)
ent_sta = Entry(root, textvariable = coun, width = 25, font = ("Comic Sans MS", 10, "bold"))
ent_sta.place(x = 125, y = 320, anchor = W)

lab_cit = Label(root, text = "City", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_cit.place(x = 20, y = 360, anchor = W)
ent_cit = Entry(root, textvariable = city, width = 25, font = ("Comic Sans MS", 10, "bold"))
ent_cit.place(x = 125, y = 360, anchor = W)

submit = Button(root, text = "Submit", fg = "white", bg = "blue", font = ("Comic Sans MS", 13, "bold"), command = Submit)
submit.place(x = 270, y = 410, anchor = CENTER)

status = Label(root, text = "", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
status.place(x = 110, y = 410, anchor = CENTER)
root.mainloop()
