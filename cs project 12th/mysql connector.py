import mysql.connector as a
db=a.connect(host="localhost", user="root" , passwd="7786" )
cursor=db.cursor()
cursor.execute("create database  bankmanagment")
print("databses is createdsuccessfully")
