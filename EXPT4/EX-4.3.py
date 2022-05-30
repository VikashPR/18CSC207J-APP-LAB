from tkinter import *
three = Tk()
three.title("EMPLOYEE")
# employee id
empid = Label(three, text="Empid").grid(row=0, column=0, padx=10, pady=10)
empid_in = Entry(three).grid(row=0, column=1, padx=10, pady=10)

# customer id
cusname = Label(three, text="Employee Name :").grid(
    row=1, column=0, padx=10, pady=10)
cusname_in = Entry(three).grid(row=1, column=1, padx=10, pady=10)

# job
branch = Label(three, text="Job").grid(row=2, column=0, padx=10, pady=10)
branch_in = Entry(three).grid(row=2, column=1, padx=10, pady=10)

# employee type
emmtype = Label(three, text="Employee type").grid(
    row=3, column=0, padx=10, pady=10)
var = IntVar()
regbutn = Radiobutton(three, text="Regular", variable=var, value=0).grid(
    row=3, column=1, padx=10, pady=10)
tembutn = Radiobutton(three, text="Temporary", variable=var, value=1).grid(
    row=3, column=3, padx=10, pady=10)

# salary
sal = Label(three, text="Salary").grid(row=4, column=0, padx=10, pady=10)
salamt = Spinbox(three, from_=19, to=100).grid(
    row=4, column=1, padx=10, pady=10)

# insert and update button
ins = Button(three, text="insert").grid(row=5, column=0, padx=10, pady=10)
update = Button(three, text="Update").grid(row=5, column=1, padx=10, pady=10)

# delete and select button
dele = Button(three, text="Delete").grid(row=6, column=0, padx=10, pady=10)
sele = Button(three, text="Select").grid(row=6, column=1, padx=10, pady=10)

three.geometry("500x400")
three.mainloop()
