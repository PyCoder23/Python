SubTotal = 0
TotalGsT = 0
Total = 0
a = 0
b = 0
c = 0
i = 0
Crust = {"Thin":4.00, "Thick":6.50, "Wood Fried":8.50}
Cheese = ["Cheddar", "Colby", "Edam", "Emmental", "Gruyere", "Mozzarella", "Provolone", "Ricotta"]
Cheese_price = 0.5
Topp = {"Tomato":0.75,"Mushroom":0.75,"Pepparoni":0.50,"Onions":0.25,"Black olives":0.75,"Green peppers":0.50,"Anchovies":0.25,"Garlic":0.50,"Ham":1.50,"Bacon":1.25}


print("Hi! welcome to 'Fat pizza' pizza parlour")
Name = str(input("Please enter your name :"))
Quan = int(input(Name+", please tell how many pizzas do you want to order ? :"))

while Quan == 0:
    Quan = int(input(Name+" ,Please Order atleast one pizza :"))

Crust_T = str(input("Please tell which crust do you want from 'Thin Crust', 'Thick Crust' or 'Wood Fried Crust'  :"))

while Crust_T != "Thin" and  Crust_T != "Thick" and Crust_T != "Wood Fried" :
    Crust_T = str(input("Invalid choice, wrong spelling or Wrong case, please try again from 'Thin Crust', 'Thick Crust' or 'Wood Fried Crust'  :"))

if Crust_T == "Thin" :
    a =  Crust.get('Thin')
    SubTotal += a
if Crust_T == "Thick" :
    a =  Crust.get('Thick')
    SubTotal += a
if Crust_T == "Wood Fried" :
    a =  Crust.get('Wood Fried')
    SubTotal += a

print()

Cheese_A = int(input("Please tell the number of cheese slices do you want  :"))
while Cheese_A >= 4 :
    Cheese_A = int(input("Maximum nummber of cheese slices is three please enter three or less cheese slices  :"))

while Cheese_A == 0:
    Cheese_A = int(input(Name+" ,You have to order atleast one slice  :"))

    
Cheese_S = str(input("Please tell which type of cheese do you want from 'Cheddar', 'Colby', 'Edam', 'Emmental', 'Gruyere', 'Mozzarella', 'Provolone' or 'Ricotta'  :"))

while Cheese_S != "Cheddar" and  Cheese_S != "Colby" and Cheese_S != "Edam" and Cheese_S != "Emmental" and Cheese_S != "Gruyere" and Cheese_S != "Mozzarella" and Cheese_S != "Provolone" and Cheese_S != "Ricotta" :
    Cheese_S = str(input("Invalid choice, wrong spelling or Wrong case, please try again from 'Cheddar', 'Colby', 'Edam', 'Emmental', 'Gruyere', 'Mozzarella', 'Provolone' or 'Ricotta'  :"))

if Cheese_S == "Cheddar" :
    b =  0.5
    SubTotal += b * Cheese_A
if Cheese_S == "Colby" :
    b =  0.5
    SubTotal += b * Cheese_A
if Cheese_S == "Edam" :
    b =  0.5
    SubTotal += b * Cheese_A
if Cheese_S == "Emmental" :
    b =  0.5
    SubTotal += b * Cheese_A
if Cheese_S == "Gruyere" :
    b =  0.5
    SubTotal += b * Cheese_A
if Cheese_S == "Mozzarella" :
    b =  0.5
    SubTotal += b * Cheese_A
if Cheese_S == "Provolone" :
    b =  0.5
    SubTotal += b * Cheese_A
if Cheese_S == "Ricotta" :
    b =  0.5
    SubTotal += b * Cheese_A
    
print()

Topp_N = int(input("Please tell the number of toppings do you want  :"))
while Topp_N >= 7 :
    Topp_N = int(input("Maximum nummber of toppings is six please enter six or less number of toppings :"))

while Topp_N == 0:
    Topp_N = int(input(Name+" ,You have to order atleast one topping :"))
    
