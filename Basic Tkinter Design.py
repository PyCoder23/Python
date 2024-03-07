from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title("Title")
root.geometry("400x200")
root.config(bg = "yellow")

num = tk.StringVar()
ans=tk.StringVar()

def Submit():
    ans.set("")
    A = num.get()
    try:
        A = int(A)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter integars only")
    else:
        print(A)
        ans.set(A)
        
Title = Label(root, text = "Title", fg = "red", bg = "yellow", font = ("Comic Sans MS", 18, "bold"))
Title.place(x = 200, y = 25, anchor = CENTER)

label_1 = Label(root, text = "Enter Number", fg = "blue", bg = "yellow", font = ("Comic Sans MS", 15, "bold"))
label_1.place(x = 200, y = 70, anchor = CENTER)

entry = Entry(root, width = 20, textvariable = num, fg = "blue3")
entry.place(x = 140, y = 115, anchor = CENTER)

submit = Button(root, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
submit.place(x = 260, y = 115, anchor = CENTER)

out = Label(root, textvariable = ans, bg = "yellow", font = ("Comic Sans MS", 12, "bold"))
out.place(x = 200, y = 160, anchor = CENTER)
