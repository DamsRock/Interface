from tkinter import *
from functools import partial

root = Tk()

photo = PhotoImage(file="images1.gif")
photos = PhotoImage(file="images-1.gif")
phot0 = PhotoImage(file="index.gif")
root.geometry("1000x1000")
text = StringVar(root)

label = Label(root, text='')
entry_name = Entry(root, textvariable=text)

button = Button(root, image=photo, height=300, width=300)

putton = Button(root, image=photos, height=300, width=300)
lutton = Button(root, image=phot0, height=300, width=300)

label.grid(column=0, row=0)
button.grid(column=1, row=0)
putton.grid(column=2, row=0)
lutton.grid(column=3, row=0)

root.mainloop()