Topp_T = str(input("Please tell which type of toppings do you want from 'Tomato', 'Mushroom', 'Pepparoni', 'Onions', 'Black olives', 'Green peppers', 'Anchovies', 'Garlic', 'Ham', 'Bacon' :"))

while Topp_T != "Tomato" and  Topp_T != "Mushroom" and Topp_T != "Pepparoni" and Topp_T != "Onions" and Topp_T != "Black olives" and Topp_T != "Green peppers" and Topp_T != "Anchovies" and Topp_T != "Garlic" and Topp_T != "Ham" and Topp_T != "Bacon":
    Topp_T = str(input("Invalid choice, wrong spelling or Wrong case, please try again from 'Tomato', 'Mushroom', 'Pepparoni', 'Onions', 'Black olives', 'Green peppers', 'Anchovies', 'Garlic', 'Ham', 'Bacon' :"))

if Topp_T == "Tomato" :
    i = (Topp.get('Tomato'))
    SubTotal += i * Topp_N
if Topp_T == "Mushroom" :
    i = (Topp.get('Mushroom'))
    SubTotal += i * Topp_N
if Topp_T == "Pepparoni" :
    i = (Topp.get('Pepparoni'))
    SubTotal += i * Topp_N
if Topp_T == "Onions" :
    i = (Topp.get('Onions'))
    SubTotal += i * Topp_N
if Topp_T == "Black olives" :
    i = (Topp.get('Black olives'))
    SubTotal += i * Topp_N
if Topp_T == "Green peppers" :
    i = (Topp.get('Green peppers'))
    SubTotal += i * Topp_N
if Topp_T == "Anchovies" :
    i = (Topp.get('Anchovies'))
    SubTotal += i * Topp_N
if Topp_T == "Garlic" :
    i = (Topp.get('Garlic'))
    SubTotal += i * Topp_N
if Topp_T == "Ham" :
    i = (Topp.get('Ham'))
    SubTotal += i * Topp_N
if Topp_T == "Bacon" :
    i = (Topp.get('Bacon'))
    SubTotal += i * Topp_N
    
c = a 
d = c * 5 / 100
e = d + c
Total += e
TotalGsT += d

print("")
print("↓↓↓↓↓ Bill ↓↓↓↓↓ ")
print("")
print("$$$!! All prices are in dollars !!$$$")
print("")

headers = [
    'Item',
    'Type',
    'Rate', 
    'Quantity',
    'Cost',
    'Gst', 
    'Price'
]
rows = [ ]

rows.append([Crust_T, 'Crust', str(a), str("1"), str(c), str(d), str(e)])
c = b * Cheese_A
d = c * 5 / 100
e = d + c
Total += e
TotalGsT += d

rows.append([Cheese_S, 'Cheese', str(b), str(Cheese_A), str(c), str(d), str(e)])

c = i * Topp_N
d = c * 5 / 100
e = d + c
Total += e
TotalGsT += d
SubTotal = SubTotal 
Total = Total
Total = round(Total, 3)
TotalGsT = TotalGsT
TotalGsT = round(TotalGsT, 3)

rows.append([Topp_T, 'Topping', str(i), str(Topp_N), str(c), str(d), str(e)])

rows.append(["Per pizza = ", "", "", "", str(SubTotal), str(TotalGsT), str(Total)])
rows.append(["", "", "", "", "", "", ""])
rows.append(["Total = ", "", "", str(Quan),str(round(SubTotal * Quan, 2)), str(round(TotalGsT*Quan, 3)), str(round(Total * Quan, 3))])

print(f'{headers[0]: <17}{headers[1]: <13}{headers[2]:<11}{headers[3]:<14}{headers[4]:<10}{headers[5]:<10}{headers[6]}')

for row in rows:
    print(f'{row[0]: <17}{row[1]: <13}{row[2]: <15}{row[3]: <10}{row[4]: <10}{row[5]: <10}{row[6]}')
print()