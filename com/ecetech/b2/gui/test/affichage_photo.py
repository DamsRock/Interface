from tkinter import *
from functools import partial




def update_label(label, stringvar):

    text = stringvar.get()
    label.config(text=text)




def image ():
    photo = PhotoImage(file="lion....gif")

    canvas = Canvas(root,width=750, height=500)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.pack()
    root.mainloop()


root = Tk()
root.geometry("600x400")
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
