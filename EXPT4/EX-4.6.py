from tkinter import *
six = Tk()
six.title("Customer Loan Details")

# annual rate
ann = Label(six, text="Annual Rate :").grid(row=0, column=0, padx=10, pady=5)
annrate = Entry(six).grid(row=0, column=1, padx=10, pady=5)

# number of payments
num = Label(six, text="Number of Paymnets :").grid(
    row=1, column=0, padx=10, pady=5)
num_in = Entry(six).grid(row=1, column=1, padx=10, pady=5)

# loan principle
loan = Label(six, text="Loan Principle :").grid(
    row=2, column=0, padx=10, pady=5)
loan_in = Entry(six).grid(row=2, column=1, padx=10, pady=5)

# monthly payment
month = Label(six, text="Monthly Payment :").grid(
    row=3, column=0, padx=10, pady=5)
month_in = Entry(six).grid(row=3, column=1, padx=10, pady=5)

# remaining loan
remain = Label(six, text="Remaining loan :").grid(
    row=4, column=0, padx=10, pady=5)
remain_in = Entry(six).grid(row=4, column=1, padx=10, pady=5)

# buttons
final = Button(six, text="Final Balance").grid(
    row=5, column=0, padx=10, pady=5)
monthly = Button(six, text="Monthly Payment").grid(
    row=5, column=1, padx=10, pady=5)
quitbuttn = Button(six, text="Quit").grid(row=5, column=2, padx=10, pady=5)

six.geometry("400x200")
six.mainloop()
