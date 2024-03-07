from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x200")
root.config(bg = "yellow")

n = tk.StringVar()
Cur = tk.StringVar()
Pa = tk.StringVar()
Ri = tk.StringVar()
Ti = tk.StringVar()
Cr = tk.StringVar()
ANS = tk.StringVar()
ans = tk.StringVar()

def sel(event):
    global ty
    ty = event.widget.get()
    
def Submit(ty):
    cur = Cur.get()
    if cur == "Please enter Currency":
        messagebox.showerror("No currency entered", "Please enter transaction currency")
    else:
        print("\nCurrency is " + str(cur))
        print(ty)
        Title.config(text = ty + " Calculator")
        Ty.place_forget()
        label_1.config(textvariable = ans)
        ans.set("Enter principal amount")
        submit.config(command = lambda : get_pa(ty, cur))
        entry.place_forget()
        entry_2.place(x = 140, y = 115, anchor = CENTER)
        entry_2.config(textvariable = Pa)
        submit.place(x = 260, y = 115, anchor = CENTER)

def get_pa(ty, cur):
    P = Pa.get()
    try:
        P = float(P)
    except ValueError:
        messagebox.showerror("Invalid Input!", "Enter numerical value only")
    else:        
        ans.set("Enter Rate of Interest")
        submit.config(command = lambda : get_ri(ty, cur, P))
        entry_2.place(x = 140, y = 115, anchor = CENTER)
        entry_2.config(textvariable = Ri)
        submit.place(x = 260, y = 115, anchor = CENTER)

def get_ri(ty, cur, P):
    R = Ri.get()
    try:
        R = float(R)
    except ValueError:
        messagebox.showerror("Invalid Input!", "Enter numerical value only")
    else:
        ans.set("Enter Time(in years)")
        submit.config(command = lambda : get_ti(ty, cur, P, R))
        entry_2.place(x = 140, y = 115, anchor = CENTER)
        entry_2.config(textvariable = Ti)
        submit.place(x = 260, y = 115, anchor = CENTER)

def get_ti(ty, cur, P, R):
    T = Ti.get()
    try:
        T = float(T)
    except ValueError:
        messagebox.showerror("Invalid Input!", "Enter numerical value only")
    else:
        if ty == "Compound Interest":
            ans.set("Enter Compound Freq. per year")
            submit.config(command = lambda : get_cr(ty, cur, P, R, T))
            entry_2.place(x = 140, y = 115, anchor = CENTER)
            entry_2.config(textvariable = Cr)
            submit.place(x = 260, y = 115, anchor = CENTER)
        else:
            si(ty, cur, P, R, T)

def get_cr(ty, cur, P, R, T):
    N = Cr.get()
    try:
        N = float(N)
    except ValueError:
        messagebox.showerror("Invalid Input!", "Enter numerical value only")
    else:
        ci(ty, cur, P, R, T, N)

def si(ty, cur, P, R, T):
    submit.place_forget()
    entry.place_forget()
    entry_2.place_forget()
    label_1.config(textvariable = ans)
    label_1.config(font = ("Comic Sans MS", 12, "bold"))
    label_1.place(x = 200, y = 80, anchor = CENTER)
    label_2.place(x = 200, y = 110, anchor = CENTER)
    SI = (P * R * T)/100
    SI = round(SI, 2)
    ans.set("Simple Interest = "+cur+str(SI))
    ANS.set("Amount = "+cur+str(round(SI+P, 2)))
    ret.place(x = 200, y = 160, anchor = CENTER)

def ci(ty, cur, P, R, T, N):
    submit.place_forget()
    entry.place_forget()
    entry_2.place_forget()
    label_1.config(textvariable = ans)
    label_1.config(font = ("Comic Sans MS", 12, "bold"))
    label_1.place(x = 200, y = 80, anchor = CENTER)
    label_2.place(x = 200, y = 110, anchor = CENTER)
    CI = P * ((1+(R)/(100*N))**(N*T))
    CI -= P
    CI = round(CI, 2)
    ans.set("Compound Interest = "+cur+str(CI))
    ANS.set("Amount = "+cur+str(round(CI+P, 2)))
    ret.place(x = 200, y = 160, anchor = CENTER)
    

def again():
    n.set("")
    Cur.set("")
    Pa.set("")
    Ri.set("")
    Ti.set("")
    Cr.set("")
    ANS.set("")
    ans.set("")
    
    ret.place_forget()
    label_1.config(font = ("Comic Sans MS", 15, "bold"))
    label_2.place_forget()
    placeholder = 'Please enter Currency'

    entry.place(x = 140, y = 155, anchor = CENTER)

    def erase(event=None):
        if entry.get() == placeholder:
            entry.delete(0,'end')
    def add(event=None):
        if entry.get() == '':
            entry.insert(0,placeholder)

    add()
    entry.bind('<FocusIn>',erase)
    entry.bind('<FocusOut>',add)

    ans.set("Select Interest")
    label_1.place(x = 200, y = 70, anchor = CENTER)

    Ty.place(x = 200, y = 110, anchor = CENTER)

    submit.config(command = lambda : Submit(ty))
    submit.place(x = 260, y = 155, anchor = CENTER)

Title = Label(root, text = "Interest Calculator", fg = "red", bg = "yellow", font = ("Comic Sans MS", 18, "bold"))
Title.place(x = 200, y = 30, anchor = CENTER)

placeholder = 'Please enter Currency'

entry = Entry(root, width = 20, textvariable = Cur)
entry_2 = Entry(root, width = 20, text = "")
entry.place(x = 140, y = 155, anchor = CENTER)

def erase(event=None):
    if entry.get() == placeholder:
        entry.delete(0,'end')
def add(event=None):
    if entry.get() == '':
        entry.insert(0,placeholder)

add()
entry.bind('<FocusIn>',erase)
entry.bind('<FocusOut>',add)

label_1 = Label(root, text = "Select Interest", fg = "blue", bg = "yellow", font = ("Comic Sans MS", 15, "bold"))
label_1.place(x = 200, y = 70, anchor = CENTER)

label_2 = Label(root, textvariable = ANS, fg = "blue", bg = "yellow", font = ("Comic Sans MS", 12, "bold"))

Ty = ttk.Combobox(root, width = 20, textvariable = n)
Ty['values'] = ('Simple Interest', 
                'Compound Interest')

Ty.place(x = 200, y = 110, anchor = CENTER)
Ty.current()
Ty.bind("<<ComboboxSelected>>", sel)

submit = Button(root, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = lambda : Submit(ty))
submit.place(x = 260, y = 155, anchor = CENTER)

ret = Button(root, text = "Use again", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = again)

