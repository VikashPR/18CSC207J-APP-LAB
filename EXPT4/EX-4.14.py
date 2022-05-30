
from datetime import datetime
from tkinter import *

fourteen = Tk()


def convert():
    if variable.get() == 'USD' and variable1.get() == 'INR':
        txtvat2.set(str(float(leftentry.get())*74.93))
    elif variable.get() == 'INR' and variable1.get() == 'USD':
        txtvat2.set(str(float(leftentry.get())/74.93))
    elif variable.get() == 'INR' and variable1.get() == 'INR':
        txtvat2.set(str(float(leftentry.get())))
    elif variable.get() == 'USD' and variable1.get() == 'USD':
        txtvat2.set(str(float(leftentry.get())))


label1 = Label(text='Welcome to Real time currency converter',
               bg='#4169E1', fg='White').grid(row=0, columnspan=3, padx=5, pady=5)
label2 = Label(text='1 USD = 74.93 Indian Rupee').grid(
    row=1, columnspan=3, padx=5, pady=5)
label3 = Label(text='Date ' + str(datetime.now())
               ).grid(row=2, columnspan=3, padx=5, pady=5)


variable = StringVar(fourteen)
variable.set('USD')

variable1 = StringVar(fourteen)
variable1.set('INR')

leftside = OptionMenu(fourteen, variable, 'USD', 'INR').grid(
    row=3, column=0, padx=5, pady=5)
rigtside = OptionMenu(fourteen, variable1, 'INR', 'USD').grid(
    row=3, column=2, padx=5, pady=5)

txtvat1 = StringVar()
txtvat2 = StringVar()

leftentry = Entry(fourteen, textvariable=txtvat1).grid(
    row=4, column=0, padx=5, pady=5)
rightentry = Entry(fourteen, textvariable=txtvat2).grid(
    row=4, column=2, padx=5, pady=5)

convertButton = Button(fourteen, command=convert, fg='white',
                       bg='#1E90FF', text='Convert').grid(row=5, column=1, padx=5, pady=5)


fourteen.mainloop()
