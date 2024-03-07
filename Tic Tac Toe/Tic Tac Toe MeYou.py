from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import sys

root = tk.Tk()
root.title('Tic Tac Toe')
root.geometry("350x400")
root.resizable('False', 'False')
root.config(bg = 'cyan')

global ch
global bh

global turn
turn = 1

global win 
win = ''

ch = "X"
bh = "O"

myve = []
moveX = []
moveO = []
for i in range(1, 10):
    myve.append(i)

global stat
stat = 1

global ate
ate = 1

global score
score = 0

global acore 
acore = 0

#TicTacToe Master:
#https://www.quora.com/Given-all-possible-games-of-Tic-Tac-Toe-which-first-move-is-the-most-likely-to-result-in-victory-for-the-first-player

def check():
    global ch
    global bh
    global stat
    global score
    global acore
    global pl
    global win
    win = ''
    if stat == 1:
        for i in moveO:
            for j in moveO:
                for k in moveO:
                    if i == 1 and j == 2 and k == 3:
                        win = 'O'
                    elif i == 4 and j == 5 and k == 6:
                        win = 'O'
                    elif i == 7 and j == 8 and k == 9:
                        win = 'O'

                    elif i == 1 and j == 4 and k == 7:
                        win = 'O'
                    elif i == 2 and j == 5 and k == 8:
                        win = 'O'
                    elif i == 3 and j == 6 and k == 9:
                        win = 'O'

                    elif i == 1 and j == 5 and k == 9:
                        win = 'O'
                    elif i == 3 and j == 5 and k == 7:
                        win = 'O'

        for i in moveX:
            for j in moveX:
                for k in moveX:
                    if i == 1 and j == 2 and k == 3:
                        win = 'X'
                    elif i == 4 and j == 5 and k == 6:
                        win = 'X'
                    elif i == 7 and j == 8 and k == 9:
                        win = 'X'

                    elif i == 1 and j == 4 and k == 7:
                        win = 'X'
                    elif i == 2 and j == 5 and k == 8:
                        win = 'X'
                    elif i == 3 and j == 6 and k == 9:
                        win = 'X'

                    elif i == 1 and j == 5 and k == 9:
                        win = 'X'
                    elif i == 3 and j == 5 and k == 7:
                        win = 'X'

        print()
        if win == bh:
            print()
            print(bh+' Wins!\nCongratulations '+pl+'! \nYou Won!\n')
            messagebox.showinfo('Game Over!', pl+' wins! Congratulations')
            score += 0
            acore += 1
            exit()

        elif win == ch:
            print()
            print(ch+' Wins!\nCongratulations '+pl+'! \nYou Won!\n')
            messagebox.showinfo('Game Over!', pl+' wins! Congratulations')
            score += 1
            acore += 0
            exit()

def start():
    global ch
    global bh
    global turn
    ch = ''
    bh = ''
    print('Welcome to Tic Tac Toe\nThis is two player mode of Tic tac toe created by PyCoder23!\nWe hope you enjoy the game & get rid of stress for a moment')
    msg = messagebox.askquestion('Welcome to 2-Player Tic Tac Toe', "Player1 do you want to play as 'X'??")
    if msg == 'yes':
        ch = 'X'
        bh = 'O'
        print("Player1, You are playing as -> 'X' and Player2, You are -> 'O'\n")
        messagebox.showinfo("Welcome", "Player1 is -> 'X' and Player2 is -> 'O'\n")
        print('First turn is yours X or Player1')
        messagebox.showinfo("Information", "First Turn -> Player 1 or 'X'")
    else:
        ch = 'O'
        bh = 'X'
        turn += 1
        print("Player1, You are playing as -> 'O' and Player2, You are -> 'X'\n")
        messagebox.showinfo("Welcome", "Player1 is -> 'O' and Player2 is -> 'X'\n")
        print('First turn is yours X or Player2\n')
        messagebox.showinfo("Information", "First Turn -> Player 2 or 'X'")

def sum1():
    global hi
    hi = 'A'
    press()

def sum2():
    global hi
    hi = 'B'
    press()

def sum3():
    global hi
    hi = 'C'
    press()

def sum4():
    global hi
    hi = 'D'
    press()

def sum5():
    global hi
    hi = 'E'
    press()

def sum6():
    global hi
    hi = 'F'
    press()

def sum7():
    global hi
    hi = 'G'
    press()

def sum8():
    global hi
    hi = 'H'
    press()

def sum9():
    global hi
    hi = 'I'
    press()

def res():
    msg = messagebox.askquestion("Welcome Back!", "Do you want to play again?")
    if msg == 'yes':
        global ate
        ate += 1

        global win
        win = ''

        global moveX
        global moveO
        moveX = []
        moveO = []

        global myve
        myve = []
        for i in range(1, 10):
            myve.append(i)

        lab1.config(text= 'A', bg = "blue", relief = GROOVE)
        lab2.config(text= 'B', bg = "blue", relief = GROOVE)
        lab3.config(text= 'C', bg = "blue", relief = GROOVE)

        lab4.config(text= 'D', bg = "blue", relief = GROOVE)
        lab5.config(text= 'E', bg = "blue", relief = GROOVE)
        lab6.config(text= 'F', bg = "blue", relief = GROOVE)

        lab7.config(text= 'G', bg = "blue", relief = GROOVE)
        lab8.config(text= 'H', bg = "blue", relief = GROOVE)
        lab9.config(text= 'I', bg = "blue", relief = GROOVE)

        global turn
        turn = 0

        start()
    else:
        fin()

