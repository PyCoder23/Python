import numpy as np 
print('Welcome to Number System Assist')
n1 = int(input('Please enter Lower Number: '))
n2 = int(input('Please enter Upper Number: '))

listNatNums = []
listWholNums = []
listInts = []

listPris = []
listPers = []
listTwinPris = []

listPriTrips = []
listHarRamaNums = []
listArmNums = []

listPalins = []
listAbundNs = []
listDefiNs = []

cub = []

for i in range(n1, n2+1):
    if i > 0:
        listNatNums.append(i)
    
    if i >= 0:
        listWholNums.append(i)
    
    listInts.append(i)

    pri = True
    for j in range(2, i):
        if i % j == 0:
            pri = False
    if pri == True and i > 0:
        listPris.append(i)
    
    F = []
    for j in range(1, i+1):
        if i % j == 0 and j != 0:
            F.append(j)
    if sum(F) == i*2 and i != 0:
        listPers.append(i)
    elif sum(F) < i*2 and i > 0:
        listDefiNs.append(i)
    elif i > 0:
        listAbundNs.append(i)

    if np.cbrt(i) % 1 == 0 or i == 0:
        cub.append(i)

    stI = str(i)
    stR = stI[::-1]
    if stR == stI:
        listPalins.append(i)

for z in cub:
    for a in cub:
        if z + a == i:
            listHarRamaNums.append(i)

for z in cub:
    for a in cub:
        for b in cub:
            if z + a + b <= n2 and z + a + b >= n1 and z != a and z != b and a != b and (z+a+b) not in listArmNums and (str(a)+str(b)+str(z)) == str(z+a+b):
                listArmNums.append(z+a+b)

for z in range(0, len(listPris)+1):
    if z < len(listPris)-1:
        j = z + 1
        se = [listPris[z], listPris[j]]
        listTwinPris.append(se)

for z in range(0, len(listPris)):
    if z < len(listPris)-2:
        j = z + 1
        k = z + 2
        if listPris[z] == 3 and listPris[j] == 5 and listPris[k] == 7:
            se = [listPris[z], listPris[j], listPris[k]]
            listPriTrips.append(se)

print("\nNatural numbers from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listNatNums)

print("\nWhole numbers from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listWholNums)

print("\nIntegars from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listInts)

print("\nPrime numbers from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listPris)

print("\nTwin primes from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listTwinPris)

print("\nPrime Triplets from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listPriTrips)

print("\nPerfect numbers from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listPers)

print("\nDeficit numbers from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listDefiNs)

print("\nAbundant numbers from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listAbundNs)

print("\nPalindrome numbers from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listPalins)

print("\nArmstrong numbers from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listArmNums)

print("\nHardy Ramanujam numbers from "+str(n1)+" to "+str(n2)+" are : ", end = "")
print(listHarRamaNums)
print()
print(cub)