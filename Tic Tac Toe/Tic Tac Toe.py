import random
import sys
print("This is a Tic Tac Toe")
print("You are Player 1 and Computer is Player 2")
Choice = str(input("You want X or O, if you want X enter 'X' or O enter 'O'"))
Move = 0
Move_1 = 1 
Round = 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6 
G = 7
H = 8
I = 9
while Choice != "X" and Choice != "O" :
    Choice = str(input("Please enter X if you want 'X' and if you want O enter 'O'"))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Algorithms for 'Tic Tac Toe'

# X
# Win X
def win_X():
    print("|--------------------------------------------------------------------------------------------|")
    print("X Wins")
    print("|--------------------------------------------------------------------------------------------|")
    if Choice == "X" :
        print("You are winner, Congrats")
        print("|----------------------------------------------------------------------------------------|")
        sys.exit()
    if Choice == "O" :
        print("You lose, Best of Luck, next time, Don't forget 'zitne wale ko bhi haar pehnaya zata hai'")
        print("|----------------------------------------------------------------------------------------|")
        sys.exit()

def chance_X():
    # Rows-X
    if A == "X" and B == "X" and C == "X" :
        win_X()
    if D == "X" and E == "X" and F == "X" :
        win_X()
    if G == "X" and H == "X" and I == "X" :
        win_X()

    # Cols-X
    if A == "X" and D == "X" and G == "X" :
        win_X()
    if B == "X" and E == "X" and H == "X" :
        win_X()
    if C == "X" and F == "X" and I == "X" :
        win_X()

    # Dias-X
    if A == "X" and E == "X" and I == "X" :
        win_X()
    if C == "X" and E == "X" and G == "X" :
        win_X()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# O
# Win O
def win_O():
    print("|----------------------------------------------------------------------------------------|")
    print("O Wins")
    print("|----------------------------------------------------------------------------------------|")
    if Choice == "O" :
        print("You are winner, Congrats")
        print("|----------------------------------------------------------------------------------------|")
        sys.exit()
    if Choice == "X" :
        print("You lose, Best of Luck, next time, Don't forget 'zitne wale co bhi haar pehnaya zata hai'")
        print("|----------------------------------------------------------------------------------------|")
        sys.exit()

def chance_O():
    # O
    # Rows-O    
    if A == "O" and B == "O" and C == "O" :
        win_O()
    if D == "O" and E == "O" and F == "O" :
        win_O()
    if G == "O" and H == "O" and I == "O" :
        win_O()

    # Cols-O    
    if A == "O" and D == "O" and G == "O" :
        win_O()
    if B == "O" and E == "O" and H == "O" :
        win_O()
    if C == "O" and F == "O" and I == "O" :
        win_O()
        
    # Dias-O
    if A == "O" and E == "O" and I == "O" :
        win_O()
    if C == "O" and E == "O" and G == "O" :
        win_O()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Computer Mind Algorithms

# Program Output Starts
print("This is the box of the game and has 9 letters and 9 squares, 1 on each")
print("___________________")
print("|     |     |     |")
print("|  1  |  2  |  3  |")
print("|_____|_____|_____|")
print("|     |     |     |")
print("|  4  |  5  |  6  |")
print("|_____|_____|_____|")
print("|     |     |     |")
print("|  7  |  8  |  9  |")
print("|_____|_____|_____|")
print("                   ")

#Incase X is chosen
if Choice == "X" :
    for i in range (0,4) :
        # First, Third, Five, Seven Move
        Move_1 = random.choice(numbers)
        numbers.remove(Move_1)
        print("You are 'X' and Computer is 'O'")
        print("Computer's "+str(Round)+"th move is "+str(Move_1))
        if Move_1 == 1 :
            A = "O"
        if Move_1 == 2 :
            B = "O"
        if Move_1 == 3 :
            C = "O"
        if Move_1 == 4 :
            D = "O"
        if Move_1 == 5 :
            E = "O"
        if Move_1 == 6 :
            F = "O"
        if Move_1 == 7 :
            G = "O"
        if Move_1 == 8 :
            H = "O"
        if Move_1 == 9 :
            I = "O"
            
        print("___________________")
        print("|     |     |     |")
        print("|  "+str(A)+"  |  "+str(B)+"  |  "+str(C)+"  |")
        print("|_____|_____|_____|")
        print("|     |     |     |")
        print("|  "+str(D)+"  |  "+str(E)+"  |  "+str(F)+"  |")
        print("|_____|_____|_____|")
        print("|     |     |     |")
        print("|  "+str(G)+"  |  "+str(H)+"  |  "+str(I)+"  |")
        print("|_____|_____|_____|")
        print("                   ")
        O()

        # Second, Fourth, Sixth, Eight Move
        print("You are 'X' and Computer is 'O'")
        print("Now it is your "+str(Round)+"th move ")
        Move = int(input("Please enter your move as X from "+str(numbers)))
        if Move not in numbers :
            Move = int(input("Move already choosed, Please enter your move as X from "+str(numbers)))
        if Move != Move_1 :
            numbers.remove(Move)
            if Move == 1 :
                A = "X"
            if Move == 2 :
                B = "X"
            if Move == 3 :
                C = "X"
            if Move == 4 :
                D = "X"
            if Move == 5 :
                E = "X"
            if Move == 6 :
                F = "X"
            if Move == 7 :
                G = "X"
            if Move == 8 :
                H = "X"
            if Move == 9 :
                I = "X"
                
            print("___________________")
            print("|     |     |     |")
            print("|  "+str(A)+"  |  "+str(B)+"  |  "+str(C)+"  |")
            print("|_____|_____|_____|")
            print("|     |     |     |")
            print("|  "+str(D)+"  |  "+str(E)+"  |  "+str(F)+"  |")
            print("|_____|_____|_____|")
            print("|     |     |     |")
            print("|  "+str(G)+"  |  "+str(H)+"  |  "+str(I)+"  |")
            print("|_____|_____|_____|")
            print("                   ")
            Round += 1
            X()

        
    # Ninth Move
    Move_1 = random.choice(numbers)
    numbers.remove(Move_1)
    print("You are 'X' and Computer is 'O'")
    print("Computer's "+str(Round)+"th move is "+str(Move_1))
    if Move_1 == 1 :
        A = "O"
    if Move_1 == 2 :
        B = "O"
    if Move_1 == 3 :
        C = "O"
    if Move_1 == 4 :
        D = "O"
    if Move_1 == 5 :
        E = "O"
    if Move_1 == 6 :
        F = "O"
    if Move_1 == 7 :
        G = "O"
    if Move_1 == 8 :
        H = "O"
    if Move_1 == 9 :
        I = "O"
        
    print("___________________")
    print("|     |     |     |")
    print("|  "+str(A)+"  |  "+str(B)+"  |  "+str(C)+"  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  "+str(D)+"  |  "+str(E)+"  |  "+str(F)+"  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  "+str(G)+"  |  "+str(H)+"  |  "+str(I)+"  |")
    print("|_____|_____|_____|")
    print("                   ")
    O()

