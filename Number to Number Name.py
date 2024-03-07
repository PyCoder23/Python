from num2words import num2words
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title("Number to name converter")
root.geometry("400x240")
root.config(bg = "black")

num = tk.StringVar()
ans = tk.StringVar()

def Submit():
    ans.set("")
    A = num.get()
    try:
        A = int(A)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter integars only")
    else:
        print(A)
        print(num2words(A)) # Number Name
        print(num2words(A, to = 'ordinal')) # Alpha position
        print(num2words(A, to = 'ordinal_num')) # Numeric Position
        print(num2words(A, to = 'currency')) # Currency
        print(num2words(A, lang ='fr')) # Number name in French
        print("")
        name = num2words(A)
        ans.set("Number name of "+str(A)+" is "+name)

Title = Label(root, text = "Number to Number Name", fg = "white", bg = "black", font = ("Comic Sans MS", 18, "bold"))
Title.place(x = 200, y = 25, anchor = CENTER)

label_1 = Label(root, text = "Enter Number", fg = "white", bg = "black", font = ("Comic Sans MS", 15, "bold"))
label_1.place(x = 200, y = 70, anchor = CENTER)

entry = Entry(root, width = 20, textvariable = num, fg = "black", font = ("Comic Sans MS", 11, "bold"))
entry.place(x = 200, y = 115, anchor = CENTER)

ans.set("")
submit = Button(root, text = "Submit", fg = "white", relief = "solid", bg = "blue", font = ("Comic Sans MS", 15, "bold"), command = Submit)
submit.place(x = 200, y = 170, anchor = CENTER)

out = Label(root, textvariable = ans, fg = 'white', bg = "black", font = ("Comic Sans MS", 11, "bold"), wraplength = 300, justify = "center")
out.place(x = 200, y = 210, anchor = CENTER)
root.mainloop()