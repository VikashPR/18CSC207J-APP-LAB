from tkinter import *
one = Tk()
one.title("STUDENT")
# regno
red = Label(one, text="Regno ").grid(row=0, column=0, padx=2, pady=2)
red_in = Entry(one).grid(row=0, column=1, padx=2, pady=2)

# name
name = Label(one, text="Name : ").grid(row=1, column=0, padx=2, pady=2)
name_in = Entry(one).grid(row=1, column=1, padx=2, pady=2)

# dept
dept = Label(one, text="Dept ").grid(row=2, column=0, padx=2, pady=2)
dept_in = Entry(one).grid(row=2, column=1, padx=2, pady=2)

# gender
gender = Label(one, text="Gender").grid(row=3, column=0, padx=2, pady=2)
var = IntVar()
malebutn = Radiobutton(one, text="Male", variable=var, value=0).grid(
    row=3, column=1, padx=2, pady=2)
femalebutn = Radiobutton(one, text="Female", variable=var, value=1).grid(
    row=3, column=3, padx=2, pady=2)

# age
age = Label(one, text="Age").grid(row=4, column=0, padx=2, pady=2)
age = Spinbox(one, from_=19, to=100).grid(row=4, column=1, padx=2, pady=2)

# insert and update button
ins = Button(one, text="insert").grid(row=5, column=0, padx=2, pady=2)
update = Button(one, text="Update").grid(row=5, column=1, padx=2, pady=2)

# delete and select button
dele = Button(one, text="Delete").grid(row=6, column=0, padx=2, pady=2)
sele = Button(one, text="Select").grid(row=6, column=1, padx=2, pady=2)

one.geometry("450x250")
one.mainloop()