# Incase O is chosed 
if Choice == "O" :
    print("You are 'O' and Computer is 'X'")
    for i in range (0,4) :
        # First, Third, Fifth, Seventh Move
        print("Now it is your "+str(Round)+"th move ")
        Move = int(input("Please enter your move as X from "+str(numbers)))
        if Move not in numbers :
            Move = int(input("Move already choosed, Please enter your move as X from "+str(numbers)))
        if Move in numbers :
            numbers.remove(Move)
            if Move == 1 :
                A = "O"
            if Move == 2 :
                B = "O"
            if Move == 3 :
                C = "O"
            if Move == 4 :
                D = "O"
            if Move == 5 :
                E = "O"
            if Move == 6 :
                F = "O"
            if Move == 7 :
                G = "O"
            if Move == 8 :
                H = "O"
            if Move == 9 :
                I = "O"
                
            print("___________________")
            print("|     |     |     |")
            print("|  "+str(A)+"  |  "+str(B)+"  |  "+str(C)+"  |")
            print("|_____|_____|_____|")
            print("|     |     |     |")
            print("|  "+str(D)+"  |  "+str(E)+"  |  "+str(F)+"  |")
            print("|_____|_____|_____|")
            print("|     |     |     |")
            print("|  "+str(G)+"  |  "+str(H)+"  |  "+str(I)+"  |")
            print("|_____|_____|_____|")
            print("                   ")
            O()

        # Second, Fourth, Sixth, Eight Move
        Move_1 = random.choice(numbers)        
        print("You are 'O' and Computer is 'X'")
        print("Computer's "+str(Round)+"th move is "+str(Move_1))
        if Move_1 == 1 :
            A = "X"
            numbers.remove(Move_1)
        if Move_1 == 2 :
            B = "X"
            numbers.remove(Move_1)
        if Move_1 == 3 :
            C = "X"
            numbers.remove(Move_1)
        if Move_1 == 4 :
            D = "X"
            numbers.remove(Move_1)
        if Move_1 == 5 :
            E = "X"
            numbers.remove(Move_1)
        if Move_1 == 6 :
            F = "X"
            numbers.remove(Move_1)
        if Move_1 == 7 :
            G = "X"
            numbers.remove(Move_1)
        if Move_1 == 8 :
            H = "X"
            numbers.remove(Move_1)
        if Move_1 == 9 :
            I = "X"
            numbers.remove(Move_1)
            
        print("___________________")
        print("|     |     |     |")
        print("|  "+str(A)+"  |  "+str(B)+"  |  "+str(C)+"  |")
        print("|_____|_____|_____|")
        print("|     |     |     |")
        print("|  "+str(D)+"  |  "+str(E)+"  |  "+str(F)+"  |")
        print("|_____|_____|_____|")
        print("|     |     |     |")
        print("|  "+str(G)+"  |  "+str(H)+"  |  "+str(I)+"  |")
        print("|_____|_____|_____|")
        print("                   ")
        Round += 1
        X()

        
    # Ninth Move
    print("You are 'O' and Computer is 'X'")
    print("Now it is your "+str(Round)+"th move ")
    Move = int(input("Please enter your move as X from "+str(numbers)))
    if Move not in numbers :
        Move = int(input("Move already choosed, Please enter your move as X from "+str(numbers)))
    if Move in numbers :
        numbers.remove(Move)
        if Move == 1 :
            A = "O"
        if Move == 2 :
            B = "O"
        if Move == 3 :
            C = "O"
        if Move == 4 :
            D = "O"
        if Move == 5 :
            E = "O"
        if Move == 6 :
            F = "O"
        if Move == 7 :
            G = "O"
        if Move == 8 :
            H = "O"
        if Move == 9 :
            I = "O"
            
        print("___________________")
        print("|     |     |     |")
        print("|  "+str(A)+"  |  "+str(B)+"  |  "+str(C)+"  |")
        print("|_____|_____|_____|")
        print("|     |     |     |")
        print("|  "+str(D)+"  |  "+str(E)+"  |  "+str(F)+"  |")
        print("|_____|_____|_____|")
        print("|     |     |     |")
        print("|  "+str(G)+"  |  "+str(H)+"  |  "+str(I)+"  |")
        print("|_____|_____|_____|")
        print("                   ")
        O()
