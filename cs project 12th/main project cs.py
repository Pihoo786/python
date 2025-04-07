import mysql.connector as a
db=a.connect(host="localhost", user="root" , passwd="7786" )
cursor=db.cursor()
cursor.execute("create database  bankmanagment")
print("databses is createdsuccessfully")


import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="7786",database="bankmanagment")
mycursor=mydb.cursor()
mycursor.execute("create table details(username char(20) primary key , password varchar(15), balance integer default(0),  loan integer default(0), intrest_rate integer default(0))")

print("table is createdsuccessfully")
                 


import mysql.connector as sql
db=sql.connect(host="localhost",user="root",passwd="7786",database="bankmanagment",)
cursor=db.cursor()
import time

print("__________________________________________________________________________|______________________________________________________________________________________"
"-o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o-(_)-o--o--o--o--o----o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o--o-")
print("\t\t\t\t\t DAV PUBLIC SCHOOL SEC-37")
print("\t\t\t\t\tBANK MANAGEMENT SYSTEM")
print("\t\t\t\t\t         THE WORLD BANK")
time.sleep(1)
print("\n\t\t\t\t \tDesigned and Maintainned By :")
print("\t\t\t\t\tDhanvee Birla - CLASS XII B - ROLL NO - 14 ")
time.sleep(1)
print("\n\n\t\t\t\t\t WELCOME TO THE WORLD BANK")

def balance(w):
    cursor=db.cursor()
    n="select balance from details where username=%s"
    cursor.execute(n,(w,))
    results=cursor.fetchall()
    for i in results:
        print(" your current balance is rupees", i[0])
        print("we are directing you to the main page.")
    time.sleep(2)
    mainpage()
def account_details(y):
    cursor=db.cursor()
    details="select* from details where username=%s"
    cursor.execute(details,(y,))
    results=cursor.fetchall()
    for i in results:
        print("username :",i[0] , "\npassword :" , i[1] ,"\nbalance :" , i[2], "\nloan taken :" ,i[3], "\ninterst rate :" ,i[4])
    time.sleep(2)
    mainpage()

def mainpage():
    print("\t\t\t\t\thello welcome to The World Bank")
    e=int(input("type :\n1:to deposit money\n2:to transfer money\n3:to take a loan\n4:to check account details\n5:logout\nenter"))
    time.sleep(1)
    if e==1:
        deposit()
    elif e==2:
        transfer()
    elif e==3:
         loan()
    elif e==4:
         account_details(p)
    elif e==5:
         entry()
        
def deposit():
    n=input("please enter the amount you would like to deposite in your account")
    r=input("are you sure you want to deposite in your account enter yes or no" )
    if r=="yes":
        m=(n,p)
        z="update details set balance=balance+%s where username=%s"
        cursor.execute(z,m)
        db.commit()
        balance(p)
    else:
        l=input("to enter new amount enter new in not print anything else")
        if l=="new":
            deposite()
        else:
            mainpage()
            
def transfer():
    global j
    j=input("enter user name of the person you want to transfer money")
    cursor=db.cursor()
    cursor.execute("select username from details where username=%s", (j,))
    results=cursor.fetchall()
    if results!=[]:
        r=input("enter amount that needs to be transferred")
        cursor=db.cursor()
        k=(r, p)
        l=(r, j)
        aa=("update details set balance=balance-%s where username=%s")
        bb=("update details set balance=balance+%s where username=%s" )
        cursor.execute(aa,k)
        cursor.execute(bb,l)
        balance(p)
            
    else:
        print("\n USER NOT FOUND")
        print("please enter it again or logout and create a new account")
        q=input("enter ok to enter again or anything else to go back to main page")
        time.sleep(2)
        if q=="ok":
            transfer()
        else:
            mainpage()

def password():
        print("\t\tcreate password")
        o=input("enter password")
        u=input("enter your password again ")
        if o==u:
            q=(p,o)
            m=("insert into details values(%s,%s,0,0,0)")
            cursor.execute(m,q)
            db.commit()
            print("account created successfully")
            login(p) 
        else:
            print("passwords didnt matched")
            password()

def login(p):
    print("\t\t\t\t\tLOGIN")
    cursor=db.cursor()
    cursor.execute("select username from details")
    results2=cursor.fetchall()
    if (p,) in results2:
        q=input('enter password')
        cursor.execute("select username from details where password=%s ",(q,))
        results=cursor.fetchone()
        if results is not None:
            print("you have successfully logged in")
            mainpage()
            
        else:
            print("\n PASSWORD IS WRONG  ")
            print("please enter it again")
            q=input("enter helpleo if you want want to direct to the forgot password page \n press y to enter it again \n 2 to sign up")
            if q=="y":
                login(p)
            elif q=="helpleo":
                helpleo()
            else:
                signup(p)
    else:
        print("\n USERNAME DOES NOT EXISTS")
        print("please enter it again")
        A=input("press 1 to enter again \n 2 to signup \nanything else to go back")
        if A=="1":
            login(p)
        elif A=="2":
            signup(p)
        else:
            firstpage()
        
