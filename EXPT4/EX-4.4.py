from tkinter import *
four = Tk()
four.title("FLYER")
# booking id
bookid = Label(four, text="Bookingid ").grid(row=0, column=0, padx=4, pady=4)
bookid_in = Entry(four).grid(row=0, column=1, padx=4, pady=4)

# pass name
passname = Label(four, text="Passenger Name :").grid(
    row=1, column=0, padx=4, pady=4)
passname_in = Entry(four).grid(row=1, column=1, padx=4, pady=4)

# flight
flight = Label(four, text="Flight").grid(row=2, column=0, padx=4, pady=4)
flight_in = Entry(four).grid(row=2, column=1, padx=4, pady=4)

# source
source = Label(four, text="Source").grid(row=3, column=0, padx=4, pady=4)
var = IntVar()
butn1 = Radiobutton(four, text="Delhi", variable=var, value=0).grid(
    row=3, column=1, padx=4, pady=4)
butn2 = Radiobutton(four, text="Mumbai", variable=var,
                    value=1).grid(row=3, column=2, padx=4, pady=4)
des = Label(four, text="Destination ").grid(row=3, column=3, padx=4, pady=4)
var1 = IntVar()
butn1 = Radiobutton(four, text="Chennai", variable=var1,
                    value=0).grid(row=3, column=4, padx=4, pady=4)
butn2 = Radiobutton(four, text="kolkata", variable=var1,
                    value=1).grid(row=3, column=5, padx=4, pady=4)

# Duration
dur = Label(four, text="Duration ").grid(row=4, column=0, padx=4, pady=4)
dur_in = Spinbox(four, from_=3, to=4).grid(row=4, column=1, padx=4, pady=4)

# insert and update button
ins = Button(four, text="insert").grid(row=5, column=0, padx=4, pady=4)
update = Button(four, text="Update").grid(row=5, column=1, padx=4, pady=4)

# delete and select button
dele = Button(four, text="Delete").grid(row=6, column=0, padx=4, pady=4)
sele = Button(four, text="Select").grid(row=6, column=1, padx=4, pady=4)

four.geometry("600x250")
four.mainloop()
