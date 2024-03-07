# Jai Shree Ram
# Har Har Mahadev
# Interschool DPS Mayank 8B, Niaamit 8C
# Python program to print a number pyramid

# Statements which print the welcome lines!
print('>------------------------------------------------------------------------------<')
print('\t\t\t    Welcome to DPS Bathinda')
print('\t\t      A Program to Print a Number Pyramid')

# Variable which makes it possible for the program to be run multiple times if the user wishes!
ch = 'y'

# While loop which runs the program till the user wishes
while ch.lower() == 'y':
    print('>------------------------------------------------------------------------------<')
    
    # Statement which takes inputs the desired number of rows for pyramid!
    n = str(input('Enter the size of pyramid:'))
    
    # Variable which checks for invalid inputs for the no. of rows
    g = '1'

    # While loop which checks for invalid inputs for the no. of rows
    while g == '1':

        # Try loop which trys to convert input no. into int value!
        try:                        
            n = int(n)

        # Loop which asks for the desired number of rows for pyramid again till the input is an integer!     
        except ValueError:
            
            # Statement which takes inputs the desired number of rows for pyramid till user enters valid input!
            n = str(input('Invalid Input! Enter the size of pyramid:'))            

        else:
            # Statement to break the while loop if the input value is integer and is valid!
            g = '0'     

    # For loop which makes the program run the no. of rows as the desired number!
    for i in range(1, n+1):

        # For loop which makes the program run the no. of columns as the program wants!
        for j in range(1, 2*n):    
            
            # If loop which checks if the place is correct for placement of number!
            if j == n or (j >= n + 1 - i and j <= n + i - 1):
                
                # Statement which prints the number(i) but does not move to the new line!
                print(i, end = '  ')

            # Else loop which runs if the place is incorrect for placement of number!
            else:
                
                # Statement which prints blank at undesired places but does not move to the new line!
                print(" ", end = '  ')       

        # Statement which makes the program to come to new line
        print()

    # Input statement which asks the user if they want to continue!
    ch = str(input('Do you want to continue or not? y/n : '))

    # While loop which checks if the input in 'ch' entered by user is either 'y' or 'n'!
    while ch.lower() != 'y' and ch.lower() != 'n':

        # Input statement which asks the user if they want to continue until input is valid!!
        ch = str(input('Do you want to continue or not? Enter out of y/n only! : '))

  
# Line to greet the user 'Bye'!
print('>------------------------------------------------------------------------------<')
print('\t\t\t Thanks for using this Program ')
print('\t\t\tGreetings from Mayank')
print('>------------------------------------------------------------------------------<')

