from tkinter import *

root = Tk()

myLable = Label(root, text="This is grid1 bro")
myLable2 = Label(root, text="This is grid1 bro")

myLable.grid(row=0, column=0)
myLable2.grid(row=12, column=1)

root.mainloop()