from tkinter import *
from tkinter import messagebox

twelve = Tk()
twelve.title('tk')
twelve.configure(background='lightgrey')
twelve.geometry('500x300')

name = Label(twelve,text="Enter name").grid(row=1,column=1,padx=5,pady=5)
name_in = Entry(twelve,width=30).grid(row=1 ,column=3,padx=5,pady=5)

email = Label(twelve,text="Enter Email").grid(row=2,column=1,padx=5,pady=5)
email_in = Entry(twelve,width=30).grid(row=2 ,column=3,padx=5,pady=5)

passwrd = Label(twelve,text="Enter Password").grid(row=3,column=1,padx=5,pady=5)
pass_in = Entry(twelve,width=30,show="*").grid(row=3 ,column=3,padx=5,pady=5)

gen = Label(twelve,text="Select Gender").grid(row=4,column=1,padx=5,pady=5)

var1 = IntVar()
male = Radiobutton(twelve,text="Male",value=1,variable=var1).grid(row=4,column=3,padx=5,pady=5)
female = Radiobutton(twelve,text="FeMale",value=2,variable=var1).grid(row=5,column=3,padx=5,pady=5)
others = Radiobutton(twelve,text="Others",value=3,variable=var1).grid(row=6,column=3,padx=5,pady=5)

verify = Checkbutton(twelve,text="Verify terms and conditions").grid(row=7,column=3,padx=5,pady=5)

submit = Button(twelve,width=20,padx=2,pady=2,text="Submit").grid(row=8,column=3,padx=5,pady=5)

twelve.mainloop()