from tkinter import *
eight = Tk()
eight.title("Registration form")

form = Label(eight, text="Form", bg='#90EE90').grid(
    row=0, column=1, padx=42, pady=2)

name = Label(eight, text="Name ", bg='#90EE90').grid(
    row=1, column=0, padx=5, pady=5)
name_in = Entry(eight, width=40).grid(row=1, column=1, padx=2, pady=2)

course = Label(eight, text="Course", bg='#90EE90').grid(
    row=2, column=0, padx=2, pady=2)
course_in = Entry(eight, width=40).grid(row=2, column=1, padx=2, pady=2)

sem = Label(eight, text="Semester", bg='#90EE90').grid(
    row=3, column=0, padx=2, pady=2)
semester_in = Entry(eight, width=40).grid(row=3, column=1, padx=2, pady=2)

form = Label(eight, text="Form No. ", bg='#90EE90').grid(
    row=4, column=0, padx=2, pady=2)
form_in = Entry(eight, width=40).grid(row=4, column=1, padx=2, pady=2)

contact = Label(eight, text="Contact No. ", bg='#90EE90').grid(
    row=5, column=0, padx=2, pady=2)
contact_in = Entry(eight, width=40).grid(row=5, column=1, padx=2, pady=2)

email = Label(eight, text="Email id ", bg='#90EE90').grid(
    row=6, column=0, padx=2, pady=2)
email_in = Entry(eight, width=40).grid(row=6, column=1, padx=2, pady=2)

address = Label(eight, text="Address", bg='#90EE90').grid(
    row=7, column=0, padx=2, pady=2)
address_in = Entry(eight, width=40).grid(row=7, column=1, padx=2, pady=2)

sub = Button(eight, text="Submit", bg="red", fg='black').grid(
    row=8, column=1, padx=2, pady=2)

eight.geometry("500x300")
eight.configure(bg='#90EE90')
eight.mainloop()
