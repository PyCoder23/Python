print('>------------------------------------------------------------------------------<')
print('\t\t\t        Welcome to PyCoders')
print('\t\t\tA program to print Number combination')
print('>------------------------------------------------------------------------------<')
nums = int(input('Please enter no. of numbers do you want to enter:'))
print('>------------------------------------------------------------------------------<')
lis = []
for i in range(1, nums+1):
    if i == 1: my = 'st'
    elif i == 2: my = 'nd'
    elif i == 3: my = 'rd'
    else: my = 'th'
    n = int(input('Please enter your '+str(i) + my + ' number:' ))

    lis.append(n)

print('>------------------------------------------------------------------------------<')

for i in lis:
    for j in lis:
        print(i, j)

print('>------------------------------------------------------------------------------<')
print('\t\t\t Bye! Thanks for using this program')
print('>------------------------------------------------------------------------------<')
