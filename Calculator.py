from tkinter import *
from tkinter import ttk
import tkinter as tk
import numpy as np

root = tk.Tk()
root.title("Calculator")
root.geometry("300x420")
root.config(bg="yellow")

ops = ["a", "b", "c", "d", "e", "f", "eq", "CE", "C", "bk", "sq", "rt", "cu", "curt", "rec"]

global num1
num1 = 0

global num2
num2 = 0

global Ans
Ans = 0

global op
op = ""

global A
A = 0

def callback(ans):
    char= ans.get()
    try :
        char = float(char)
    except ValueError:
        ans.set(ans.get()[0:-1])

def enter(args):
    global op
    global num1
    global num2
    if args in ops:
        if args == "eq" and float(num1) != 0:
            equal(args)
            print("")
            
        elif args == "a" or args == "b" or args == "c" or args == "d" or args == "sq" or args == "rt" or args == "per" or args == "cu" or args == "curt" or args == "rec" :
            oper(args)
            
        elif args == "C":
            op = ""
            num1 = 0
            num2 = 0
            ans.set("")
            print("")
            
        elif args == "CE":
            ans.set("")

        elif args == "bk":
            ans.set(ans.get()[0:-1])

        elif args == "e":
            a = ans.get()
            a = float(a)
            if (a % 1) == 0:
                a = int(a)
                ans.set(str(a)+".")
            else:
                ans.set(float(ans.get()))

        elif args == "f":
            val = float(ans.get())
            val = 0 - float(val)
            if val % 1 == 0:
                val = int(val)
            else:
                val = float(val)
            ans.set(val)
            
    else:
        char = ""
        char = ans.get()
        char += str(args)
        ans.set(char)

def equal(args):
    global op
    global num1
    global num2
    num2 = ans.get()
    print(num2)
    ans.set("")
    print(str(num1)+op+str(num2))
    oper(args)
    global Ans
    Ans = round(Ans, 3)
    if Ans % 1 == 0:
        Ans = int(Ans)
    else:
        Ans = float(Ans)
    a = str(Ans)
    if len(a) > 12:
        charlen = len(a)
        charlen
        b = 1
        for i in range(1, charlen+1):
            b *= 10
        a = int(Ans)
        a = a / b
        a = round(a, 6)
        sc = str(a) + " * 10 ^ "+str(i)
    ans.set(Ans)
    op = ""
    num1 = 0
    num2 = 0
    Ans = 0

def Eq():
    global Ans
    global op
    global num1
    global num2
    Ans = round(Ans, 3)
    if Ans % 1 == 0:
        Ans = int(Ans)
    else:
        Ans = float(Ans)
    ans.set(Ans)
    print("")
    op = ""
    num1 = 0
    num2 = 0
    Ans = 0
    
def oper(args):
    global num1
    global op
    global Ans
    if args == "a" or op == "+":
        op = "+"
        if args == "eq":
            Ans = float(num1) + float(num2)
            print(Ans)
        
    elif args == "b" or op == "-":
        op = "-"
        if args == "eq":
            Ans = float(num1) - float(num2)
            print(Ans)
        
    elif args == "c" or op == "x":
        op = "x"
        if args == "eq":
            Ans = float(num1) * float(num2)
            print(Ans)

    elif args == "d" or op == "/":
        op = "/"
        if args == "eq":
            Ans = float(num1) / float(num2)
            print(Ans)

    num1 = ans.get()
    print(num1)
    ans.set("")
    
    if args == "sq" or op == "sq":
        op = "sq"
        Ans = float(num1) * float(num1)
        print(Ans)
        Eq()
    elif args == "rt" or op == "rt":
        import math
        op = "rt"
        Ans = math.sqrt(float(num1))
        print(Ans)
        Eq()

    elif args == "cu" or op == "cu":
        op = "cu"
        Ans = float(num1) * float(num1) * float(num1)
        print(Ans)
        Eq()

    elif args == "curt" or op == "curt":
        op = "curt"
        Ans = num1
        Ans = np.cbrt(Ans)
        print(Ans)
        Eq()

    elif args == "rec" or op == "rec":
        op = "rec"
        Ans = 1/float(num1)
        print(Ans)
        Eq()            

