import random
lis = ['Rock', 'Paper', 'Scissor']

print('Welcome to Rock Paper Scissor Game!')
print('We hope you enjoy this game and feel relaxed!')

at, win, loss = 0, 0, 0

def exi():
    global at, win, loss
    print('\nYou played '+ str(at) + ' games ')
    print('You won ' + str(win) + ' games and lost '+str(loss) + ' out of them!')

    if win >= loss:
        print('You won! Congratulations!')
    else:
        print('You lost! Never mind!')
        
    print('Bye! Thanks for Playing!')

def check():
    global at, win, loss
    com = random.choice(lis)

    print('\nYou moved '+mov+' and computer moved '+com)

    if (com == 'Rock' and mov == 'Scissor') or (com == 'Scissor' and mov == 'Paper') or (com == 'Paper' and mov == 'Rock'):
        loss += 1
        print('You lost! Now Your score is -> '+str(win) + " and com's score is -> "+str(loss))

    elif (mov == 'Rock' and com == 'Scissor') or (mov == 'Scissor' and com == 'Paper') or (mov == 'Paper' and com == 'Rock'):
        win += 1
        print('You won! Now Your is score -> '+str(win) + " and com's score is -> "+str(loss))

    else:
        print('Tie! Now Your score is -> '+str(win) + " and com's score is -> "+str(loss))        
    
while True:
    mov = str(input("Please enter your move from - Rock, Paper or Scissor or enter n to exit: "))
    mov = mov.title()
    if mov.lower() == 'n':
        exi()
        break
    
    while mov != 'Rock' and mov != 'Paper' and mov != 'Scissor':
        mov = str(input("Invalid Input! Please enter your move from - Rock, Paper or Scissor or enter n to exit: "))
        mov = mov.title()

    check()
    at += 1
    print()
    
