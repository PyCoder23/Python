x = 0
y = 0
cx = ""
cy = ""
Out = ""
h = 0
H = 0
print("This is a distance calculator")
n = int(input("Enter the number of turns in the way"))
for i in range(1, n+2) :
    if i <= n :
        if i == 1 :
            a = int(input("Enter the distance(m) covered before taking "+str(i)+"st turn"))
        if i == 2 :
            a = int(input("Enter the distance(m) covered before taking "+str(i)+"nd turn"))
        if i == 3 :
            a = int(input("Enter the distance(m) covered before taking "+str(i)+"rd turn"))
        if i >= 4 :
            a = int(input("Enter the distance(m) covered before taking "+str(i)+"th turn"))
    if i > n :
        a = int(input("Enter the distance(m) covered before reaching the final destination"))
    b = str(input("Enter the direction you travelled in from North, East, South and West"))
    while b != "North" and b != "East" and b != "South" and b != "West" :
        b = str(input("Invalid Input, Enter the direction you travelled in from North, East, South and West"))
    if b == "North" :
        y = y + a
    if b == "East" :
        x = x + a
    if b == "South" :
        y = y - a
    if b == "West" :
        x = x - a
if x > 0 :
    cx = "East"
if x < 0 :
    cx = "West"
if y > 0 :
    cy = "North"
if y < 0 :
    cy = "South"
if x == 0 :
    cx = ""
if y == 0 :
    cy = ""
import math
h = math.sqrt((x * x) + (y*y))
H = round(h, 3)
print("You are "+str(H)+"m away from starting point in "+cy+cx+" direction")
