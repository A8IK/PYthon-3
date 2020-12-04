import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="@Atik31122002",database="ATIK")

mycursor = mydb.cursor()            ##This cursor actually give me main coursor to work with my code

#mycursor.execute("show databases")
mycursor.execute("select * from student")  ##If we do execute then it'll fetch all database and it'll store cursor

result = mycursor.fetchall()   ##We are fetching data from cursor and importing that in result and result are fetching us the data
            ###We can also use here "fetchone" in that case we will get one line

for db in mycursor:
    print(db)

for i in result:
    print(i)
