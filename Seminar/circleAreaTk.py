from tkinter import *

app = Tk()

def areaCircle():
    r = float(radius.get())
    area = r * r * 3.14159
    resultVar.set(area)

def perimeterCircle():
    r = float(radius.get())
    perimeter = r * 2 * 3.14159
    resultVar.set(perimeter)

app.title("Circle Calculator")

Label(app, text="Radius").grid(row=0, column=0, padx=5, pady=5)
radius = Entry(app)
radius.grid(row=0, column=1, padx=5, pady=5)

resultVar = StringVar()
Label(app, text="Result").grid(row=1, column=0, padx=5, pady=5)
result = Entry(app, textvariable=resultVar).grid(row=1, column=1, padx=5, pady=5)

Button(app, text="Calc Area", command=areaCircle).grid(row=2, column=0, padx=5, pady=5)
Button(app, text="Calc Perimeter", command=perimeterCircle).grid(row=2, column=1, padx=5, pady=5)

app.mainloop()