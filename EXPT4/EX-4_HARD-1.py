import tkinter as tk 
from tkinter import ttk
set1=tk.Tk()
set1.geometry('870x800')
set1.configure(background="SlateBlue2")
set1.title('Student Registration Form')

l1=tk.Label(set1,text="  First Name",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=0,column=0)
t=tk.Entry(set1,width=27).grid(row=0,column=1,pady=10)
q1=tk.Label(set1,text="(max 30 characters a-z and A-z)",bg='SlateBlue2',fg='white').grid(row=0,column=2)
l2=tk.Label(set1,text="  Last Name",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=1,column=0)
t1=tk.Entry(set1,width=27).grid(row=1,column=1,pady=10)
q2=tk.Label(set1,text="(max 30 characters a-z and A-z)",bg='SlateBlue2',fg='white').grid(row=1,column=2)


l4=tk.Label(set1,text="  Date Of Birth",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=2,column=0)


n= tk.StringVar()
j=ttk.Combobox(set1, width = 5,text="Month",textvariable = n )
j['values'] = (' January',  ' February', ' March', ' April', ' May', ' June', ' July', ' August', ' September', ' October', ' November', ' December')
j.grid(row=2,column=1,sticky=tk.W,pady=10)
n1= tk.StringVar()
j1=ttk.Combobox(set1, width = 3,text="Day",textvariable = n1)
j1['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
j1.grid(row=2,column=1,pady=10)
n2= tk.StringVar()
j2=ttk.Combobox(set1, width = 5,text="Year",textvariable = n2)
j2['values'] = (1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009)
j2.grid(row=2,column=1,sticky=tk.E,pady=10)

l3=tk.Label(set1,text="  Email ID",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=3,column=0)
t2=tk.Entry(set1,width=27).grid(row=3,column=1,pady=10)

l5=tk.Label(set1,text="  Mobile Number",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=4,column=0)
t3=tk.Entry(set1,width=27).grid(row=4,column=1,pady=10)
q3=tk.Label(set1,text="(10 digit number)",bg='SlateBlue2',fg='white').grid(row=4,column=2,sticky=tk.W)

l6=tk.Label(set1,text="  Gender",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=5,column=0)
rb=tk.Radiobutton(set1,text='Male',value=1,bg="SlateBlue2",fg='white',width=20,anchor=tk.W).grid(row=5,column=1,pady=10)
rb1=tk.Radiobutton(set1,text='Female',value=2,bg="SlateBlue2",fg='white',width=20,anchor=tk.W).grid(row=5,column=2,pady=10)

l7=tk.Label(set1,text='  Address',bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=7,column=0)
t4=tk.Text(set1,height=5, width=30).grid(row=7,column=1,columnspan=2,sticky=tk.W,pady=10)

l8=tk.Label(set1,text='  City',bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=8,column=0)
t5=tk.Entry(set1,width=27).grid(row=8,column=1,pady=10)
q4=tk.Label(set1,text="(max 30 characters a-z and A-z)",bg='SlateBlue2',fg='white').grid(row=8,column=2)

l9=tk.Label(set1,text="  PIN Code",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=9,column=0)
t6=tk.Entry(set1,width=27).grid(row=9,column=1,pady=10)
q5=tk.Label(set1,text="(6 digit number)",bg='SlateBlue2',fg='white').grid(row=9,column=2,sticky=tk.W)


l10=tk.Label(set1,text="  State",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=10,column=0)
t7=tk.Entry(set1,width=27).grid(row=10,column=1,pady=10)
q6=tk.Label(set1,text="(max 30 characters a-z and A-z)",bg='SlateBlue2',fg='white').grid(row=10,column=2)


l11=tk.Label(set1,text="  Country",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=11,column=0)
t8=tk.Entry(set1,width=27).grid(row=11,column=1,pady=10)



l12=tk.Label(set1,text="  Hobbies",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=12,column=0)
cb1=tk.Checkbutton(set1,text="Drawing",bg='SlateBlue2').grid(row=12,column=1,sticky=tk.W,pady=1)
cb2=tk.Checkbutton(set1,text="Singing",bg='SlateBlue2').grid(row=12,column=1,sticky=tk.E,pady=1)
cb3=tk.Checkbutton(set1,text="Dancing",bg='SlateBlue2').grid(row=12,column=2,sticky=tk.W,pady=1)
cb4=tk.Checkbutton(set1,text="Sketching",bg='SlateBlue2').grid(row=12,column=2,sticky=tk.E,pady=1)
cb5=tk.Checkbutton(set1,text="Other",bg='SlateBlue2').grid(row=13,column=1,sticky=tk.W,pady=10)
t9=tk.Entry(set1,width=27).grid(row=13,column=1,columnspan=2,pady=10) 


l13=tk.Label(set1,text="  Qualification",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=14,column=0)
l14=tk.Label(set1,text="Sl.No.Examination",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=14,column=1)
l15=tk.Label(set1,text="Board",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=14,column=2) 
l16=tk.Label(set1,text="Percentage",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=14,column=3)         
l17=tk.Label(set1,text="Year of Passing",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=14,column=4) 


l18=tk.Label(set1,text="1     Class X",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=15,column=1)
l19=tk.Label(set1,text="2     Class X11",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=16,column=1) 
l20=tk.Label(set1,text="3     Graduation",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=17,column=1)
l21=tk.Label(set1,text="4     Masters",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=18,column=1)   
t10=tk.Entry(set1,width=27).grid(row=15,column=2,pady=6)
t11=tk.Entry(set1,width=27).grid(row=15,column=3,pady=6)
t12=tk.Entry(set1,width=27).grid(row=15,column=4,pady=6)

t13=tk.Entry(set1,width=27).grid(row=16,column=2,pady=6)
t14=tk.Entry(set1,width=27).grid(row=16,column=3,pady=6)
t15=tk.Entry(set1,width=27).grid(row=16,column=4,pady=6)

t16=tk.Entry(set1,width=27).grid(row=17,column=2,pady=6)
t17=tk.Entry(set1,width=27).grid(row=17,column=3,pady=6)
t18=tk.Entry(set1,width=27).grid(row=17,column=4,pady=6)

t19=tk.Entry(set1,width=27).grid(row=18,column=2,pady=6)
t20=tk.Entry(set1,width=27).grid(row=18,column=3,pady=6)
t21=tk.Entry(set1,width=27).grid(row=18,column=4,pady=6)


l22=tk.Label(set1,text="  Courses Applied For",bg='SlateBlue2',fg='white',width=20,anchor=tk.W).grid(row=19,column=0)
cb1=tk.Radiobutton(set1,text="BCA",bg='SlateBlue2').grid(row=19,column=1,sticky=tk.W,pady=6)
cb2=tk.Radiobutton(set1,text="B.Com",bg='SlateBlue2').grid(row=19,column=1,pady=6)
cb3=tk.Radiobutton(set1,text="B.Sc",bg='SlateBlue2').grid(row=19,column=2,sticky=tk.W,pady=6)
cb4=tk.Radiobutton(set1,text="B.A",bg='SlateBlue2').grid(row=19,column=2,pady=6)

      
button=tk.Button(set1,text='Submit',command=set1.destroy).grid(row=20,column=2)
set1.mainloop()