def Next(event):
    global A
    print("hi")
    if A % 2 == 0:
        root.geometry("360x420")
        entry.place(x=180, y=50, anchor = CENTER)
        entry.config(width = 15)
        sq.place(x=300, y=120, anchor = CENTER)
        Root.place(x=300, y=180, anchor = CENTER)
        Cu.place(x=300, y=240, anchor = CENTER)
        curt.place(x=300, y=300, anchor = CENTER)
        rec.place(x=300, y=360, anchor = CENTER)
        
    elif A % 2 == 1:
        root.geometry("300x420")
        entry.place(x=150, y=50, anchor = CENTER)
        entry.config(width = 12)
        sq.place_forget()
        Root.place_forget()
        Cu.place_forget()
        curt.place_forget()
        rec.place_forget()
        
    A += 1 
    
ans = StringVar()
ans.trace("w", lambda name, index,mode, ans=ans: callback(ans))

entry=Entry(root, textvariable = ans, width = 12, font = ("Xenara", 28, "bold"), justify = "right")
entry.place(x=150, y=50, anchor = CENTER)

clent = Button(root, text = " CE ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("CE"))
clent.place(x=60, y=120, anchor = CENTER)

clear = Button(root, text = " C ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("C"))
clear.place(x=120, y=120, anchor = CENTER)

bksp = Button(root, text = " ⌫ ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("bk"))
bksp.place(x=180, y=120, anchor = CENTER)

add = Button(root, text = " + ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("a"))
add.place(x=240, y=120, anchor = CENTER)

but_one = Button(root, text = " 1 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(1))
but_one.place(x=60, y=180, anchor = CENTER)

but_two = Button(root, text = " 2 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(2))
but_two.place(x=120, y=180, anchor = CENTER)

but_three = Button(root, text = " 3 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(3))
but_three.place(x=180, y=180, anchor = CENTER)

sub = Button(root, text = " - ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("b"))
sub.place(x=240, y=180, anchor = CENTER)

but_four = Button(root, text = " 4 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(4))
but_four.place(x=60, y=240, anchor = CENTER)

but_five = Button(root, text = " 5 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(5))
but_five.place(x=120, y=240, anchor = CENTER)

but_six = Button(root, text = " 6 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(6))
but_six.place(x=180, y=240, anchor = CENTER)

mul = Button(root, text = " x ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("c"))
mul.place(x=240, y=240, anchor = CENTER)

but_seven = Button(root, text = " 7 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(7))
but_seven.place(x=60, y=300, anchor = CENTER)

but_eight = Button(root, text = " 8 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(8))
but_eight.place(x=120, y=300, anchor = CENTER)

but_nine = Button(root, text = " 9 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(9))
but_nine.place(x=180, y=300, anchor = CENTER)

div = Button(root, text = " / ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("d"))
div.place(x=240, y=300, anchor = CENTER)

sign = Button(root, text = "+/-", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("f"))
sign.place(x=60, y=360, anchor = CENTER)

but_zero = Button(root, text = " 0 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(0))
but_zero.place(x=120, y=360, anchor = CENTER)

point = Button(root, text = ".", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("e"))
point.place(x=180, y=360, anchor = CENTER)

eq = Button(root, text = " = ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("eq"))
eq.place(x=240, y=360, anchor = CENTER)

sq = Button(root, text = " sq ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("sq"))

Root = Button(root, text = " √ ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("rt"))

Cu = Button(root, text = " cu ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("cu"))

curt = Button(root, text = " ∛ ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("curt"))

rec = Button(root, text = " 1/x ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("rec"))

more = Label(root, text = " → ", fg = "white", bg = "white", font = ("Comic Sans MS", 22, "bold"))
more.place(x=54, y=50, anchor = CENTER)
more.bind("<Button-1>", Next)
root.mainloop()