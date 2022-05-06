from faulthandler import disable
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk


app = Tk()
app.title("Tab Widget")
tabControl = ttk.Notebook(app)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.grid(row=0, column=0)
pb = ttk.Progressbar(
    tab1,
    orient='horizontal',
    mode='indeterminate',
    length=280
)

Checkbutton(tab1, text="Disabled").grid(
    row=1, column=0)

Checkbutton(tab1, text="Unchecked").grid(
    row=1, column=1)

Checkbutton(tab1, text="Enabled").grid(
    row=1, column=2)

Checkbutton(tab1, text="Blue").grid(
    row=2, column=0)

Checkbutton(tab1, text="Gold").grid(
    row=2, column=1)

Checkbutton(tab1, text="Red").grid(
    row=2, column=2)


# place the progressbar
pb.grid(column=0, row=7, columnspan=2, padx=10, pady=20)

# Run button
start_button = ttk.Button(
    tab1,
    text='Run ProgressBar',
    command=pb.start
)
start_button.grid(column=0, row=3, padx=10, pady=10)

# start button
start_button = ttk.Button(
    tab1,
    text='Start ProgressBar',
    command=pb.start
)
start_button.grid(column=0, row=4, padx=10, pady=10)
# stop button
stop_button = ttk.Button(
    tab1,
    text='Stop immediately',
    command=pb.stop
)
stop_button.grid(column=0, row=5, padx=10, pady=10)


# stop button
stop_button = ttk.Button(
    tab1,
    text='Stop after a second',
    command=pb.stop
)
stop_button.grid(column=0, row=6, padx=10, pady=10)


app.mainloop()
