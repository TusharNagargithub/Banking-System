from tkinter import*
import time
from random import*
import tkinter.messagebox
from tkinter import messagebox
import mysql.connector
localtime=time.asctime(time.localtime(time.time()))
t=Tk()
t.geometry("2000x900")
t.title("HOME PAGE_(Tushar Nagar)"); #title name of Web Application
t.config(bg="LightBlue1")
lab1=Label(t,bg="yellow",fg="black",text="Welcome To The Home page of Bank Management System",font=("times new roman","35"))
lab1.place(x=200,y=50)
lab2=Label(t,bg="yellow",fg="black",text="Select your bank ",font=("times new roman","30"))
lab2.place(x=450,y=150)
con=mysql.connector.connect(user='root',password='',host='localhost',database='tushar')
def chk111():  #Create A Loan Form
    obj22=Tk()
    obj22.geometry("2000x900")
    obj22.title("CreateAccount_(Tushar Nagar)")
    obj22.config(bg="DarkOrange1")
    cur=con.cursor()
    lab411=Label(obj22,bg="yellow",fg="black",text="Ok i'm in loan form",font=("times new roman","20"))
    lab411.place(x=750,y=20)
    lab411=Label(obj22,bg="yellow",fg="black",text="Please Fill your complete detail for Loan",font=("times new roman","40"))
    lab411.place(x=100,y=20)
    lab51=Label(obj22,bg="black",fg="white",text="Enter your first name",font=("times new roman","30"))
    lab51.place(x=160,y=150)
    a31=Entry(obj22,font=("times new roman","30"))
    a31.place(x=550,y=150)
    lab611=Label(obj22,bg="black",fg="white",text="Enter your last name",font=("times new roman","30"))
    lab611.place(x=160,y=210)
    a41=Entry(obj22,font=("times new roman","25"))
    a41.place(x=550,y=210)
    lab71=Label(obj22,bg="black",fg="white",text="Enter Pin Card Number",font=("times new roman","30"))
    lab71.place(x=160,y=270)
    a51=Entry(obj22,font=("times new roman","25"))
    a51.place(x=550,y=270)
    lab81=Label(obj22,bg="black",fg="white",text="Enter Customer_id ",font=("times new roman","30"))
    lab81.place(x=160,y=330)
    a61k=Entry(obj22,font=("times new roman","25"))
    a61k.place(x=550,y=330)
    lab91=Label(obj22,bg="black",fg="white",text="Enter Password ",font=("times new roman","30"))
    lab91.place(x=160,y=390)
    a71=Entry(obj22,font=("times new roman","30"))
    a71.place(x=550,y=390)
    r11=StringVar()
    lab1611=Label(obj22,bg="black",fg="white",text="Select Gender",font=("times new roman","30"))
    lab1611.place(x=160,y=450)
    rb1=Radiobutton(obj22,font=("times new roman","30"),bg="yellow",text="female",variable=r11,value="female")
    rb1.place(x=550,y=450)
    rb11=Radiobutton(obj22,font=("times new roman","30"),bg="yellow",text="Male",variable=r11,value="male")
    rb11.place(x=700,y=450)
    lab812=Label(obj22,bg="black",fg="white",text="Enter Loan Type ",font=("times new roman","30"))
    lab812.place(x=160,y=510)
    a612=Entry(obj22,font=("times new roman","30"))
    a612.place(x=550,y=510)
    lab82=Label(obj22,bg="black",fg="white",text="Enter your Adress ",font=("times new roman","30"))
    lab82.place(x=160,y=570)
    a62=Entry(obj22,font=("times new roman","30"))
    a62.place(x=550,y=570)
    lab83=Label(obj22,bg="black",fg="white",text="Enter Amount For Loan ",font=("times new roman","30"))
    lab83.place(x=160,y=630)
    lnamt=Entry(obj22,font=("times new roman","30"))
    lnamt.place(x=550,y=630)
    def mysql1():  # Submit Loan Form data in your database
        ln=lnamt.get()
        cust_id=str(a61k.get())
        cur=con.cursor()
        cur.execute("SELECT * FROM studenttable where customer_id=%s",(cust_id,))
        datak=cur.fetchone()
        if not datak:
            lab831=Label(obj22,bg="skyblue",fg="black",text="Please correct enter customer _id",font=("times new roman","35"))
            lab831.place(x=100,y=270)
        else:
            pn=int(datak[3])
            pk=int(lnamt.get())
            sm1=pn+pk
            sm=str(sm1)
            cur.execute("update studenttable set time_loan=%s where customer_id=%s ",(localtime,cust_id))
            cur.execute("update studenttable set Loan=%s where customer_id=%s ",(sm,cust_id))
            con.commit()
            lab831=Label(obj22,bg="skyblue",fg="black",text="your Loan has been pass",font=("times new roman","35"))
            lab831.place(x=100,y=270)
    bt1j=Button(obj22,bg="blue",fg="white",text="Submit data for loan",font=("times new roman","35"),command=mysql1)
    bt1j.place(x=120,y=690)
    def rfh():
        obj22.destroy()
        chk111()
    bt1j=Button(obj22,bg="blue",fg="white",text="Refresh",font=("times new roman","35"),command=rfh)
    bt1j.place(x=600,y=690)
    def bkw():
        obj22.destroy()
    bt1j=Button(obj22,bg="blue",fg="white",text="back",font=("times new roman","35"),command=bkw)
    bt1j.place(x=850,y=690)
