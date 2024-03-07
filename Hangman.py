import random
words = ['DOG', 'CAT', 'BULL', 'FIST', 'APPLE', 'MOUSE', 'PENCIL', 'NUMBER', 'DOLPHIN', 'NOTEPAD']
hints = ['An animal that many people keep as a pet', 'A small animal with soft fur that people often keep as a pet',
         'An adult male of the cow family', 'A hand with the fingers closed together tightly',
         'Iphone logo', 'A very small animal with fur and a long thin tail',
         'Used to write made of wood', 'A word or symbol that indicates a quantity',
         'An intelligent animal that lives in the sea and looks like a large fish', 'Used to store typed data in pc']

wor = random.randint(0, 9)

word = words[wor]
        
plist = []
hint = hints[wor]
ch = []
at = []
for i in word:
    ch.append(i)
    at.append(i)

lim = len(word)*2 - 2

more = len(word)
a = []
for i in range(1, len(word)+1):
    a.append('_')

print('Hint -> '+hint)

while lim > 0:
    for i in a:
        print(i, end = '  ')
    print()
        
    print('You have '+str(lim)+' attempts')
    att = str(input('Guess your '+str((len(word)*2-1)-lim)+' attempt:'))
    att = att.upper()

    if att in ch:
        print('Good')
        pos = at.index(att)
        while at[pos] != att or pos in plist:
            for i in range(0, len(word)):
                pos = i
                if at[pos] == att and pos not in plist:
                    break
        a[pos] = att

        plist.append(pos)
        ch.remove(att)
        more -= 1
        if more == 0:
            print()
            for i in a:
                print(i, end = '  ')
            print()
            print('You won very good!')
            lim = 0

    elif len(att) > 1:
        print('Enter only a single letter!')
        
    elif att in at and att not in ch:
        print('You have already guessed!')
        lim -= 0
    else:
        print('Bad!')
        lim -= 1
        
    print()
    
if more != 0 and lim == 0:
    print('You lose! Try again!')
    print("The word was -> '"+word+"'")
    
