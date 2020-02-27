from tkinter import *
root = Tk()

global ligne
global colour

def callback(*args):
    for i in range(len(colour)):
        if ligne.get().lower() == test[i].lower():
            ligne.configure({"background": colour[i]})
            break
        else:
            ligne.configure({"background": "white"})


var = StringVar()
ligne = Entry(root, textvariable=var)
test = ["Yes", "No", "Maybe"]
colour = ["Green", "Red", "Orange"]
var.trace(mode="w", callback=callback)

ligne.pack()
root.mainloop()
