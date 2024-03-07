from tkinter import *
from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title('Percentage Calculator')
root.geometry('400x210')
root.config(bg = 'cyan')

n = tk.StringVar()

def sub():
    global des
    des = n.get()
    n.set('')
    try:
        des = float(des)
    except ValueError:
        messagebox.showerror('Invalid Input!', 'Please enter numerical value only!')
    else:
        if des < 0 or des > 100:
            messagebox.showerror('Invalid Input!', 'Please enter valid value from 0 to 100 only!')
            n.set('')

        else:
            print('Desired percentage -> '+str(des))
            lab.config(text = 'Enter your percentage Term 1')
            submit.config(command = proHF)

def proHF():
    global hfper
    hfper = n.get()
    n.set('')
    try:
        hfper = float(hfper)
    except ValueError:
        messagebox.showerror('Invalid Input!', 'Please enter numerical value only!')
    else:
        if hfper < 0 or hfper > 100:
            messagebox.showerror('Invalid Input!', 'Please enter valid value from 0 to 100 only!')
            n.set('')

        else:
            print('Your percentage in Term 1 -> '+str(hfper))
            pro()

def pro():
    lab.config(text = 'Enter marks in PT2 of SST')
    submit.config(command = pro1)

def pro1():
    global sst
    sst = n.get()
    n.set('')
    try:
        sst = float(sst)
    except ValueError:
        messagebox.showerror('Invalid Input!', 'Please enter numerical value only!')
    else:
        if sst < 0 or sst > 25:
            messagebox.showerror('Invalid Input!', 'Please enter valid value from 0 to 25 only!')
            n.set('')

        else:
            print('\nYour marks in Sst Pt2 -> '+str(sst))
            
            lab.config(text = 'Enter marks in PT2 of Science')
            submit.config(command = pro2)

def pro2():
    global sci
    sci = n.get()
    n.set('')
    try:
        sci = float(sci)
    except ValueError:
        messagebox.showerror('Invalid Input!', 'Please enter numerical value only!')
    else:
        if sci < 0 or sci > 25:
            messagebox.showerror('Invalid Input!', 'Please enter valid value from 0 to 25 only!')
            n.set('')

        else:
            print('Your marks in Sci Pt2 -> '+str(sci))
            
            lab.config(text = 'Enter marks in PT2 of Maths')
            submit.config(command = pro3)

def pro3():
    global mat
    mat = n.get()
    n.set('')
    try:
        mat = float(mat)
    except ValueError:
        messagebox.showerror('Invalid Input!', 'Please enter numerical value only!')
    else:
        if mat < 0 or mat > 25:
            messagebox.showerror('Invalid Input!', 'Please enter valid value from 0 to 25 only!')
            n.set('')

        else:
            print('Your marks in Maths Pt2 -> '+str(mat))
            
            lab.config(text = 'Enter marks in PT2 of Hindi')
            submit.config(command = pro4)

def pro4():
    global hin
    hin = n.get()
    n.set('')
    try:
        hin = float(hin)
    except ValueError:
        messagebox.showerror('Invalid Input!', 'Please enter numerical value only!')
    else:
        if hin < 0 or hin > 25:
            messagebox.showerror('Invalid Input!', 'Please enter valid value from 0 to 25 only!')
            n.set('')

        else:
            print('Your marks in Hindi Pt2 -> '+str(hin))
            
            lab.config(text = 'Enter marks in PT2 of English')
            submit.config(command = pro5)

def pro5():
    global eng
    eng = n.get()
    n.set('')
    try:
        eng = float(eng)
    except ValueError:
        messagebox.showerror('Invalid Input!', 'Please enter numerical value only!')
    else:
        if eng < 0 or eng > 25:
            messagebox.showerror('Invalid Input!', 'Please enter valid value from 0 to 25 only!')
            n.set('')

        else:
            print('Your marks in English Pt2 -> '+str(eng))
            
            #lab.config(text = 'Enter marks in PT2 of English')
            lab.place_forget()
            com()

def com():
    global des, hfper, sst, sci, mat, hin, eng, myt, myp
    Sum = des*2
    myp = Sum - hfper

    myt = (sst + sci + mat + hin + eng)*2/5
    myt += 50

    lab.place(x = 200, y = 77, anchor = CENTER)
    lab2.place(x = 200, y = 115, anchor = CENTER)
    ent.place_forget()
    
    print()
    if myt+400 < myp*5:
        maxe = (((myt+400)/5)+hfper)/2
        print('Oh Sorry! It is not possible to acheive this percentage')
        print('Maximum Percentage You can get \nBy acheiving full marks in annual exams is -> '+str(round(maxe,3))+'%')

        lab.config(text = "Oh Sorry! It is Impossible")
        lab2.config(text = "Maximum Percentage -> "+str(round(maxe,3))+'%')
        
        messagebox.showinfo("Oh Sorry!", "Maximum Percentage You can get -> "+str(round(maxe,3))+'%')        

    else:
        myt = (myt+400) - myp*5
        myt = round(myt, 3)
        print("You can only afford to do mistakes worth "+str(myt)+" Marks in combined Annual Exams!")
        print("Try Hard! All the Best!")

        lab.config(text = "Your Limit "+str(myt)+" Marks")
        lab2.config(text = "Try Hard! All the Best!")
        
        messagebox.showinfo("Try Hard! All the Best!", "You can only do mistakes worth "+str(myt)+" Marks in all Subjects!")

    submit.config(text = 'Use Again!', command = re)

def re():
    global des, hfper, sst, sci, mat, hin, eng, myt, myp
    des, hfper, sst, sci, mat, hin, eng, myt, myp = 0, 0, 0, 0, 0, 0, 0, 0, 0
    
    lab.config(text = 'Enter desired percentage')
    lab2.place_forget()
    ent.place(x = 200, y = 115, anchor = CENTER)
    submit.config(command = sub, text = 'Submit')

titl = Label(root, text = 'Percentage Calculator', fg = 'blue3', bg = 'cyan', font = ('Comic Sans MS', 23, 'bold'))
titl.place(x = 200, y = 30, anchor = CENTER)

lab = Label(root, text = 'Enter desired percentage', fg = 'blue3', bg = 'cyan', font = ('Comic Sans MS', 15, 'bold'))
lab.place(x = 200, y = 77, anchor = CENTER)

lab2 = Label(root, text = '', fg = 'blue3', bg = 'cyan', font = ('Comic Sans MS', 15, 'bold'))

ent = Entry(root, textvariable = n, fg = 'black', font = ('Comic Sans MS', 10, 'bold'))
ent.place(x = 200, y = 115, anchor = CENTER)

submit = Button(root, text = 'Submit', fg = 'white', bg = 'blue3', font = ('Comic Sans MS', 14, 'bold'), command = sub)
submit.place(x = 200, y = 167, anchor = CENTER)

root.mainloop()