def login():  # Create a Login Form for Filling your Email'id
    obj=Tk()
    obj.geometry("2000x900")
    obj.config(bg="PaleGreen1")
    obj.title(" LOGIN_(Tushar Nagar)")
    lab=Label(obj,bg="yellow",fg="black",text="Please Enter Your Email'id And Password",font=("times new roman","35"))
    lab.place(x=150,y=50)
    lab3=Label(obj,bg="black",fg="white",text="Enter Your Email'id",font=("times new roman","25"))
    lab3.place(x=250,y=200)
    a1=Entry(obj,font=("times new roman","25"))
    a1.place(x=550,y=200)
    lab4=Label(obj,bg="black",fg="white",text="Enter Your Password",font=("times new roman","25"))
    lab4.place(x=250,y=250)
    a2=Entry(obj,font=("times new roman","25"))
    a2.place(x=550,y=250)
    rdm1=randint(1000,9999)
    lb5e11=Label(obj,bg="silver",fg="black",text="Capture",font=("times new roman","20"))
    lb5e11.place(x=380,y=350)
    lb5e4=Label(obj,bg="skyblue",fg="black",text=rdm1,font=("times new roman","20"))
    lb5e4.place(x=500,y=350)
    a13e4=Entry(obj,font=("times new roman","20"))
    a13e4.place(x=400,y=300)
    def go():
        obj.destroy()
    bt1j1=Button(obj,bg="blue",fg="white",text="back",font=("times new roman","20"),command=go)
    bt1j1.place(x=550,y=500)
    def mylogin():  # Verify Your Login Form Email'id
        if len(a13e4.get())==0:
            vlu1=0
        else:
            vlu1=int(a13e4.get())
        if  vlu1==0:
            lb5e11=Label(obj,bg="yellow",fg="black",text="Please Enter Capture value",font=("times new roman","25"))
            lb5e11.place(x=380,y=700)
        elif vlu1!=rdm1:
            lb5e11=Label(obj,bg="yellow",fg="black",text="Please Enter correct Capture value",font=("times new roman","25"))
            lb5e11.place(x=380,y=700)            
        elif (a1.get()=="Tushar@gmail.com" and a2.get()=="123"):
            obj1=Tk()
            obj1.geometry("2000x900")
            obj1.config(bg="orchid1")
            def createAccount():   # Create Form for Creating Your Bank Account
                obj2=Tk()
                obj2.geometry("2000x900")
                obj2.title("CreateAccount_(Tushar Nagar)t")
                obj2.config(bg="DarkOrange1")
                lab4=Label(obj2,bg="yellow",fg="black",text="Please enter your complete detail for creating your Account",font=("times new roman","40"))
                lab4.place(x=100,y=20)
                lab5=Label(obj2,bg="black",fg="white",text="Enter your first name",font=("times new roman","30"))
                lab5.place(x=160,y=150)
                a3=Entry(obj2,font=("times new roman","30"))
                a3.place(x=550,y=150)
                lab6=Label(obj2,bg="black",fg="white",text="Enter your last name",font=("times new roman","30"))
                lab6.place(x=160,y=210)
                a4=Entry(obj2,font=("times new roman","25"))
                a4.place(x=550,y=210)
                lab7=Label(obj2,bg="black",fg="white",text="Enter Pin Card Number",font=("times new roman","30"))
                lab7.place(x=160,y=270)
                a5=Entry(obj2,font=("times new roman","25"))
                a5.place(x=550,y=270)
                lab8=Label(obj2,bg="black",fg="white",text="Enter Customer_id ",font=("times new roman","30"))
                lab8.place(x=160,y=330)
                a6=Entry(obj2,font=("times new roman","25"))
                a6.place(x=550,y=330)
                lab9=Label(obj2,bg="black",fg="white",text="Enter Password ",font=("times new roman","30"))
                lab9.place(x=160,y=390)
                a7=Entry(obj2,font=("times new roman","30"))
                a7.place(x=550,y=390)
                r1=StringVar()
                lab16=Label(obj2,bg="black",fg="white",text="Select Gender",font=("times new roman","30"))
                lab16.place(x=160,y=450)
                rb=Radiobutton(obj2,font=("times new roman","30"),bg="yellow",text="female",variable=r1,value="female")
                rb.place(x=550,y=450)
                rb1=Radiobutton(obj2,font=("times new roman","30"),bg="yellow",text="Male",variable=r1,value="male")
                rb1.place(x=700,y=450)
                def mysql(): # Submit your Filling Form data in MySql Database.
                    name=a3.get()+" "+a4.get()
                    customer=a6.get()
                    l3=len(customer)
                    l4=len(name)
                    balance="100"
                    ln="0"
                    password=a7.get()
                    l5=len(password)
                    l6=len(a5.get()) #pincard
                    if l3==0 and l4==0 and l5==0 and l6==0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid first an last name,customer'id ,passsword and pincode",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l3==0 and l4==0 and l5!=0 and l6!=0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid first an last name,customer'id ",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l3==0 and l4!=0 and l5!=0 and l6==0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid customer'id ,passsword",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l3!=0 and l4!=0 and l5==0 and l6==0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid passsword and pincode",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l3!=0 and l4!=0 and l5!=0 and l6==0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid pincode",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l3!=0 and l4!=0 and l5==0 and l6!=0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid passsword",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l3!=0 and l4==0 and l5!=0 and l6!=0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid first an last name ",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l3==0 and l4!=0 and l5!=0 and l6!=0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid customer'id ",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l3==0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid customer'id ",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l4==0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid customer'id ",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l5==0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid password ",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l6==0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid pincard ",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l3!=0 and l4!=0 and l5!=0 and l6==0:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter valid pincard ",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    elif l3!=0 and l4!=0 and l5!=0 and l6!=0:
                        cur=con.cursor();
                        cur.execute("insert into studenttable values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,customer,balance,ln,password,localtime,localtime,localtime,localtime))
                        con.commit()
                        cur.close()
                        objj=Tk()
                        objj.geometry("2000x900")
                        objj.config(bg="PaleGreen1")
                        lab16=Label(objj,bg="yellow",fg="black",text="Congrats!...Your Account has been Created",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                        bt13=Button(objj,bg="red",fg="white",text="Click here",font=("times new roman","45"),command=login_bank)
                        bt13.place(x=500,y=450)
                        lab16=Label(objj,bg="yellow",fg="black",text="Congrats!...Your Account has been Created",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                    else:
                        lab16=Label(obj2,bg="yellow",fg="black",text="Please enter correct values",font=("times new roman","45"))
                        lab16.place(x=80,y=250)
                bt1=Button(obj2,bg="red",fg="white",text="Submit mysql",font=("times new roman","35"),command=mysql)
                bt1.place(x=160,y=550)
                def rfsh():
                    obj2.destroy()
                    createAccount()
                def rfsh1():
                    obj2.destroy()
                bt1=Button(obj2,bg="red",fg="white",text="Refresh",font=("times new roman","35"),command=rfsh)
                bt1.place(x=500,y=550)
                bt1=Button(obj2,bg="red",fg="white",text="Back",font=("times new roman","35"),command=rfsh1)
                bt1.place(x=700,y=550)
            def operationdatabase():  # Create Form for Verify your Bank Account
                obj3=Tk()
                obj3.geometry("900x800")
                obj3.title("CreateAccoun_(Tushar Nagar)t")
                obj3.config(bg="DarkOrange1")
                lab14=Label(obj3,bg="blue",fg="white",text="Please enter your complete detail for creating your Account",font=("times new roman","25"))
                lab14.place(x=50,y=20)
                lab15=Label(obj3,bg="black",fg="white",text="Enter your name",font=("times new roman","25"))
                lab15.place(x=80,y=100)
                a13=Entry(obj3,font=("times new roman","25"))
                a13.place(x=400,y=100)
                lab16=Label(obj3,bg="black",fg="white",text="Enter your customer_id ",font=("times new roman","25"))
                lab16.place(x=80,y=150)
                a14=Entry(obj3,font=("times new roman","25"))
                a14.place(x=400,y=150)
                lab17=Label(obj3,bg="black",fg="white",text="Enter password ",font=("times new roman","25"))
                lab17.place(x=80,y=200)
                a15=Entry(obj3,font=("times new roman","25"))
                a15.place(x=400,y=200)
            lab3=Label(obj1,bg="yellow",fg="black",text="Your Email'id is Verified.................",font=("times new roman","55"))
            lab3.place(x=250,y=50)
            def login_bank():  # create form for direct login to your Bank Account.
                objj=Tk()
                objj.geometry("2000x900")
                objj.config(bg="PaleGreen1")
                objj.title(" LOGIN_(Tushar Nagar)")
                lb=Label(objj,bg="yellow",fg="black",text="Please Enter Your Username And Password",font=("times new roman","35"))
                lb.place(x=150,y=50)
                lb3=Label(objj,bg="black",fg="white",text="Enter Username Name     ",font=("times new roman","25"))
                lb3.place(x=250,y=150)
                a11=Entry(objj,font=("times new roman","25"))
                a11.place(x=650,y=150)
                lb4=Label(objj,bg="black",fg="white",text="Enter Username Customer'Id",font=("times new roman","25"))
                lb4.place(x=250,y=200)
                a12=Entry(objj,font=("times new roman","25"))
                a12.place(x=650,y=200)
                lb5=Label(objj,bg="black",fg="white",text="Enter Username Password",font=("times new roman","25"))
                lb5.place(x=250,y=250)
                a13=Entry(objj,font=("times new roman","25"))
                a13.place(x=650,y=250)
                rdm=randint(500,9000)
                lb5e1=Label(objj,bg="silver",fg="black",text="Capture",font=("times new roman","20"))
                lb5e1.place(x=380,y=350)
                lb5e=Label(objj,bg="skyblue",fg="black",text=rdm,font=("times new roman","20"))
                lb5e.place(x=500,y=350)
                a13e=Entry(objj,font=("times new roman","20"))
                a13e.place(x=400,y=300)
                def chk11():   # Create Form for Show Customer Detail.
                    objct12=Tk()
                    objct12.geometry("2000x900")
                    objct12.config(bg="PaleGreen1")
                    objct12.title("Account detail_(Tushar Nagar)")
                    cur=con.cursor()
                    customer=a12.get()
                    cur.execute("SELECT * FROM studenttable where customer_id=%s",(customer,))
                    data=cur.fetchone()
                    if not data:
                        lb41=Label(objct12,bg="black",fg="white",text="These Customer may not be present",font=("times new roman","65"))
                        lb41.place(x=250,y=400)
                    else:
                        n=data[0]
                        c=data[1]
                        a=data[2]
                        b=data[3]
                        d=data[4]
                        t=data[5]
                        n1=data[6]
                        m=data[7]
                        p=data[8]
                        lb4111=Label(objct12,bg="yellow",fg="black",text="Customer Bank Account detail",font=("times new roman","35"))
                        lb4111.place(x=60,y=80)
                        lb411=Label(objct12,bg="yellow",fg="black",text="Name of Customer",font=("times new roman","25"))
                        lb411.place(x=100,y=200)
                        lb412=Label(objct12,bg="skyblue",fg="black",text=n,font=("times new roman","25"))
                        lb412.place(x=700,y=200)
                        lb413=Label(objct12,bg="yellow",fg="black",text="Customer account no.",font=("times new roman","25"))
                        lb413.place(x=100,y=250)
                        lb414=Label(objct12,bg="skyblue",fg="black",text=c,font=("times new roman","25"))
                        lb414.place(x=700,y=250)
                        lb415=Label(objct12,bg="yellow",fg="black",text="Customer Amount",font=("times new roman","25"))
                        lb415.place(x=100,y=300)
                        lb416=Label(objct12,bg="skyblue",fg="black",text=a,font=("times new roman","25"))
                        lb416.place(x=700,y=300)
                        lb415=Label(objct12,bg="yellow",fg="black",text="Loan Amount",font=("times new roman","25"))
                        lb415.place(x=100,y=350)
                        lb416=Label(objct12,bg="skyblue",fg="black",text=b,font=("times new roman","25"))
                        lb416.place(x=700,y=350) 
                        lb415=Label(objct12,bg="yellow",fg="black",text="Customer Password",font=("times new roman","25"))
                        lb415.place(x=100,y=400)
                        lb416=Label(objct12,bg="skyblue",fg="black",text=d,font=("times new roman","25"))
                        lb416.place(x=700,y=400)
                        lb415=Label(objct12,bg="yellow",fg="black",text="Last date you have transfer Amount",font=("times new roman","25"))
                        lb415.place(x=100,y=450)
                        lb416=Label(objct12,bg="skyblue",fg="black",text=t,font=("times new roman","25"))
                        lb416.place(x=700,y=450)
                        lb415=Label(objct12,bg="yellow",fg="black",text="Last date you have Loan Amount",font=("times new roman","25"))
                        lb415.place(x=100,y=500)
                        lb416=Label(objct12,bg="skyblue",fg="black",text=n1,font=("times new roman","25"))
                        lb416.place(x=700,y=500)
                        lb415=Label(objct12,bg="yellow",fg="black",text="Last date you have deposite Amount",font=("times new roman","25"))
                        lb415.place(x=100,y=550)
                        lb416=Label(objct12,bg="skyblue",fg="black",text=m,font=("times new roman","25"))
                        lb416.place(x=700,y=550)
                        lb415=Label(objct12,bg="yellow",fg="black",text="Last date you have withdraw Amount",font=("times new roman","25"))
                        lb415.place(x=100,y=600)
                        lb416=Label(objct12,bg="skyblue",fg="black",text=p,font=("times new roman","25"))
                        lb416.place(x=700,y=600)
                        def rfqq():
                            objct12.destroy()
                        bt12=Button(objct12,bg="blue",fg="black",text="back",font=("times new roman","30"),command=rfqq)
                        bt12.place(x=550,y=650)
                def chk1():  # Create Form For Transfer Amount
                    objct1=Tk()
                    objct1.geometry("2000x900")
                    objct1.config(bg="PaleGreen1")
                    objct1.title("OK_(Tushar Nagar)")
                    lb=Label(objct1,bg="yellow",fg="black",text="Please Enter detail customer'id from & customer'id To also enter amount for Transfer",font=("times new roman","35"))
                    lb.place(x=100,y=50)
                    lab711=Label(objct1,bg="black",fg="white",text="Enter your User_id From...  ",font=("times new roman","30"))
                    lab711.place(x=120,y=150)
                    a51=Entry(objct1,font=("times new roman","25"))
                    a51.place(x=700,y=150)
                    lab71j1=Label(objct1,bg="black",fg="white",text="Enter your Password...  ",font=("times new roman","30"))
                    lab71j1.place(x=120,y=210)
                    a51kk=Entry(objct1,font=("times new roman","25"))
                    a51kk.place(x=700,y=210)
                    lab712=Label(objct1,bg="black",fg="white",text="Enter User_id To ...  ",font=("times new roman","30"))
                    lab712.place(x=120,y=270)
                    a512=Entry(objct1,font=("times new roman","25"))
                    a512.place(x=700,y=270)
                    lab72=Label(objct1,bg="black",fg="white",text="Enter User_id To conform...   ",font=("times new roman","30"))
                    lab72.place(x=120,y=330)
                    a5j1=Entry(objct1,font=("times new roman","25"))
                    a5j1.place(x=700,y=330)
                    lab81=Label(objct1,bg="black",fg="white",text="Select Bank user'id To... ",font=("times new roman","30"))
                    lab81.place(x=120,y=390)
                    mb=Menubutton(objct1,text="select your Bank")
                    mb.place(x=700,y=390)
                    mb.menu=Menu(mb)
                    mb["menu"]=mb.menu
                    s=StringVar()
                    h=StringVar()
                    a=StringVar()
                    mb.menu.add_checkbutton(label="SBI",variable=s)
                    mb.menu.add_checkbutton(label="HDFC",variable=h)
                    mb.menu.add_checkbutton(label="Axis",variable=a)
                    mb.place(x=700,y=390)
                    lab81=Label(objct1,bg="black",fg="white",text="Enter amount for send... ",font=("times new roman","30"))
                    lab81.place(x=120,y=450)
                    a61=Entry(objct1,font=("times new roman","25"))
                    a61.place(x=700,y=450)
                    def chck21():   #  Transfer amount to another Account
                        cur=con.cursor()
                        customer=a512.get()##Receiver
                        customer_owner=a12.get()##Sender
                        if a5j1.get()!=a512.get() :
                            lb421=Label(objct1,bg="yellow",fg="black",text="Please enter correct user'id To",font=("times new roman","25"))
                            lb421.place(x=250,y=510)
                        elif customer_owner!=a51.get():
                            lb41=Label(objct1,bg="black",fg="white",text="Please enter correct user'id From",font=("times new roman","25"))
                            lb41.place(x=250,y=570)
                        else:
                            cur.execute("SELECT * FROM studenttable where customer_id=%s",(customer,))
                            data=cur.fetchone()
                            cur.execute("SELECT * FROM studenttable where customer_id=%s",(customer_owner,))
                            datas=cur.fetchone()
                            if datas[4]!=a51kk.get():
                                lb419=Label(objct1,bg="black",fg="white",text="Please enter correct Password From",font=("times new roman","25"))
                                lb419.place(x=350,y=700)
                            else:
                                if not data:
                                    lb41=Label(objct1,bg="skyblue",fg="black",text="These Customer may not be present",font=("times new roman","25"))
                                    lb41.place(x=700,y=520)
                                else:
                                    k=int(data[2])##receiver amount
                                    l=int(datas[2])##sender amount
                                    n=int(a61.get())##send amount
                                    objk=Tk()
                                    objk.geometry("2000x900")
                                    objk.config(bg="PaleGreen1")
                                    objk.title("Finally WebPage")
                                    lab81=Label(objk,bg="yellow",fg="black",text="Click here to Transfer the Amount",font=("times new roman","65"))
                                    lab81.place(x=100,y=80)
                                    def chck31(): # Create Form to show final message send Amount to another account 
                                        lab81=Label(objk,bg="yellow",fg="black",text="Your Transfer the Amount is Successfull",font=("times new roman","35"))
                                        lab81.place(x=250,y=450)
                                    bt12=Button(objk,bg="red",fg="white",text="transfer Amount",font=("times new roman","45"),command=chck31)
                                    bt12.place(x=500,y=250)
                                    if l>=n:
                                        cur=con.cursor()
                                        sums=k+n
                                        minus=l-n
                                        amount=str(sums)
                                        amount1=str(minus)
                                        cur.execute("update studenttable set Balance=%s where customer_id=%s ",(amount,a512.get()))
                                        #con.commit()
                                        cur.execute("update studenttable set Balance=%s where customer_id=%s ",(amount1,a12.get()))
                                        cur.execute("update studenttable set time_transfer=%s where customer_id=%s ",(localtime,a12.get()))
                                        con.commit()
                                    else:
                                        lab811=Label(objk,bg="PaleGreen1",fg="PaleGreen1",text="______________________________________________________",font=("times new roman","65"))
                                        lab811.place(x=100,y=80)
                                        lab8121=Label(objk,bg="yellow",fg="black",text="Your have not those enter amount in your account ..........",font=("times new roman","50"))
                                        lab8121.place(x=50,y=254)
                    bt12=Button(objct1,bg="red",fg="white",text="Transfer",font=("times new roman","30"),command=chck21)
                    bt12.place(x=300,y=600)
                    def rf():
                        objct1.destroy()
                        chk1()
                    bt12=Button(objct1,bg="red",fg="white",text="Refresh",font=("times new roman","30"),command=rf)
                    bt12.place(x=550,y=600)
                    def rf12():
                        objct1.destroy()         
                    bt12=Button(objct1,bg="red",fg="white",text="back",font=("times new roman","30"),command=rf12)
                    bt12.place(x=720,y=600)
                def check1(): # Create Form for finally Verify your data through database.
                    cur=con.cursor()
                    customer_id=a12.get()
                    cur.execute("SELECT * FROM studenttable where customer_id=%s",(customer_id,)) 
                    if len(a13e.get())==0:
                        val1=0
                    else:
                        val1=int(a13e.get())
                    data=cur.fetchone()
                    cust_name=a11.get()
                    pwd=a13.get()
                    flag=False
                    flag_for_id=True
                    flag_for_pwd=False
                    if not data:
                        lb41=Label(objj,bg="yellow",fg="black",text="please enter correct User'id",font=("times new roman","30"))
                        lb41.place(x=250,y=600)
                        flag_for_id=False
                    elif data[0]==cust_name and data[4]==pwd:
                        flag=True
                        flag_for_pwd=True
                    elif data[0]==cust_name:
                        flag=True
                    elif data[4]==pwd:
                        flag_for_pwd=True
                    if flag==False and flag_for_pwd==False:
                       lb41=Label(objj,bg="yellow",fg="black",text="please enter correct User Name and Password",font=("times new roman","30"))
                       lb41.place(x=250,y=700)
                    elif flag==False:
                        lb41=Label(objj,bg="yellow",fg="black",text="please enter correct User Name",font=("times new roman","30"))
                        lb41.place(x=250,y=700)
                    elif flag_for_pwd==False:
                        lb41=Label(objj,bg="yellow",fg="black",text="please enter correct User Password",font=("times new roman","30"))
                        lb41.place(x=250,y=700)
                    elif val1==0:
                        lb41=Label(objj,bg="yellow",fg="black",text="please enter Capture_ value :- ",font=("times new roman","30"))
                        lb41.place(x=250,y=700)
                    elif val1!=rdm:
                        lb41=Label(objj,bg="yellow",fg="black",text="please enter correct Capture_ value :- ",font=("times new roman","30"))
                        lb41.place(x=250,y=700)
                    else:
                        if flag_for_id==False:
                            lb41=Label(objj,bg="red",fg="white",text="Please enter valid customer'id",font=("times new roman","55"))
                            lb41.place(x=200,y=800)
                        else:
                            objct=Tk()
                            objct.geometry("2000x900")
                            objct.config(bg="PaleGreen1")
                            objct.title("Successfully Registered_(Tushar Nagar)      ")
                            lbk=Label(objct,bg="yellow",fg="black",text="You Have Successfully Verified your Name and Customer_ID",font=("times new roman","40"))
                            lbk.place(x=50,y=100)
                            lbk1=Label(objct,bg="skyblue",fg="black",text="Please click here for Transfer amount",font=("times new roman","30"))
                            lbk1.place(x=120,y=250)
                            bt11=Button(objct,bg="red",fg="white",text="Transfer",font=("times new roman","20"),command=chk1)
                            bt11.place(x=700,y=250)
                            lbk2=Label(objct,bg="skyblue",fg="black",text="Please click here for Account detail",font=("times new roman","30"))
                            lbk2.place(x=120,y=310)
                            bt12=Button(objct,bg="red",fg="white",text="Account detail",font=("times new roman","20"),command=chk11)
                            bt12.place(x=700,y=310)
                            lbk3=Label(objct,bg="skyblue",fg="black",text="Fill Application Form for Loan",font=("times new roman","30"))
                            lbk3.place(x=120,y=370)
                            bt13=Button(objct,bg="red",fg="white",text="Loan",font=("times new roman","20"),command=chk111)
                            bt13.place(x=700,y=370)
                            def deposite(): # Create Form for deposite your Amount in your Account
                                objcte=Tk()
                                objcte.geometry("2000x900")
                                objcte.config(bg="PaleGreen1")
                                objcte.title("Deposite Amount_(Tushar Nagar)")
                                lb7=Label(objcte,bg="yellow",fg="black",text="Please Enter Your Username And Password",font=("times new roman","35"))
                                lb7.place(x=150,y=50)
                                lb37=Label(objcte,bg="black",fg="white",text="Enter Username Name     ",font=("times new roman","25"))
                                lb37.place(x=250,y=150)
                                a117=Entry(objcte,font=("times new roman","25"))
                                a117.place(x=700,y=150)
                                lb47=Label(objcte,bg="black",fg="white",text="Enter Username Customer'Id",font=("times new roman","25"))
                                lb47.place(x=250,y=200)
                                a127=Entry(objcte,font=("times new roman","25"))
                                a127.place(x=700,y=200)
                                lb57=Label(objcte,bg="black",fg="white",text="Enter Username Password",font=("times new roman","25"))
                                lb57.place(x=250,y=250)
                                a137=Entry(objcte,font=("times new roman","25"))
                                a137.place(x=700,y=250)
                                lbk=Label(objcte,bg="black",fg="white",text="Enter amount to deposite",font=("times new roman","25"))
                                lbk.place(x=250,y=300)
                                a511=Entry(objcte,font=("times new roman","25"))
                                a511.place(x=700,y=300)
                                def dep(): # Create Form for show Message your amount is deposite or not
                                    l=a127.get() #customer 'id to deposite
                                    en=a511.get()#Enter new amount to deposite
                                    cur=con.cursor()
                                    cur.execute("SELECT * FROM studenttable where customer_id=%s",(l,))
                                    data=cur.fetchone()
                                    l=len(a511.get())
                                    if not data:
                                        lbk=Label(objcte,bg="black",fg="white",text="Please Enter Correct user'id ",font=("times new roman","40"))
                                        lbk.place(x=80,y=500)
                                    elif data[0]!=a117.get() and data[4]!=a137.get():
                                        lbk=Label(objcte,bg="black",fg="white",text="Please Enter Correct user'name and Password",font=("times new roman","40"))
                                        lbk.place(x=80,y=600)
                                    elif data[0]!=a117.get():
                                        lbk=Label(objcte,bg="black",fg="white",text="Please Enter Correct user'name ",font=("times new roman","40"))
                                        lbk.place(x=80,y=600)
                                    elif data[4]!=a137.get():
                                        lbk=Label(objcte,bg="black",fg="white",text="Please Enter Correct user'Password ",font=("times new roman","40"))
                                        lbk.place(x=80,y=600)
                                    elif l==0:
                                        lbk=Label(objcte,bg="black",fg="white",text="Please Enter valid amount ",font=("times new roman","40"))
                                        lbk.place(x=80,y=600)
                                    else:                                    
                                        w=int(data[2])
                                        a1=int(a511.get())
                                        b1=a1+w
                                        sum21=str(b1)
                                        cur.execute("update studenttable set time_deposite=%s where customer_id=%s ",(localtime,a12.get()))
                                        cur.execute("update studenttable set Balance=%s where customer_id=%s ",(sum21,a12.get()))
                                        con.commit()
                                        lbk113=Label(objcte,bg="skyblue",fg="black",text="Your deposite amount is submitted",font=("times new roman","30"))
                                        lbk113.place(x=120,y=580)
                                bt132=Button(objcte,bg="red",fg="white",text="deposite",font=("times new roman","20"),command=dep)
                                bt132.place(x=200,y=400)
                                def bk():
                                    objcte.destroy()
                                def bkjj():
                                    objcte.destroy()
                                    deposite()
                                bt131=Button(objcte,bg="red",fg="white",text="back",font=("times new roman","20"),command=bk)
                                bt131.place(x=500,y=400)
                                bt131=Button(objcte,bg="red",fg="white",text="Refresh",font=("times new roman","20"),command=bkjj)
                                bt131.place(x=350,y=400)
                            lbk3=Label(objct,bg="skyblue",fg="black",text="Please click here for Deposit data",font=("times new roman","30"))
                            lbk3.place(x=120,y=430)
                            bt13=Button(objct,bg="red",fg="white",text="deposite",font=("times new roman","20"),command=deposite)
                            bt13.place(x=700,y=430)
                            lbk3=Label(objct,bg="skyblue",fg="black",text="Please click here to Check Balance",font=("times new roman","30"))
                            lbk3.place(x=120,y=490)
                            def blneck(): # Create form for Show Message your current Account Balance through database
                                objcte1=Tk()
                                objcte1.geometry("2000x900")
                                objcte1.config(bg="PaleGreen1")
                                objcte1.title("Current Amount_(Tushar Nagar)")
                                lb1k=Label(objcte1,bg="yellow",fg="black",text="Bank Account Balance detail ",font=("times new roman","60"))
                                lb1k.place(x=50,y=100)
                                lbk=Label(objcte1,bg="yellow",fg="black",text="Your current Account Balance: ",font=("times new roman","25"))
                                lbk.place(x=80,y=250)
                                cur=con.cursor()
                                m=a12.get()
                                cur.execute("SELECT * FROM studenttable where customer_id=%s",(m,))
                                data=cur.fetchone()
                                blnc=data[2]
                                lbk=Label(objcte1,bg="skyblue",fg="black",text=blnc,font=("times new roman","25"))
                                lbk.place(x=500,y=250)
                                def bky():
                                    objcte1.destroy()
                                bt13=Button(objcte1,bg="red",fg="white",text="back",font=("times new roman","20"),command=bky)
                                bt13.place(x=100,y=400)
                            bt13=Button(objct,bg="red",fg="white",text="Check Balance",font=("times new roman","20"),command=blneck)
                            bt13.place(x=700,y=490)
                            def wthdrw(): # Create Form for deposite your Amount in your Account
                                objtw=Tk()
                                objtw.geometry("2000x900")
                                objtw.config(bg="PaleGreen1")
                                objtw.title("Deposite Amount_(Tushar Nagar)")
                                lb7=Label(objtw,bg="yellow",fg="black",text="Please Enter Your Username And Password",font=("times new roman","35"))
                                lb7.place(x=150,y=50)
                                lb37=Label(objtw,bg="black",fg="white",text="Enter Username Name     ",font=("times new roman","25"))
                                lb37.place(x=250,y=150)
                                a1171=Entry(objtw,font=("times new roman","25"))
                                a1171.place(x=700,y=150)
                                lb47=Label(objtw,bg="black",fg="white",text="Enter Username Customer'Id",font=("times new roman","25"))
                                lb47.place(x=250,y=200)
                                a1271=Entry(objtw,font=("times new roman","25"))
                                a1271.place(x=700,y=200)
                                lb57=Label(objtw,bg="black",fg="white",text="Enter Username Password",font=("times new roman","25"))
                                lb57.place(x=250,y=250)
                                a1371=Entry(objtw,font=("times new roman","25"))
                                a1371.place(x=700,y=250)
                                lbk=Label(objtw,bg="black",fg="white",text="Enter amount to withdraw",font=("times new roman","25"))
                                lbk.place(x=250,y=300)
                                a511=Entry(objtw,font=("times new roman","25"))
                                a511.place(x=700,y=300)
                                def wdr(): # Create Form for show Message your amount is deposite or not
                                    l1=a1271.get() #customer 'id to deposite
                                    cur=con.cursor()
                                    cur.execute("SELECT * FROM studenttable where customer_id=%s",(l1,))
                                    data1=cur.fetchone()
                                    l=len(a511.get())
                                    if not data1:
                                        lbk=Label(objtw,bg="yellow",fg="black",text="Please Enter Correct user'id ",font=("times new roman","20"))
                                        lbk.place(x=80,y=500)
                                    elif data1[0]!=a1171.get() and data1[4]!=a1371.get() and l==0:
                                        lbk=Label(objtw,bg="yellow",fg="black",text="Please Enter Correct user'name ,password , amount",font=("times new roman","20"))
                                        lbk.place(x=80,y=600)
                                    elif data1[0]!=a1171.get():
                                        lbk=Label(objtw,bg="yellow",fg="black",text="Please Enter Correct user'name ",font=("times new roman","20"))
                                        lbk.place(x=80,y=600)
                                    elif data1[4]!=a1371.get():
                                        lbk=Label(objtw,bg="yellow",fg="black",text="Please Enter Correct user'Password ",font=("times new roman","20"))
                                        lbk.place(x=80,y=650)
                                    elif l==0:
                                        lbk=Label(objtw,bg="yellow",fg="black",text="Please Enter valid amount ",font=("times new roman","20"))
                                        lbk.place(x=80,y=700)
                                    else:                                    
                                        w1=int(data1[2])
                                        a12=int(a511.get())
                                        if a12>w1:
                                            lbk=Label(objtw,bg="black",fg="white",text="These Amount are not in your account for withdraw ",font=("times new roman","40"))
                                            lbk.place(x=80,y=600)
                                        else:
                                            b12=w1-a12
                                            sum21q=str(b12)
                                            cur.execute("update studenttable set time_withdraw=%s where customer_id=%s ",(localtime,a1271.get()))
                                            cur.execute("update studenttable set Balance=%s where customer_id=%s ",(sum21q,a1271.get()))
                                            con.commit()
                                            lbk113=Label(objtw,bg="skyblue",fg="black",text="Your have withdrawed amount",font=("times new roman","30"))
                                            lbk113.place(x=400,y=480)
                                bt13s=Button(objtw,bg="red",fg="white",text="Withdraw",font=("times new roman","20"),command=wdr)
                                bt13s.place(x=300,y=400)
                                def rw():
                                    objtw.destroy()
                                    wthdrw()
                                def bk3():
                                    objtw.destroy()
                                bt13s=Button(objtw,bg="red",fg="white",text="Refresh",font=("times new roman","20"),command=rw)
                                bt13s.place(x=450,y=400)
                                bt13q=Button(objtw,bg="red",fg="white",text="back",font=("times new roman","20"),command=bk3)
                                bt13q.place(x=600,y=400)
                            lbk3s=Label(objct,bg="skyblue",fg="black",text="Please click here Withdraw amount",font=("times new roman","30"))
                            lbk3s.place(x=120,y=550)
                            bt13s=Button(objct,bg="red",fg="white",text="Withdraw",font=("times new roman","20"),command=wthdrw)
                            bt13s.place(x=700,y=550)
                            bt13w=Button(objct,bg="red",fg="white",text="Logout",font=("times new roman","25"),command=login_bank)
                            bt13w.place(x=400,y=630)
                btn11=Button(objj,bg="blue",fg="white",text="Login",font=("times new roman","30"),command=check1)
                btn11.place(x=350,y=450)
                def ok():
                    objj.destroy()
                    login_bank()
                btn113=Button(objj,bg="blue",fg="white",text="Refresh",font=("times new roman","20"),command=ok)
                btn113.place(x=550,y=460)
                def updt_pwd():
                    objj1=Tk()
                    objj1.geometry("2000x900")
                    objj1.config(bg="PaleGreen1")
                    objj1.title(" Update Password_(Tushar Nagar)")
                    lb1=Label(objj1,bg="yellow",fg="black",text="Please Enter Your User'id and user password for Updating the password",font=("times new roman","35"))
                    lb1.place(x=100,y=50)
                    lb31=Label(objj1,bg="black",fg="white",text="Enter User Name     ",font=("times new roman","25"))
                    lb31.place(x=250,y=150)
                    a11=Entry(objj1,font=("times new roman","25"))
                    a11.place(x=700,y=150)
                    lb41=Label(objj1,bg="black",fg="white",text="Enter User Customer'Id",font=("times new roman","25"))
                    lb41.place(x=250,y=200)
                    a121=Entry(objj1,font=("times new roman","25"))
                    a121.place(x=700,y=200)
                    lb5=Label(objj1,bg="black",fg="white",text="Enter User NewPassword",font=("times new roman","25"))
                    lb5.place(x=250,y=250)
                    a131=Entry(objj1,font=("times new roman","25"))
                    a131.place(x=700,y=250)
                    def pwt_updt_mql():
                        cur1=con.cursor()
                        customer_id1=a121.get()
                        cut_nm=a11.get()
                        cur1.execute("SELECT * FROM studenttable where customer_id=%s",(customer_id1,))
                        data1=cur1.fetchone()
                        flg_id=True
                        npwd=a131.get()
                        lm=len(npwd)
                        flg_pw=True
                        if lm==0:
                            flg_pw=False
                        if not data1:
                            lb41=Label(objj1,bg="yellow",fg="black",text="please enter correct User'id ,user password and user name",font=("times new roman","30"))
                            lb41.place(x=250,y=500)
                        elif lm==0 and cut_nm!=data1[0]:
                            lb41=Label(objj1,bg="yellow",fg="black",text="please enter Valid Password and name",font=("times new roman","30"))
                            lb41.place(x=250,y=550)
                        elif lm==0:
                            lb41=Label(objj1,bg="yellow",fg="black",text="please enter Valid Password",font=("times new roman","30"))
                            lb41.place(x=250,y=600)
                        elif cut_nm!=data1[0]:
                            lb41=Label(objj1,bg="yellow",fg="black",text="please enter Valid UserName",font=("times new roman","30"))
                            lb41.place(x=250,y=650)                            
                        elif cut_nm==data1[0]:
                            if flg_pw==True:
                                cur1.execute("update studenttable set password=%s where customer_id=%s ",(a131.get(),customer_id1))
                                con.commit()
                                lb41=Label(objj1,bg="yellow",fg="black",text="Your Password is Succesfully Update",font=("times new roman","30"))
                                lb41.place(x=250,y=700)
                            else:
                                lb41=Label(objj1,bg="yellow",fg="black",text="please enter Valid Password",font=("times new roman","30"))
                                lb41.place(x=250,y=700)
                    btn115=Button(objj1,bg="blue",fg="white",text="Submit",font=("times new roman","20"),command=pwt_updt_mql)
                    btn115.place(x=250,y=400)
                    def ref_():
                        objj1.destroy()
                        updt_pwd()
                    btn115=Button(objj1,bg="blue",fg="white",text="Refresh_",font=("times new roman","20"),command=ref_)
                    btn115.place(x=450,y=400)
                    def bk_():
                        objj1.destroy()
                        login_bank()
                    btn115=Button(objj1,bg="blue",fg="white",text="back",font=("times new roman","20"),command=bk_)
                    btn115.place(x=650,y=400)
                btn114=Button(objj,bg="blue",fg="white",text="Forget Password",font=("times new roman","20"),command=updt_pwd)
                btn114.place(x=700,y=450)
                def gth1():
                    objj.destroy()
                    mylogin()
                btn12=Button(objj,bg="blue",fg="white",text="back",font=("times new roman","20"),command=gth1)
                btn12.place(x=450,y=550)
            lb3=Label(obj1,bg="yellow",fg="black",text="If You Have Already your Bank Account",font=("times new roman","25"))
            lb3.place(x=350,y=300)
            btn=Button(obj1,bg="red",fg="white",text="Click Here",font=("times new roman","30"),command=login_bank)
            btn.place(x=350,y=350)
            lb4=Label(obj1,bg="yellow",fg="black",text="If You Want to Create Bank Account",font=("times new roman","25"))
            lb4.place(x=350,y=480)
            btn12=Button(obj1,bg="red",fg="white",text="Click Here",font=("times new roman","30"),command=createAccount)
            btn12.place(x=350,y=530)
            def gth():
                obj1.destroy()
                obj.destroy()
            btn12=Button(obj1,bg="blue",fg="white",text="go to home page",font=("times new roman","20"),command=gth)
            btn12.place(x=450,y=200)
        else:
            objk1=Tk()
            objk1.geometry("2000x900")
            objk1.title("HOME PAGE_(Tushar Nagar)");
            objk1.config(bg="PaleGreen1")
            lab3=Label(objk1,bg="yellow",fg="black",text="Please Try Again Your Password or username is Wrong",font=("times new roman","45"))
            lab3.place(x=150,y=50)
            objk1.config(bg="red2")
            btn=Button(objk1,bg="green",fg="white",text="Click here to try again",font=("times new roman","35"),command=login)
            btn.place(x=550,y=350)
    btn1=Button(obj,bg="red",fg="white",text="Login",font=("times new roman","30"),command=mylogin)
    btn1.place(x=350,y=450)
    def rfs():
        obj.destroy()
        login()
    btn12=Button(obj,bg="blue",fg="white",text="Refresh",font=("times new roman","20"),command=rfs)
    btn12.place(x=650,y=450)
btn=Button(t,bg="blue",fg="white",text="      SBI     ",font=("times new roman","25"),command=login)
btn.place(x=500,y=250)
btn=Button(t,bg="blue4",fg="white",text="     HDFC   ",font=("times new roman","25"),command=login)
btn.place(x=500,y=350)
btn=Button(t,bg="red",fg="white",text="     AXIS     ",font=("times new roman","25"),command=login)
btn.place(x=500,y=450)
def ext():
    t.destroy()
btn=Button(t,bg="blue",fg="white",text="exit",font=("times new roman","20"),command=ext)
btn.place(x=200,y=550)




