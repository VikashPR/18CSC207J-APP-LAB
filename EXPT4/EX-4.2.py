from tkinter import *
two = Tk()
two.title("BANKING")
# cusid
custid = Label(two, text="Custid ").grid(row=0, column=0, padx=5, pady=5)
custid_in = Entry(two).grid(row=0, column=1, padx=5, pady=5)

# cus name
name = Label(two, text="Customer Name : ").grid(
    row=1, column=0, padx=5, pady=5)
name_in = Entry(two).grid(row=1, column=1, padx=5, pady=5)

# Branch
branch = Label(two, text="Branch ").grid(row=2, column=0, padx=5, pady=5)
branch_in = Entry(two).grid(row=2, column=1, padx=5, pady=5)

# acc type
acctype = Label(two, text="Account type").grid(row=3, column=0, padx=5, pady=5)
var = IntVar()
malebutn = Radiobutton(two, text="Saving", variable=var,
                       value=0).grid(row=3, column=1, padx=5, pady=5)
femalebutn = Radiobutton(two, text="Non Saving", variable=var, value=1).grid(
    row=3, column=3, padx=5, pady=5)

# amount
amount = Label(two, text="Amount").grid(row=4, column=0, padx=5, pady=5)
no_slider = Scale(two, from_=19, to=100, orient=HORIZONTAL).grid(
    row=4, column=1, padx=5, pady=5)

# insert and update button
ins = Button(two, text="insert").grid(row=5, column=0, padx=5, pady=5)
update = Button(two, text="Update").grid(row=5, column=1, padx=5, pady=5)

# delete and select button
dele = Button(two, text="Delete").grid(row=6, column=0, padx=5, pady=5)
sele = Button(two, text="Select").grid(row=6, column=1, padx=5, pady=5)

two.geometry("450x300")
two.mainloop()
