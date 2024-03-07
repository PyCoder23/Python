from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title("Profit Loss Calculator")
root.geometry("400x170")
root.config(bg = "yellow")

num = tk.StringVar()
ans=tk.StringVar()
n = tk.StringVar()
a = tk.StringVar()
b = tk.StringVar()
op = ""

def Submit(op):
    if op == "":
        messagebox.showerror("No Input", "Choose operation please")
    else:
        ans.set("")
        A = a.get()
        B = b.get()
        try:
            A = int(A)
            B = int(B)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter integars only")
        else:
            print(A)
            print(B)
            ans.set(A)
            ent1.place_forget()
            ent2.place_forget() 
            submit.place_forget()
            Ty.place_forget()
            lab.place_forget()
            if op == 'Cost Price' or op == 'Selling Price':
                Price(op, A, B)
            elif op == 'Profit or Loss' or op == 'Profit or Loss %':
                Pro(op, A, B)

def fin(out, A, B):
    global M
    global N
    
    x.config(text = str(M) + " was " + str(A))
    x.place(x = 110, y = 70, anchor = W)

    y.config(text = str(N) + " was " + str(B))
    y.place(x = 110, y = 115, anchor = W)
    
    z.config(text = out)
    z.place(x = 110, y = 160, anchor = W)
    
def Price(op, A, B):
    if op == 'Cost Price':
        cp = A - B
        cp = round(cp, 3)
        print("Cost Price = "+str(cp))
        out = "Cost Price = "+str(cp)
        
    elif op == 'Selling Price':
        sp = A + B
        sp = round(sp, 3)
        print("Selling Price = "+str(sp))
        out = "Selling Price = "+str(sp)
    fin(out, A, B)
    
def Pro(op, A, B):
    if op == 'Profit or Loss':
        pro = B - A
        pro = round(pro, 3)
        print("Profit = "+str(pro))
        out = "Profit = "+str(pro)
        
    elif op == 'Profit or Loss %':
        per = B - A
        per = (per/A) * 100
        per = round(per, 3)
        print("Profit = " + str(per) + "%")
        out = "Profit = " + str(per) + "%"
    fin(out, A, B)
        
def sel(event):
    op = event.widget.get()
    print(op)
    submit.config(command = lambda : Submit(op))
    lab.place_forget()

    root.geometry("400x200")
    global M
    global N
    global placeholder1
    global placeholder2
    if op == 'Cost Price':
        placeholder1 = 'Enter S.P.'
        placeholder2 = 'Enter Profit or Loss'
        root.geometry("400x220")
        lab.config(text = "Express Gain in +ve and Loss in -ve")
        lab.place(x = 200, y = 195, anchor = CENTER)
        M = "Selling Price"
        N = "Profit/Loss"
        
    elif op == 'Selling Price':
        placeholder1 = 'Enter C.P.'
        root.geometry("400x220")
        placeholder2 = 'Enter Profit or Loss'
        lab.config(text = "Express Gain in +ve and Loss in -ve")
        lab.place(x = 200, y = 195, anchor = CENTER)
        M = "Cost Price"
        N = "Profit/Loss"
        
    elif op == 'Profit or Loss':
        placeholder1 = 'Enter C.P.'
        placeholder2 = 'Enter S.P.'
        M = "Cost Price"
        N = "Selling Price"

    elif op == 'Profit or Loss %':
        placeholder1 = 'Enter C.P.'
        placeholder2 = 'Enter S.P.'
        M = "Cost Price"
        N = "Selling Price"

    ent1.delete(0,'end')
    ent1.insert(0,placeholder1)

    ent2.delete(0,'end')
    ent2.insert(0,placeholder2)
    
    ent1.place(x = 150, y = 115, anchor = CENTER)
    ent2.place(x = 150, y = 155, anchor = CENTER) 
    submit.place(x = 270, y = 135, anchor = CENTER)
    
Title = Label(root, text = "Profit Loss Calculator", fg = "blue2", bg = "yellow", font = ("Comic Sans MS", 18, "bold"))
Title.place(x = 200, y = 25, anchor = CENTER)

Ty = ttk.Combobox(root, width = 20, textvariable = n)
Ty['values'] = ('Cost Price', 
                'Selling Price',
                'Profit or Loss', 
                'Profit or Loss %',)

Ty.place(x = 200, y = 70, anchor = CENTER)
Ty.current()
Ty.set("Select Operation")
Ty.bind("<<ComboboxSelected>>", sel)

ent1 = Entry(root, width = 20, textvariable = a, fg = "black")
ent2 = Entry(root, width = 20, textvariable = b, fg = "black")

lab = Label(root, text = "", fg = "black", bg = "yellow", font = ("Comic Sans MS", 12, "bold"))

global placeholder1
global placeholder2
placeholder1 = 'Please enter side'
def erase_a(event=None):
    if ent1.get() == placeholder1:
        ent1.delete(0,'end')
def add_a(event=None):
    if ent1.get() == '':
        ent1.insert(0,placeholder1)
add_a()
ent1.bind('<FocusIn>',erase_a)
ent1.bind('<FocusOut>',add_a)

placeholder2 = 'Please enter 2nd side'
def erase_b(event=None):
    if ent2.get() == placeholder2:
        ent2.delete(0,'end')
def add_b(event=None):
    if ent2.get() == '':
        ent2.insert(0,placeholder2)
add_b()
ent2.bind('<FocusIn>',erase_b)
ent2.bind('<FocusOut>',add_b)

x = Label(root, text = "", fg = "red", bg = "yellow", font = ("Comic Sans MS", 14, "bold"))
y = Label(root, text = "", fg = "green2", bg = "yellow", font = ("Comic Sans MS", 14, "bold"))
z = Label(root, text = "", fg = "blue", bg = "yellow", font = ("Comic Sans MS", 14, "bold"))

submit = Button(root, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = lambda : Submit(op))
submit.place(x = 200, y = 120, anchor = CENTER)

out = Label(root, textvariable = ans, bg = "yellow", font = ("Comic Sans MS", 12, "bold"))
root.mainloop()