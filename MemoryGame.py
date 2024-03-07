from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import random

root = tk.Tk()
root.title('Memory Game')
root.geometry("400x210")
root.config(bg = 'cyan')
root.resizable(False, False)

n = tk.StringVar()
t = tk.StringVar()

moves = []

global k
k = 1

def submit():
    global n, diff

    diff = t.get()
    com.place_forget()
    print('Difficulty -> '+diff)

    lab.config(text = 'Rules', font = ('Comic Sans MS', 17, 'bold'), fg = 'blue2')
    ent.place_forget()
    rules.place(x = 200, y = 130, anchor = CENTER)

    root.geometry("400x245")

    sub.config(text = 'Next', command = com1)
    sub.place(x = 200, y = 200, anchor = CENTER)

    #messagebox.showinfo('Welcome to Memory Game!', 'Welcome to Memory Game! We hope you enjoy the game!!') 

def com1():
    lab.config(text = 'Please enter one-digit number', font = ('Comic Sans MS', 15, 'bold'))  
    rules.place_forget() 

    root.geometry("400x210")
    sub.place(x = 200, y = 160, anchor = CENTER)
    ent.place(x = 200, y = 110, anchor = CENTER)

    sub.config(command = getNum)

def getNum():
    m = 1
    global k, n, moves

    nu = str(n.get())

    num = []
    for i in nu:
        if i != ' ':
            num.append(str(i))    


    if len(num) == len(moves):
        messagebox.showerror('Invalid Input', 'Enter '+str(len(moves)+1)+ ' one digit numbers!')

    elif len(num) < len(moves):
        los(num, moves)

    else:
        n.set('')

        moves.append(num[len(num)-1])

        if k > 1 :
            pas = True
            
            for i in range(0, len(moves)):
                if moves[i] != num[i]:
                    pas = False

            if pas == False:
                m = 0
                los(num, moves)
        
        if m != 0:
            mov = random.randint(0, 9)
            moves.append(str(mov))

            lab.config(text = "Computer's Move -> "+str(mov)+"!")

            labL.config(text = "Length of Sequence -> "+str(len(moves))+"!")
            labL.place(x = 200, y = 110, anchor = CENTER)

            ent.place_forget()
            sub.config(command = next, text = 'Next')

            k += 1

def res():
    global k, num, moves, mov 
    k, mov = 0, 0
    diff = ""
    nums = []
    moves = []
    sub.config(text = 'Submit', command = submit)
    lab.config(text = 'Please select difficulty')

    labS.place_forget()
    labL.place_forget()
    com.place(x = 200, y = 110, anchor = CENTER)

    root.geometry("400x210")
    sub.place(x = 200, y = 160, anchor = CENTER)

    root.title('Memory Game')

    com.set('Please select level')
    com.current()

def next():
    ent.place(x = 200, y = 110, anchor = CENTER)
    labL.place_forget()
    sub.config(command = getNum, text = 'Submit')
    lab.config(text = "Plz extend the seq. by entering "+str(len(moves)+1)+" digs!")

def los(num, moves):
    global k, diff

    ent.place_forget()
    print('\nGame Over!')

    a = ''
    for i in num:
        a = a + i 

    lab.config(text = ' You entered -> '+a+'!')
    print('You entered -> '+a+'!')

    b = ''
    for i in moves:
        b = b + i 

    labL.config(text = 'Correct Seq. -> '+b+'!')
    print('Correct Seq. -> '+b+'!')

    labL.place(x = 200, y = 110, anchor = CENTER)

    root.geometry("400x250")

    labS.config(text = ' Your score -> '+str(k)+ '!')
    labS.place(x = 200, y = 150, anchor = CENTER)
    sub.place(x = 200, y = 200, anchor = CENTER)
    sub.config(text = 'Play Again', command = res)

    if diff == 'Easy' and k > 3:
        title.config(text = 'You win!')
        print('You win!')
    elif diff == 'Medium' and k > 5:
        title.config(text = 'You win!')
        print('You win!')
    elif diff == 'Hard' and k > 7:
        title.config(text = 'You win!')
        print('You win!')
    elif diff == 'Expert' and k > 10:
        title.config(text = 'You win!')
        print('You win!')
    elif diff == 'Nightmare' and k > 14:
        title.config(text = 'You win!')
        print('You win!')
    else:
        title.config(text = 'You lose!')
        print('You loose!')

    print('Your score -> '+str(k)+ '!\n')
    k = 0

    #print(num)
    #print(moves)

title = Label(text = 'Memory Game', fg = 'blue3', bg = 'cyan', font = ('Comic Sans MS', 20, 'bold'))
title.place(x = 200, y = 25, anchor = CENTER)

lab = Label(text = 'Please select difficulty', fg = 'blue', bg = 'cyan', font = ('Comic Sans MS', 15, 'bold'))
lab.place(x = 200, y = 70, anchor = CENTER)

labL = Label(text = '', fg = 'blue', bg = 'cyan', font = ('Comic Sans MS', 15, 'bold'))

labS = Label(text = '', fg = 'blue', bg = 'cyan', font = ('Comic Sans MS', 15, 'bold'))

ent = Entry(textvariable = n, fg = 'blue2', font = ('Comic Sans MS', 10, 'bold'))

com = ttk.Combobox(root, textvariable=t, width = 20, font = ('Comic Sans MS', 10, 'bold'))
com.set('Please select level')
com.current()
com['values'] = ('Easy',
                 'Medium',
                 'Hard',
                 'Expert',
                 'Nightmare')
com.place(x = 200, y = 110, anchor = CENTER)

sub = Button(text = 'Submit', fg = 'white', bg = 'blue2', font = ('Comic Sans MS', 13, 'bold'), command = submit)
sub.place(x = 200, y = 160, anchor = CENTER)

rul = "You say a one-digit number, and I will add another! We'll keep extending the sequence If you forget a number, you are out ! Last           one standing wins!! Ready?"
rules = Text(root, height = 3, width = 36, fg = 'white', bg = 'black', relief = GROOVE, wrap = CHAR, font = ('Comic Sans MS', 11, 'bold'))
rules.insert(INSERT, rul)
rules.config(state=DISABLED, padx = 3, pady = 3)

root.mainloop()