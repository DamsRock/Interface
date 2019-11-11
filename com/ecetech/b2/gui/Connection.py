from tkinter import *
from functools import partial


def update_label(label, stringvar):
    text = stringvar.get()
    label.config(text=text)

root = Tk()
root.geometry("600x400")
text_id = StringVar(root)
id = Label(root, text='')
text_mdp = StringVar(root)
mdp = Label(root, text='')
entree_nom = Entry(root, textvariable=text_id)
entree_mdp = Entry(root, textvariable=text_mdp)
button = Button(root, text='Connection', command=partial(update_label, id, text_id))
putton = Button(root, text='Inscription')
id.grid(column=0, row=0)
mdp.grid(column=0, row=0)
entree_nom.grid(column=0, row=1)
entree_mdp.grid(column=0, row=2)
button.grid(column=0, row=3)
putton.grid(column=0, row=4)
root.mainloop()
