from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import math
import time

root = tk.Tk()
root.title("Geometry")
root.geometry("400x200")
root.config(bg = "cyan")

Ans = tk.StringVar()
n = tk.StringVar()
m = tk.StringVar()

a = tk.StringVar()
b = tk.StringVar()
c = tk.StringVar()

ans = 0
peri = 0
area = 0
def r():
    print("")
    ans = 0
    peri = 0
    area = 0
    A = 0
    B = 0
    C = 0
    n.set("")
    m.set("")
    a.set("")
    b.set("")
    c.set("")
    Ans.set("")
    opt.config(text = "Unit is cm")
    dis.config(text = "")
    submit.config(command = lambda : Submit(ty, sh))
    root.geometry("400x200")
    ent1.place_forget()
    ent2.place_forget()
    ent3.place_forget()
    Ty.place(x = 200, y = 70, anchor = CENTER)
    Ty.set("Select Operation")
    Sh.place(x = 200, y = 110, anchor = CENTER)
    Sh.set("Select Shape")
    ch.place_forget()
    
def go(ty, sh):
    A = 0
    B = 0
    C = 0
    global ans
    A = a.get()
    if sh == "Rectangle" or sh == "Cylinder" or sh == "Right-angled Triangle":
        B = b.get()
    elif sh == "Normal Triangle" :
        B = b.get() 
        C = c.get()
    try:
        A = int(A)
        B = int(B)
        C = int(C)
    except ValueError:
        messagebox.showerror("Invalid Input!", "Enter integars only")
    else:
        if sh == "Square":
            print("Side = " + str(A))
            peri = A * 4
            area = A * A
            if ty == "Perimeter":
                ans = peri
            elif ty == "Area":
                ans = area

        elif sh == "Rectangle":
            print("Length = " + str(A))
            print("Height = " + str(B))
            peri = 2*(A+B)
            area = A * B
            if ty == "Perimeter":
                ans = peri
            elif ty == "Area":
                ans = area

        elif sh == "Right-angled Triangle":
            C = (A*A) + (B*B)
            C = math.sqrt(C)
            peri = A + B + C
            area = A * B
            peri = round(peri, 3)
            area = round(area, 3)
            if ty == "Perimeter":
                ans = peri
                print("Height = " + str(B))
            elif ty == "Area":
                ans = area
                print("Perp. = " + str(B))
            print("Base = " + str(A))

        elif sh == "Normal Triangle":
            peri = A + B + C
            s = peri/2
            area = s*(s-A)*(s-B)*(s-C)
            area = math.sqrt(area)
            area = round(area, 3)
            if ty == "Perimeter":
                ans = peri
            elif ty == "Area":
                ans = area
            print("Side A = " + str(A))
            print("Side B = " + str(B))
            print("Side C = " + str(C))

        elif sh == "Circle":
            peri = 2 * A * 22/7
            area = A * A * 22/7
            peri = round(peri, 3)
            area = round(area, 3)
            if ty == "Perimeter":
                ans = peri
            elif ty == "Area":
                ans = area
            print("Radius = " + str(A))

        elif sh == "Cylinder":
            peri = 2 * A * 22/7 * B
            area = A * A * 22/7 * B
            peri = round(peri, 3)
            area = round(area, 3)
            if ty == "Perimeter":
                ans = peri
            elif ty == "Area":
                ans = area
            print("Radius = " + str(A))
            print("Height = " + str(B))

        opt.config(text = (ty + " of " + sh)) 
        Ans.set(str(ans)+" cm")
        print(ty + " of this " + sh + " = " + str(ans))
        ch.place(x = 340, y = 80, anchor = CENTER)