def signup(p):
    print("\t\t\t\t\tSIGNUP")
    cursor=db.cursor()
    cursor.execute("select username from details where username=%s",(p,))
    results=cursor.fetchall()
    if results==[]:
        password()
    else:
        print("\n USERNAME ALREADY EXISTS")
        print("please enter it again")
        A=input("press 1 to enter again \n 2 to login \nanything else to go back")
        if A=="1":
            login(p)
        elif A=="2":
            login(p)
        else:
            firstpage()
     
def loan():
    print("hello!!! \t I'm here to assist you in taking loan. please select the kind of loan you want from the following options:- "
          "\n 1 :  home loan \n 2 : car loan \n 3 : education loan \n anything else to go back")
    x=input("enter")
    if x=="1":
        print("\t\t\t\t\t HOME LOAN \n we can provide you a loan of  50 lakhs with 14% interest rate")
        i=5000000
        h=14
        yes(i,h)
    elif x=="2":
        print("\t\t\t\t\t CAR LOAN \n we can provide you a loan of 11 lakhs with 6% interest rate")
        i=1100000
        h=6
        yes(i,h)
    elif x=="3":
        print("\t\t\t\t\t EDUCATIONAL LOAN \n we can provide you a loan of 15 lakhs with 3% interest rate")
        i=1500000
        h=3
        yes(i,h)
    else:
        print("we are directing you to the main page")
        mainpage()

def yes(i,h):
    t=input("do you want the loan if yes type yes else type no")
    if t=="yes":
        m=(i,p)
        d=(h,p)
        g=(i,i,h)
        z1="update details set loan=loan+%s where username=%s"
        z2="update details set intrest_rate=intrest_rate+%s where username=%s"
        cursor.execute(z1,m)
        cursor.execute(z2,d)
        db.commit()
        cursor.execute("select %s+(%s*(%s/100)) from details", g)
        mm=cursor.fetchall()
        for i in mm:
            print("now you need to pay back" , i[0] )
            break
        mainpage()
    else:
        print("we are directing you back to the loan section ")
        time.sleep(2)
        loan()
        
def about():
    print('''The World bank (TWB) a Fortune 500 company, is an Indian Multinational, Public Sector Banking and Financial services statutory body headquartered in Delhi. The rich heritage and legacy of over 200 years, accredits TWB as the most trusted Bank by Indians through generations.
TWB, one the largest Indian Bank with 1/6th market share, serves over 48 lakh customers through its vast network of over 22,40 branches, 65,60 ATMs/ADWMs, 76,08 BC outlets, with an undeterred focus on innovation, and customer centricity, which stems from the core values of the Bank - Service, Transparency, Ethics, Politeness and Sustainability.
The Bank has successfully diversified businesses through its various subsidiaries i.e TWB General loan, TWB deposit, TWB withdrawl, TWB Card, etc. It has spread its presence globally and operates across time zones through 235 offices in 29 foreign countries.
Growing with times, TWB continues to redefine banking in India, as it aims to offer responsible and sustainable Banking solutions.
          CONTACT-+91 771245678"
            EMAIL-theworldbank2324@gmail.com''' )
    q=input("press y to direct to first page or anything else to logout ")
    if q=="y":
           firstpage()
    else:
           exit()

def helpleo():
    print("hello my name is leo ")
    p=input("please tell me your username if you want to reset password")
    def pt():
        q=input("enter your password")
        o=input("enter your password again")
        f=(q,p)
        if p==o:
            t=("update details set password=%s where username=%s")
            cursor.execute(t,f)
            db.commit()
            print("password changed successfully")
            print("redirecting you to login page")
            time.sleep(3)
            login(p)
        else:
            print("passwords didnt matched")
            pt()
    pt()

def firstpage():
    print("Please choose one of the options. ")
    e=int(input("type :\n1:to log into your existing account \n2:to create a new account\n3: about us \n4:EXIT \nENTER"))
    if e==1:
        login(p)
    elif e==2:
        signup(p)
    elif e==3:
         about()
    elif e==4:
           exit()
def entry():
    global p
    print("hello!!! \t I am leo and I am here to assist you.")
    p=input("enter username")
    firstpage()
entry()    







              