def fin():
    global score
    global acore
    global ate
    root.withdraw()
    age = score/ate * 100
    mage = acore/ate * 100
    age = round(age, 2)
    mage = round(mage, 2)  
    age = str(age) + str('%')
    mage = str(mage) + str('%')
    print('P1, You played '+str(ate)+ ' games and won '+str(score)+' out of them!')
    print('P1, Your score -> '+str(age)+'\n')

    print('P2, You played '+str(ate)+ ' games and won '+str(acore)+' out of them!')
    print('P2, Your score -> '+str(mage)+'\n')
    messagebox.showinfo('Aftermath', 'You both played -> '+str(ate)+' games! Player 1 won -> '+str(score)+' and Player 2 won -> '+str(acore))
    messagebox.showerror('Please play again soon!', "Bye, Thanks for playing")
    root.destroy()
    sys.exit()

def exit():
    global win
    if win == '':
        print('Game Over!\n')
        messagebox.showinfo('Game Over!', "Match resulted in Draw! Ha ha ha!")
    global stat 
    stat = 0
    res()

def press():
    global stat
    global turn
    global ch
    global bh
    global pl
    if stat == 1:
        global hi
        if turn % 2 == 1:
            pl = 'P1'
            py = 'P2'
            mon = ch
        else:
            pl = 'P2'
            py = 'P1'
            mon = bh

        print(pl, 'You pressed -> '+hi)
        
        x = ord(hi)-64
        if x in myve:
            myve.remove(x)
            if mon == 'X':
                moveX.append(x)
            else:
                moveO.append(x)

            print(pl+', Your move -> '+str(chr(x+64)))
            print('Now, Available moves are -> ', end = '')

            for i in myve:
                print(chr(i+64), end = ' ')

            if not myve:
                print('No move left!', end = ' ')

            if x == 1:
                lab1.config(bg='black')
                lab1.config(text = mon)
                lab1.config(relief = RIDGE)

            elif x == 2:
                lab2.config(bg='black')
                lab2.config(text = mon)
                lab2.config(relief = RIDGE)

            elif x == 3:
                lab3.config(bg='black')
                lab3.config(text = mon)   
                lab3.config(relief = RIDGE)     

            elif x == 4:
                lab4.config(bg='black')
                lab4.config(text = mon)
                lab4.config(relief = RIDGE)

            elif x == 5:
                lab5.config(bg='black')
                lab5.config(text = mon)
                lab5.config(relief = RIDGE)

            elif x == 6:
                lab6.config(bg='black')
                lab6.config(text = mon) 
                lab6.config(relief = RIDGE)

            elif x == 7:
                lab7.config(bg='black')
                lab7.config(text = mon)
                lab7.config(relief = RIDGE)

            elif x == 8:
                lab8.config(bg='black')
                lab8.config(text = mon)
                lab8.config(relief = RIDGE)

            elif x == 9:
                lab9.config(bg='black')
                lab9.config(text = mon) 
                lab9.config(relief = RIDGE)
            
            check()
            if not myve:
                exit()
            print(py+' Your Turn\n')
            turn += 1
            stat = 1
            
        else:
            print('Move already chosen!')
            print('Try moving from -> ', end = '')
            if not myve:
                print('No move left!', end = ' ')
            for i in myve:
                print(chr(i+64), end = ' ')
            print('\n')
        
    
Title = Label(root, text = 'Tic Tac toe', bg = 'cyan', fg = 'blue', font = ('Comic Sans MS', 40, 'bold'))
Title.place(x = 175, y= 40, anchor = CENTER)

lab1 = Button(root, text = 'A', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum1, relief = GROOVE)
lab1.place(x = 70, y= 130, anchor = CENTER)

lab2 = Button(root, text = 'B', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum2, relief = GROOVE)
lab2.place(x = 174, y= 130, anchor = CENTER)

lab3 = Button(root, text = 'C', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum3, relief = GROOVE)
lab3.place(x = 280, y= 130, anchor = CENTER)

lab4 = Button(root, text = 'D', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum4, relief = GROOVE)
lab4.place(x = 70, y= 230, anchor = CENTER)

lab5 = Button(root, text = 'E', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum5, relief = GROOVE)
lab5.place(x = 174, y= 230, anchor = CENTER)

lab6 = Button(root, text = 'F', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum6, relief = GROOVE)
lab6.place(x = 280, y= 230, anchor = CENTER)

lab7 = Button(root, text = 'G', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum7, relief = GROOVE)
lab7.place(x = 70, y= 330, anchor = CENTER)

lab8 = Button(root, text = 'H', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum8, relief = GROOVE)
lab8.place(x = 174, y= 330, anchor = CENTER)

lab9 = Button(root, text = 'I', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum9, relief = GROOVE)
lab9.place(x = 280, y= 330, anchor = CENTER)

start()
root.mainloop()
