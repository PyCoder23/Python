from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mayank@ATL",
    database="cred",
    charset="utf8")

mycursor = mydb.cursor() 
root = tk.Tk()
root.title("Login system")
root.geometry("350x250")
root.config(bg = "cyan")
root.resizable(False, False)

email =tk.StringVar()
pas =tk.StringVar()
cap =tk.StringVar()

cred = {"ABC" : "123"}

CAP = ""

def captcha():
    global CAP
    import random
    import array
    MAX_LEN = 7
     
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
     
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
     
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '>',
               '*', '(', ')', '<']
     
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
     
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
     
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        
    CAP = temp_pass
                 
def ried():
    print("Success")
    label.config(text = "Login sucessful!")
    cap_ca.config(text = "7777777")

def wred():
    print("Fail")
    messagebox.showerror("Wrong Credentials", "Invalid Username or Password")
    captcha()
    cap_ca.config(text = CAP)
    
def Sub():
    fail = 0
    Email = email.get()
    Pass = pas.get()
    Cap = cap.get()
    email.set("")
    pas.set("")
    cap.set("")
    print(Email)
    print(Pass)
    print(Cap)
    
    if Cap != CAP:
        messagebox.showerror("Wrong Verfication", "Invalid Captcha")
        captcha()
        cap_ca.config(text = CAP)

    if Cap == CAP:
        query = """SELECT count(*) FROM CREDENTIALS where EMAIL = %s"""
        mycursor.execute(query, (Email,))
        myresult = mycursor.fetchone()
        print(myresult[0])
        if int(myresult[0]) == 0:
            wred()
        else:
            query = """SELECT PASSWORD FROM CREDENTIALS where EMAIL = %s"""
            mycursor.execute(query, (Email,))

            myresult = mycursor.fetchall()
            for row in myresult:
                print("Password  = ", row[0], "\n")
                if row[0] == Pass:
                    ried()
                else:
                    wred()

    print("")

captcha()
lab_em = Label(root, text = "Email", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_em.place(x = 20, y = 60, anchor = W)
ent_em = Entry(root, textvariable = email, width = 25, font = ("Comic Sans MS", 10, "bold"))
ent_em.place(x = 125, y = 60, anchor = W)

lab_pa = Label(root, text = "Password", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_pa.place(x = 20, y = 100, anchor = W)
ent_pa = Entry(root, textvariable = pas, width = 25, font = ("Comic Sans MS", 10, "bold"))
ent_pa.place(x = 125, y = 100, anchor = W)

lab_ca = Label(root, text = "Captcha", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
lab_ca.place(x = 20, y = 140, anchor = W)
cap_ca = Label(root, text = CAP, bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
cap_ca.place(x = 125, y = 140, anchor = W)
ent_ca = Entry(root, textvariable = cap, width = 8, font = ("Comic Sans MS", 10, "bold"))
ent_ca.place(x = 328, y = 140, anchor = E)

label = Label(root, text = "", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
label.place(x = 120, y = 200, anchor = CENTER)

submit = Button(root, text = "Submit", fg = "white", bg = "blue", font = ("Comic Sans MS", 13, "bold"), command = Sub)
submit.place(x = 270, y = 200, anchor = CENTER) 
root.mainloop()