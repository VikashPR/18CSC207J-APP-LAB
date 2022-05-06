from tkinter import *

app = Tk()
canvas = Canvas(app, width=500, height=400, bg="grey")

canvas.create_text(250, 100, text="1 USD = 75 Indian Rupees",
                   fill="cyan", font=("Times", 30))
canvas.pack()
app.mainloop()
