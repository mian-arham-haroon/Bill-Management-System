from tkinter import *


root=Tk()
root.title("Bill Management")
root.geometry("1000x500")
# root.configure
root.resizable(False,False)

def Reset ():
    entry_roti.delete(0,END)
    entry_cookies.delete(0,END)
    entry_tea.delete(0,END)
    entry_coffies.delete(0,END)
    entry_juice.delete(0,END)
    entry_pancakes.delete(0,END)
    entry_egg.delete(0,END)

def Total ():
    try:a1=int(roti.get())
    except:a1=0
    try:a2=int(cookies.get())
    except:a2=0
    try:a3=int(tea.get())
    except:a3=0
    try:a4=int(coffies.get())
    except:a4=0
    try:a5=int(juice.get())
    except:a5=0
    try:a6=int(pancakes.get())
    except:a6=0
    try:a7=int(egg.get())
    except:a7=0

#define the cost of each item
    c1=15*a1
    c2=30*a2
    c3=60*a3
    c4=150*a4
    c5=100*a5
    c6=50*a6
    c7=20*a7
    
    lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f'%totalcost)  #we also write for single zero desimal so simple write the totalcost
    Total_bill.set(string_bill)

Label(text="Bill Management",bg="black",font=("calibri",33),fg="white",width="300",height="2").pack()

#menu card
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness="1",width="300",height="370")
f.place(x=10,y=118)

Label(f,text="Menu",font=("gabriola",40,"bold"),fg="black",background="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,"bold"),text="Roti.......Rs.15/Plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cookies.......Rs.30/Plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Tea.......Rs.60/Cup",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="coffee.......Rs.150/Cup",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Juice.......Rs.100/Glass",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Pancakes.....Rs.50/Pack",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Egg.......Rs.20/single",fg="black",bg="lightgreen").place(x=10,y=260)

#bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("calibri",20),bg="lightyellow")
Bill.place(x=120,y=10)
#entry work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

roti=StringVar()
cookies=StringVar()
tea=StringVar()
coffies=StringVar()
juice=StringVar()
pancakes=StringVar()
egg=StringVar()
Total_bill=StringVar()

#label
lbl_roti=Label(f1,font=("arial",20,"bold"),text="Roti",width=12,fg="blue4")
lbl_roti.grid(row=1,column=0)
lbl_cookies=Label(f1,font=("arial",20,"bold"),text="Cookies",width=12,fg="blue4")
lbl_cookies.grid(row=2,column=0)
lbl_tea=Label(f1,font=("arial",20,"bold"),text="Tea",width=12,fg="blue4")
lbl_tea.grid(row=3,column=0)
lbl_coffies=Label(f1,font=("arial",20,"bold"),text="Coffee",width=12,fg="blue4")
lbl_coffies.grid(row=4,column=0)
lbl_juice=Label(f1,font=("arial",20,"bold"),text="Juice",width=12,fg="blue4")
lbl_juice.grid(row=5,column=0)
lbl_pancakes=Label(f1,font=("arial",20,"bold"),text="Pancakes",width=12,fg="blue4")
lbl_pancakes.grid(row=6,column=0)
lbl_egg=Label(f1,font=("arial",20,"bold"),text="Egg",width=12,fg="blue4")
lbl_egg.grid(row=7,column=0)

#entry
entry_roti=Entry(f1,font=("arial",20,"bold"),textvariable=roti,bd=6,width=8,bg="lightpink")
entry_roti.grid(row=1,column=1)
entry_cookies=Entry(f1,font=("arial",20,"bold"),textvariable=cookies,bd=6,width=8,bg="lightpink")
entry_cookies.grid(row=2,column=1)
entry_tea=Entry(f1,font=("arial",20,"bold"),textvariable=tea,bd=6,width=8,bg="lightpink")
entry_tea.grid(row=3,column=1)
entry_coffies=Entry(f1,font=("arial",20,"bold"),textvariable=coffies,bd=6,width=8,bg="lightpink")
entry_coffies.grid(row=4,column=1)
entry_juice=Entry(f1,font=("arial",20,"bold"),textvariable=juice,bd=6,width=8,bg="lightpink")
entry_juice.grid(row=5,column=1)
entry_pancakes=Entry(f1,font=("arial",20,"bold"),textvariable=pancakes,bd=6,width=8,bg="lightpink")
entry_pancakes.grid(row=6,column=1)
entry_egg=Entry(f1,font=("arial",20,"bold"),textvariable=egg,bd=6,width=8,bg="lightpink")
entry_egg.grid(row=7,column=1)


#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)
btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)


root.mainloop()