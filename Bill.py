listN = []
listQ = []
listC = []
listD = []
listG = []

print("Welcome to Billing System!")
nam = input("Please enter your name :")
mob = input(nam + ", Please enter your mobile number :")

num = int(input("\nPlease enter number of items :"))

for i in range(1, num+1):
    namI = input("Please enter name of item :")
    listN.append(namI)

    a = False
    quaI = input("Please enter quantity of item :")
    while True:
        try:
            quaI = int(quaI)
        except ValueError:
            a = True
            print("\nInvalid Input! Please enter Integar value only!")
            quaI = input("Please enter quantity of item :")
        else:
            break
    listQ.append(quaI)

    if a:
        print()

    a = False
    cosI = input("Please enter cost of item :")
    while True:
        try:
            cosI = float(cosI)
        except ValueError:
            a = True
            print("\nInvalid Input! Please enter Numerical Value only!")
            cosI = input("Please enter cost of item :")
        else:
            break
    listC.append(cosI)

    if a:
        print()

    a = False
    disI = input("Please enter disc. applicable on item :")
    while True:
        try:
            disI = float(disI)
        except ValueError:
            a = True
            print("\nInvalid Input! Please enter Numerical Value only!")
            disI = input("Please enter disc. applicable on item :")
        else:
            break
    listD.append(disI)

    if a:
        print()

    a = False
    gstI = input("Please enter GST applicable on item :")
    while True:
        try:
            gstI = int(gstI)
        except ValueError:
            a = True
            print("\nInvalid Input! Please enter Integar value only!")
            gstI = input("Please enter GST applicable on item :")
        else:
            break
    listG.append(gstI)
    print()

total = 0
totalgs = 0

for i in range(0, len(listN)):
    disded = (listC[i] * listQ[i])*(100 - listD[i])/100
    total +=  disded * (100 + listG[i]) / 100
    totalgs += disded * (0 + listG[i]) / 100

    print("S.No -> "+str(i+1))
    print("Item -> "+listN[i])
    print("Quantity -> "+str(listQ[i]))
    print("Cost -> "+str(listC[i]))
    print("Price -> "+str(listC[i] * listQ[i]))
    print("Discount of "+str(listD[i])+"% -> "+str((listC[i] * listQ[i])*(listD[i])/100))
    print("Discounted Price -> "+str(disded))
    print("GST of "+str(listG[i])+ "% -> "+str(disded * (0 + listG[i]) / 100))
    print("Price after GST -> "+str(disded * (100 + listG[i]) / 100))
    print()

print('Total -> '+str(total))
print('Total GST -> '+str(totalgs))
print('\nBye! Thanks for Using!\nPlease visit again!')