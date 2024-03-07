from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import sys

root= tk.Tk()
root.config(bg = 'cyan')
root.geometry('400x220')
root.title("Welcome to Scholar's Quiz")
root.resizable(False, False)

n = tk.StringVar()
v1 = tk.StringVar()

global i, sc, at, bt
i, sc, at, bt = 0, 0, 8, 0

if at > 7:
    at = 7
bt = at

print("Welcome to Scholar's Quiz")
print('There will be 7 questions')
print('Each question will have 4 options')
print('Each Correct answer will give you 5 points')
print('Each Wrong answer will deduct 2 points')

lis1 = ['Maths', 'Physics', 'Chemistry', 'Biology', 'Sst']

def sub():
    top = n.get()
    print('\nYour selected topic -> '+top)
    messagebox.showinfo('Welcome to '+top+' quiz!', 'Please be ready for the '+top+' quiz!')

    ent.place_forget()
    submit.config(text = 'Next', command = lambda:go(top))

    a = 'There will be '+str(at)+' questions'
    lab1.config(text = a)
    lab2.config(text = 'Each question will have 4 options')

    lab1.place(x = 200, y = 77, anchor = CENTER)
    lab2.place(x = 200, y = 115, anchor = CENTER)

def go(top):
    if top ==  'Maths':
        lis2 = {"What's sq. root of -16?": ['4 i', '4', '-4'],
                "What's Factorial of 10" : ['3628800', '3628600', '3268800'],
                "What's value of Pi?"    : ['22/7', '3.140', '314'],
                "" : ['', '', '']

    if top ==  'Physics':
        lis2 = {"What's 'Cd' SI unit of?": ['Luminous Intensity', 'Amount of substance', 'Electric Current'],
                "What's speed of light?" : ['3 x 10**8 m/s', '3 x 10**5 m/s', '340 m/s'],    
                "What's 'N' SI unit of?" : ['Force', 'Temperature', 'Electric Current'],
                "What's speed of sound?" : ["330 m/s at 0'C", "343 m/s at 0'C", "330 m/s at 20'C"],
                "What is Pa of one atm?" : ["101325 Pa", "10**5 Pa", "760 Pa"],
                "What's charge of one e?": ["1.6 x 10**19 C", "1.9 x 10**16 C", "1 C"],
                "What's 'K' SI unit of?" : ['Temperature', 'Electric Current', 'Amount of substance']}

    if top ==  'Chemistry':
        lis2 = {'What is CuSo4?'          : ['Copper Sulphate', 'Copper Sulphite', 'Copper Sulphde'],
                "What's atomic mass of N?": ['14', '7', '16'],
                'What is Sc(NO3)3?'       : ['Scandium nitrate', 'Strontium nitrate', 'Tin nitride'],
                "What's atomic mass of C?": ['12', '6', '14'],
                "What's atomic mass of O?": ['16', '8', '18'],
                "What is 'At' symbol of"  : ['Astatine', 'Antimony', 'Silver'],
                "What's Bronze alloy of"  : ['Cu and Sn', 'Cu and Tn', 'Tn and Sn']}

    if top ==  'Biology':
        lis2 = {"What's Smog"            : ['Mixture of Smoke and Fog', 'Mixture of Coke and Fog' , 'Mixture of Smoke and Coke'],
                "What is Polysiphonia?"  : ['An Algae', 'A Fungi', 'A Bacteria'],
                "What is Volvox"         : ['A Colonial Algae', 'A Pathogen', 'A Cyanobacteria'],
                "What's Pencillum"       : ['A Mould', 'A Yeast', 'A Antiseptic'],
                "What is Suicidal bag?"  : ['Lysosome', 'Peroxisome', 'None of these'],
                "What is Nitrosomonas"   : ['A Chemoautotroph', 'Fungi', 'Denitrifying Bacteria'],
                "What is Cyanobacteria?" : ['A Prokaryote', 'A Eukaryote', 'A Mixotroph']}
        
    if top == 'Sst':
        lis2 = {'What is Asia?'   : ['A Continent', 'A Country', 'A Planet'],
                'What is India?'  : ['A Country', 'A Planet', 'A Continent'],
                'What is Venus?'  : ['A Planet ', 'A Country', 'A Continent'],
                'What is France?' : ['A Country', 'A Continent', 'A Planet'],
                'What is Mars?'   : ['A Planet', 'A Country', 'A Continent'],
                'What is Africa?' : ['A Continent', 'A Country', 'A Planet'],
                'What is Germany?': ['A Country', 'A Continent', 'A Planet']}
    
    def sel():
        global sc, ans, ops, at, bt
        at = bt
        print()
        opt = v1.get()
        #print(opt)
        print('You selected -> '+((list(lis2.values()))[(i-1)])[int(opt)-1])
        
        if ((list(lis2.values()))[(i-1)])[int(opt)-1] == ans:
            print('Correct Answer!')
            sc += 5

            messagebox.showinfo('Correct Answer!', 'Your answer was correct! Your score -> '+str(sc)+'!')

        else:
            print('Wrong Answer!')
            print('Correct Answer was -> '+ans)
            sc -= 2

            messagebox.showerror('Incorrect Answer!', 'Your answer was wrong! Correct Answer was -> '+ans + '! Your score -> '+str(sc)+'!')

        print('Your score -> '+str(sc))

        if i < at and i < len(list(lis2.keys())):
            v1.set(None)
            play()
        else:
            at = i
            fin(sc)

    def play():
        global i, sc, ans, ops
        i += 1

                
        que = (list(lis2.keys()))[(i-1)]
        ops = (list(lis2.values()))[(i-1)]
        ans = ops[0]

        mylis = lis2[que]
        random.shuffle(mylis)
        lis2[que] = mylis

        
        labQ.config(text = que)
        labQ.place(x = 30, y = 30, anchor = W)
            
        rbA.config(text = 'A -> '+ops[0], command=sel)
        rbB.config(text = 'B -> '+ops[1], command=sel)
        rbC.config(text = 'C -> '+ops[2], command=sel)

    titl.place_forget()
    lab1.place_forget()
    lab2.place_forget()
    submit.place_forget()

    rbA.place(x = 30, y = 75, anchor = W)
    rbB.place(x = 30, y = 125, anchor = W)
    rbC.place(x = 30, y = 175, anchor = W)
    play()

def fin(sc):
    global at

    if round(sc*100/(at*5), 3) > 50:
        print('Congratulations! You Won!!')
        messagebox.showinfo('Congratulations! You Won!', 'Your Final score -> '+str(sc)+'! Your Percentage -> '+str(round(sc*100/(at*5), 3)) + '%')

    else:
        print('Oh No! You lost! Try Again!!')
        messagebox.showerror('Oh No! You Lost!', 'Your Final score -> '+str(sc)+'! Your Percentage -> '+str(round(sc*100/(at*5), 3)) + '%')

    print('\nYour Final score -> '+str(sc))
    print('Your Percentage -> '+str(round(sc*100/(at*5), 3)) + '%')
    
    ask = messagebox.askquestion('Play Again?', 'Do you want to play again?')
    if ask == 'yes':
        re()
    else:
        end()

    labQ.place_forget()
    rbA.place_forget()
    rbB.place_forget()
    rbC.place_forget()

def re():
    titl.place(x = 200, y = 30, anchor = CENTER)
    
    lab1.config(text = 'Please select desired subject')
    lab1.place(x = 200, y = 77, anchor = CENTER)
    
    ent.place(x = 200, y = 115, anchor = CENTER)
    ent.set('Select Desired Subject')
    submit.place(x = 200, y = 167, anchor = CENTER)

    submit.config(command = sub, text = 'Submit')

    global i, sc
    i, sc = 0, 0

def end():
    messagebox.showinfo('Bye!', 'Thanks for playing! Please play again soon!')
    root.destroy()
    sys.exit()

titl = Label(root, text = "Scholar's Quiz", fg = 'blue3', bg = 'cyan', font = ('Comic Sans MS', 23, 'bold'))
titl.place(x = 200, y = 30, anchor = CENTER)

lab1 = Label(root, text = 'Please select desired subject', fg = 'blue2', bg = 'cyan', font = ('Comic Sans MS', 15, 'bold'))
lab1.place(x = 200, y = 77, anchor = CENTER)

lab2 = Label(root, text = '', fg = 'blue2', bg = 'cyan', font = ('Comic Sans MS', 15, 'bold'))

ent = ttk.Combobox(root, textvariable = n, font = ('Comic Sans MS', 10, 'bold'), values = lis1)
ent.place(x = 200, y = 115, anchor = CENTER)
ent.set('Select Desired Subject')

submit = Button(root, text = 'Submit', fg = 'white', bg = 'blue3', font = ('Comic Sans MS', 14, 'bold'), command = sub)
submit.place(x = 200, y = 167, anchor = CENTER)

labQ = Label(root, text = '', fg = 'blue3', bg = 'cyan', font = ('Comic Sans MS', 20, 'bold'))

rbA = Radiobutton(root, text = '', variable = v1, value = 1, bg = 'blue2',
                  activebackground = 'blue', fg = 'white',
                  font = ('Comic Sans MS', 14, 'bold'), selectcolor = 'black')

rbB = Radiobutton(root, text = '', variable = v1, value = 2, bg = 'blue2',
                  activebackground = 'blue', fg = 'white',
                  font = ('Comic Sans MS', 14, 'bold'), selectcolor = 'black')

rbC = Radiobutton(root, text = '', variable = v1, value = 3, bg = 'blue2',
                  activebackground = 'blue', fg = 'white',
                  font = ('Comic Sans MS', 14, 'bold'), selectcolor = 'black')

root.mainloop()
