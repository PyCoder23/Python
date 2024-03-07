import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Mayank@ATL',
    database = 'tictactoe',
    charset = 'utf8')

mycursor = mydb.cursor()
query = """SELECT * from rec ORDER BY ID"""
mycursor.execute(query)

Hig = 0
Low = 0
myresult = mycursor.fetchall()
for i in myresult:
    #print(i)
    Id = i[0]
    sc = float((i[2])[0:-1])
    if sc < 10:
        sc = '  '+str(sc)
    elif sc < 100:
        sc = ' '+str(sc)

    while len(str(sc)) < 6:
        sc = str(sc)+'0'

    if Id < 10:
        Id = '0' + str(Id)

    rev = float(i[3])
    if rev < 10:
        rev = ' ' + str(rev)

    if len(str(rev)) < 5 :
        rev = str(rev) + '0'
    
    print('ID -> '+str(Id)+', Score -> '+str(sc)+', Review given -> '+str(rev)+', Name -> '+(i[1]).upper())
