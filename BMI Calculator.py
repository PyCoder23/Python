from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x230")
root.config(bg = "yellow")

wei = tk.StringVar()
hei = tk.StringVar()
ans = tk.StringVar()

def Submit():
    ans.set("")
    A = wei.get()
    B = hei.get()
    try:
        A = float(A)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter numericals only")
    else:
        try:
            B = float(B)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter numericals only")
        else:
            print(A)
            print(B)
            BMI = A/(B*B)
            BMI = round(BMI, 2)
            print(BMI)
            print("")
            ans.set(BMI)
        
Title = Label(root, text = "BMI Calculator", fg = "red", bg = "yellow", font = ("Comic Sans MS", 19, "bold"))
Title.place(x = 200, y = 25, anchor = CENTER)

placeholder_A = "Enter your weight (kg)"
entry_1 = Entry(root, width = 20, textvariable = wei, font = ("Comic Sans MS", 11, "bold"))
entry_1.place(x = 200, y = 70, anchor = CENTER)
def erase_A(event=None):
    if entry_1.get() == placeholder_A:
        entry_1.delete(0,'end')
        
def add_A(event=None):
    if entry_1.get() == '':
        entry_1.insert(0,placeholder_A)

add_A()
entry_1.bind('<FocusIn>',erase_A)
entry_1.bind('<FocusOut>',add_A)

placeholder_B = "Enter your height (m)"
entry_2 = Entry(root, width = 20, textvariable = hei, font = ("Comic Sans MS", 11, "bold"))
entry_2.place(x = 200, y = 110, anchor = CENTER)
def erase_B(event=None):
    if entry_2.get() == placeholder_B:
        entry_2.delete(0,'end')
        
def add_B(event=None):
    if entry_2.get() == '':
        entry_2.insert(0,placeholder_B)

add_B()
entry_2.bind('<FocusIn>',erase_B)
entry_2.bind('<FocusOut>',add_B)

submit = Button(root, text = "Calculate", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
submit.place(x = 200, y = 160, anchor = CENTER)

out = Label(root, textvariable = ans, bg = "yellow", font = ("Comic Sans MS", 12, "bold"))
out.place(x = 200, y = 205, anchor = CENTER)
