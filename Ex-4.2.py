from ast import Delete
from cProfile import label
from cgitb import text
from select import select
from sys import builtin_module_names
from tkinter import *
from tkinter.tix import Select
from turtle import bgcolor, right, update

w = Tk()
w.title('tk')
w.geometry('600x300')
Label(w, text='Regno').grid(row=0)
Label(w, text='Name: ').grid(row=1)
Label(w, text='Dept').grid(row=2)
Label(w, text='Gender').grid(row=3)
var1 = IntVar()
Radiobutton(w, text='Male', variable=var1).grid(
    row=3, column=1, padx=35, sticky=W)
var2 = IntVar()
Radiobutton(w, text='Female', variable=var2).grid(row=3, column=2, sticky=W)
Label(w, text='Age').grid(row=5)
sp = Spinbox(w, from_=0, to=100).grid(row=5, column=1)
l1 = Entry(w)
l2 = Entry(w)
l3 = Entry(w)
l1.grid(row=0, column=1)
l2.grid(row=1, column=1)
l3.grid(row=2, column=1)
Button(w, text='Insert', width=10, command=INSERT).grid(row=6)
Button(w, text='Update', width=10, command=update).grid(row=6, column=1)
Button(w, text='Delete', width=10, command=Delete).grid(row=7)
Button(w, text='select', width=10, command=Select).grid(row=7, column=1)

mainloop()
