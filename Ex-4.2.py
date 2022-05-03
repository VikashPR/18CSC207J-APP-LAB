from tkinter import *

app = Tk()

app.title("App Ex-4.2")

custmId_label = Label(app, text="Custm ID")
custmId_input = Entry(app)
custmId_label.grid(row=0, column=0, padx=10, pady=10)
custmId_input.grid(row=0, column=1)

custmName_label = Label(app, text="Customer Name")
custmName_input = Entry(app)
custmName_label.grid(row=1, column=0, padx=10, pady=10)
custmName_input.grid(row=1, column=1)

branch_label = Label(app, text="Branch")
branch_input = Entry(app)
branch_label.grid(row=2, column=0, padx=10, pady=10)
branch_input.grid(row=2, column=1)

intVar = IntVar()
accountType_label = Label(app, text="Account Type")

accountType_inputOne = Radiobutton(
    app, text="Savings", value=1, variable=intVar)

accountType_inputTwo = Radiobutton(
    app, text="Non Savings", value=2, variable=intVar)

accountType_label.grid(row=3, column=0, pady=10, padx=10)
accountType_inputOne.grid(row=3, column=1)
accountType_inputTwo.grid(row=3, column=2)

amountSlider_label = Label(app, text="Amount")
amountSlider_input = Scale(app, from_=19, to=69, orient=HORIZONTAL)
amountSlider_label.grid(row=4, column=0, pady=10, padx=10)
amountSlider_input.grid(row=4, column=1, padx=10, pady=10)

insert_button = Button(app, text="Insert")
update_button = Button(app, text="Update")
delete_button = Button(app, text="Delete")
select_button = Button(app, text="Select")
insert_button.grid(row=5, column=0, pady=20, padx=20)
update_button.grid(row=5, column=1, pady=20, padx=20)
delete_button.grid(row=6, column=0, pady=20, padx=20)
select_button.grid(row=6, column=1, pady=20, padx=20)
app.geometry("500x400")
app.mainloop()
