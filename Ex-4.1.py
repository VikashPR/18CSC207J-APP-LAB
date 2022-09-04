from tkinter import *
from tkinter.tix import COLUMN

app = Tk()


app.title("App Lab Ex-4.1")

regNo_label = Label(app, text="Reg No")
regNo_input = Entry(app)
regNo_label.grid(row=0, column=0, padx=10, pady=10)
regNo_input.grid(row=0, column=1, padx=10, pady=10)

name_label = Label(app, text="Name")
name_input = Entry(app)
name_label.grid(row=1, column=0, padx=10, pady=10)
name_input.grid(row=1, column=1, padx=10, pady=10)

dept_label = Label(app, text="Dept")
dept_input = Entry(app)
dept_label.grid(row=2, column=0, padx=10, pady=10)
dept_input.grid(row=2, column=1, padx=10, pady=10)

gender_label = Label(app, text="Gender")
intVar = IntVar()
gender_input_male = Radiobutton(app, text="Male", variable=intVar, value=1)
gender_input_female = Radiobutton(app, text="Female", variable=intVar, value=2)
gender_label.grid(row=3, column=0)
gender_input_male.grid(row=3, column=1)
gender_input_female.grid(row=3, column=2)

spinBox = Spinbox(app, from_=17, to=69)
spinBox_label = Label(app, text="Age")
spinBox_label.grid(row=4, column=0)
spinBox.grid(row=4, column=1, padx=10, pady=10)

insert_button = Button(app, text="Insert")
update_button = Button(app, text="Update")
delete_button = Button(app, text="Delete")
select_button = Button(app, text="Select")
insert_button.grid(row=5, column=0, pady=20, padx=20)
update_button.grid(row=5, column=1, pady=20, padx=20)
delete_button.grid(row=6, column=0, pady=20, padx=20)
select_button.grid(row=6, column=1, pady=20, padx=20)


app.geometry("500x500")
app.mainloop()
