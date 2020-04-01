from functools import partial

from tkinter import *

t = 0
v = 0


def update_label(label, stringvar):
    text = stringvar.get()
    label.config(text=text)


def image():
    photo = PhotoImage(file="lion....gif")
    canvas = Canvas(root, height=500, width=500)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.pack()
    canvas.place(x=0 + t * 100, y=100 + v * 100, height=100, width=100)
    #global t
    #global v
    if t < 6:
        t = t + 1
    else:
        t = 0
        v = v + 1
    root.mainloop()


root = Tk()

root.geometry("1000x1000")
text = StringVar(root)
label = Label(root, text='')
entry_name = Entry(root, textvariable=text)
button = Button(root, text='clic', command=partial(update_label, label, text))

putton = Button(root, text='image', command=partial(image))
label.grid(column=0, row=0)
entry_name.grid(column=0, row=1)
button.grid(column=0, row=2)
putton.grid(column=0, row=3)
root.mainloop()
