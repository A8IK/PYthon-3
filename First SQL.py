import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="@Atik31122002")
print(mydb)
if (mydb):
    print("Connection Succesfull")

else:
    print("Connection error")