def Submit(ty, sh):
    opt.place(x = 90, y = 155, anchor = CENTER)
    print(ty)
    print(sh)
    global peri
    global area
    global placeholder1
    global placeholder2
    global placeholder3
    Ty.place_forget()
    Sh.place_forget()
    ent1.place(x = 200, y = 70, anchor = CENTER)

    if sh == "Square":
        root.geometry("400x160")
        submit.place(x = 200, y = 115, anchor = CENTER)
        opt.place(x = 93, y = 115, anchor = CENTER)
        dis.place(x = 300, y = 115, anchor = CENTER)
        
    elif sh == "Rectangle":
        ent1.delete(0,'end')
        placeholder1 = 'Please enter length'
        ent1.insert(0,placeholder1)
        ent2.delete(0,'end')
        placeholder2 = 'Please enter breadth'
        ent2.insert(0,placeholder2)
        ent2.place(x = 200, y = 110, anchor = CENTER)
            
    elif sh == "Right-angled Triangle":
        if ty == "Perimeter":
            placeholder1 = 'Please enter perp.'            
        elif ty == "Area":
            placeholder1 = 'Please enter height'

        placeholder2 = 'Please enter base'    
        ent1.delete(0,'end')
        ent1.insert(0,placeholder1)
        ent2.delete(0,'end')
        ent2.insert(0,placeholder2)
        ent2.place(x = 200, y = 110, anchor = CENTER)

    elif sh == "Normal Triangle":
        root.geometry("400x250")
        submit.place(x = 200, y = 205, anchor = CENTER)
        opt.place(x = 93, y = 205, anchor = CENTER)
        dis.place(x = 300, y = 205, anchor = CENTER)

        placeholder1 = 'Please enter side A.'
        placeholder2 = 'Please enter side B.'
        placeholder3 = 'Please enter side C.'                    
        ent1.delete(0,'end')
        ent1.insert(0,placeholder1)
        ent2.delete(0,'end')
        ent2.insert(0,placeholder2)
        ent2.place(x = 200, y = 110, anchor = CENTER)
        ent3.delete(0,'end')
        ent3.insert(0,placeholder3)
        ent3.place(x = 200, y = 150, anchor = CENTER)
        
    elif sh == "Circle":
        root.geometry("400x160")
        submit.place(x = 200, y = 115, anchor = CENTER)
        opt.place(x = 93, y = 115, anchor = CENTER)
        dis.place(x = 300, y = 115, anchor = CENTER)
        
        placeholder1 = 'Please enter radius.'                    
        ent1.delete(0,'end')
        ent1.insert(0,placeholder1)

    elif sh == "Cylinder":
        placeholder1 = 'Please enter base radius'
        placeholder2 = 'Please enter height'
        ent1.delete(0,'end')
        ent1.insert(0,placeholder1)
        ent2.delete(0,'end')
        ent2.insert(0,placeholder2)
        ent2.place(x = 200, y = 110, anchor = CENTER)
        
    submit.config(command = lambda : go(ty, sh))

def sen(event):
    global ty
    ty = event.widget.get()

def sem(event):
    global sh
    sh = event.widget.get()

Title = Label(root, text = "Geometry Assistant", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
Title.place(x = 200, y = 30, anchor = CENTER)

Ty = ttk.Combobox(root, width = 20, textvariable = n)
Ty['values'] = ('Perimeter', 
                'Area')

Ty.place(x = 200, y = 70, anchor = CENTER)
Ty.current()
Ty.set("Select Operation")
Ty.bind("<<ComboboxSelected>>", sen)

Sh = ttk.Combobox(root, width = 20, textvariable = m)
Sh['values'] = ('Square', 
                'Rectangle',
                'Right-angled Triangle',
                'Normal Triangle',
                'Circle',
                'Cylinder')

Sh.place(x = 200, y = 110, anchor = CENTER)
Sh.current()
Sh.set("Select Shape")
Sh.bind("<<ComboboxSelected>>", sem)

ent1 = Entry(root, textvariable = a, width = 20, font = ("Comic Sans MS", 10, "bold"))
ent2 = Entry(root, textvariable = b, width = 20, font = ("Comic Sans MS", 10, "bold"))
ent3 = Entry(root, textvariable = c, width = 20, font = ("Comic Sans MS", 10, "bold"))

global placeholder1
global placeholder2
global placeholder3

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

placeholder3 = 'Please enter 3rd side'
def erase_c(event=None):
    if ent3.get() == placeholder3:
        ent3.delete(0,'end')
def add_c(event=None):
    if ent3.get() == '':
        ent3.insert(0,placeholder3)
add_c()
ent3.bind('<FocusIn>',erase_c)
ent3.bind('<FocusOut>',add_c)

opt = Label(root, text = "Unit is cm", wraplength = 120, fg = "black", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))

dis = Label(root, textvariable = Ans, fg = "black", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
dis.place(x = 300, y = 155, anchor = CENTER)

submit = Button(root, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = lambda : Submit(ty, sh))
submit.place(x = 200, y = 155, anchor = CENTER)

ch = Button(root, text = "Reuse", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = r)
