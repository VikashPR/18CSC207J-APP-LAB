from tkinter import *
five = Tk()

# booking id
mov = Label(five, text="Movie Booking id :").grid(
    row=0, column=0, padx=10, pady=5)
mov_in = Entry(five).grid(row=0, column=1, padx=10, pady=5)

# person name
per = Label(five, text="Person name :").grid(row=1, column=0, padx=10, pady=5)
per_in = Entry(five).grid(row=1, column=1, padx=10, pady=5)

# movie name
movname = Label(five, text="Movie Name :").grid(
    row=2, column=0, padx=10, pady=5)
movname_in = Entry(five).grid(row=2, column=1, padx=10, pady=5)

# class
var = IntVar()
clas = Label(five, text="class").grid(row=3, column=0, padx=10, pady=5)
abuttn = Radiobutton(five, text="A", variable=var, value=0).grid(
    row=3, column=1, padx=5, pady=5)
bbuttn = Radiobutton(five, text="B", variable=var, value=1).grid(
    row=3, column=2, padx=5, pady=5)
timeshow = Label(five, text="Time of Show ").grid(
    row=3, column=3, padx=5, pady=5)
newvar = IntVar()
sevenbuttn = Checkbutton(five, text="7.15 pm", variable=newvar, onvalue=0).grid(
    row=3, column=4, padx=5, pady=5)
ninebuttn = Checkbutton(five, text="9 am", variable=newvar, offvalue=1).grid(
    row=3, column=5, padx=5, pady=5)

# no of tickets
no = Label(five, text="No of Tickets ").grid(row=4, column=0, padx=5, pady=5)
no_slider = Scale(five, from_=1, to=10, orient=HORIZONTAL).grid(
    row=4, column=1, padx=5, pady=5)

# insert and update button
ins = Button(five, text="insert").grid(row=5, column=0, padx=5, pady=5)
update = Button(five, text="Update").grid(row=5, column=1, padx=5, pady=5)

# delete and select button
dele = Button(five, text="Delete").grid(row=6, column=0, padx=5, pady=5)
sele = Button(five, text="Select").grid(row=6, column=1, padx=5, pady=5)

five.geometry("650x300")
five.mainloop()
