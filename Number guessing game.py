from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from num2words import num2words
import tkinter as tk
import random

root = tk.Tk()
root.title("Number Guessing game")
root.geometry("400x250")
root.config(bg = "cyan")
root.iconphoto(False, tk.PhotoImage(file="D:\Mayank\Tinkering\Coding\Python\Icon\globe.png"))

num = tk.StringVar()
ans=tk.StringVar()
r=tk.StringVar()

t = 5

def Guess():
    global x
    global Sum
    x = random.randint(1, 99)
    global evod
    if x % 2 == 0:
        evod = "even"
    else:
        evod = "odd"

    global prote
    fac = 0
    for i in range(1, x+1):
        if x % i == 0:
            fac += 1
    if fac == 2:
        prote = " prime"
    else:
        prote = " composite"

    y = str(x)
    global dig
    a = 0
    b = 0
    if x > 10:
        dig = " 2-digit"
        a = y[0]
        b = y[1]
    else:
        dig = " 1-digit"
        a = y[0]
    Sum = int(a) + int(b) 
        
Guess()

def fin():
    global t
    turn = 5 - t
    turn = num2words(turn)
    ans.set("Congratulations!")
    r.set("You won!")
    clue_1.config(text = "You guessed me in " + turn + " turns")
    clue_2.config(text = "The Coder's mystery was hacked by you")
    entry.place_forget()
    out.place_forget()
    submit.config(text = "Play Again")
    submit.config(command = reset)
    submit.place(x = 200, y = 200, anchor = CENTER)
    
def Submit():
    global x
    ans.set("")
    A = num.get()
    num.set("")
    try:
        A = int(A)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter integars only")
    else:
        print("You entered "+str(A))
        global t
        t -= 1
        r.set("You have " + str(t) + " attempts")
        
        if A < x:
            ans.set("Too Low")
            
        elif A > x:
            ans.set("Too High")
            
        elif A == x:
            fin()

        pro(t)

def pro(t):
    if t == 0:
        print("")
        end()

def end():
    global x
    ans.set("")
    r.set("No attempts left!")
    clue_1.config(text = "You could not guess me! Ha Ha Ha")
    clue_2.config(text = "The Coder's mystery number was "+str(x))
    entry.place_forget()
    out.place_forget()
    submit.config(text = "Try Again")
    submit.config(command = reset)
    submit.place(x = 200, y = 200, anchor = CENTER)

def reset():
    Guess()

    global evod
    global dig
    global Sum
    global t
    
    ans.set("")
    
    t = 5
    r.set("You have " + str(t) + " attempts")
    clue_1.config(text = "I am an " + evod + prote + dig + " number")
    clue_2.config(text = "Sum of my digits is " + str(Sum))
    entry.place(x = 140, y = 185, anchor = CENTER)
    out.place(x = 200, y = 220, anchor = CENTER)
    submit.config(text = "Submit")
    submit.config(command = Submit)
    submit.place(x = 260, y = 185, anchor = CENTER)
           
Title = Label(root, text = "Guess the Coder's number", fg = "red", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
Title.place(x = 200, y = 25, anchor = CENTER)

r.set("You have " + str(t) + " attempts")
rule_1 = Label(root, textvariable = r, fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
rule_1.place(x = 200, y = 70, anchor = CENTER)

global evod
global dig
clue_1 = Label(root, text = "I am an " + evod + prote + dig + " number", fg = "green2", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
clue_1.place(x = 200, y = 105, anchor = CENTER)

global Sum
clue_2 = Label(root, text = "Sum of my digits is " + str(Sum), fg = "orange", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
clue_2.place(x = 200, y = 140, anchor = CENTER)

entry = Entry(root, width = 20, textvariable = num, fg = "blue3")
entry.place(x = 140, y = 185, anchor = CENTER)

submit = Button(root, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
submit.place(x = 260, y = 185, anchor = CENTER)

out = Label(root, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
out.place(x = 200, y = 220, anchor = CENTER)
root.mainloop()