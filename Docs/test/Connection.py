from tkinter import *
from functools import partial


def update_label(label, stringvar):
    text = stringvar.get()
    label.config(text=text)

root = Tk()
root.title("Fenêtre de connection ou d'Inscription")
root.geometry("200x200")
text_id = StringVar(root)
id = Label(root, text='')
text_mdp = StringVar(root)
mdp = Label(root, text='')
entree_nom = Entry(root, textvariable=text_id)
entree_mdp = Entry(root, textvariable=text_mdp)
button = Button(root, text='Connection', command=partial(update_label, id, text_id))
putton = Button(root, text='Inscription')
id.grid(column=1, row=0)
entree_nom.grid(column=1, row=2)
entree_mdp.grid(column=1, row=3)
button.grid(column=1, row=4)
putton.grid(column=1, row=5)
root.mainloop()
