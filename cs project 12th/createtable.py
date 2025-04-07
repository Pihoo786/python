import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="7786",database="bankmanagment")
mycursor=mydb.cursor()
mycursor.execute("create table details(username char(20) primary key , password varchar(15), balance integer default(0),  loan integer default(0), intrest_rate integer default(0))")

print("table is createdsuccessfully")
                 
    
