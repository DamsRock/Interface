from tkinter import *

root = Tk()
root.title('Bulletin')
root.geometry('600x150')

cell1 = Text(root, height=1, width=15)
cell1.insert(INSERT, 'Matières')
cell1.pack()
cell1.grid(row=0, column=0)
cell2 = Text(root, height=1, width=5)
cell2.insert(INSERT, 'Coeff')
cell2.grid(row=0, column=1)
cell3 = Text(root, height=1, width=13)
cell3.insert(INSERT, 'Moyenne élève')
cell3.grid(row=0, column=2)
cell4 = Text(root, height=1, width=14)
cell4.insert(INSERT, 'Moyenne Classe')
cell4.grid(row=0, column=3)
matiere1 = Text(root, height=1, width=23)
matiere1.insert(INSERT, 'Mathématiques appliqués')
matiere1.grid(row=1, column=0)
matiere2 = Text(root, height=1, width=23)
matiere2.insert(INSERT, 'Physique appliquée')
matiere2.grid(row=2, column=0)
matiere3 = Text(root, height=1, width=23)
matiere3.insert(INSERT, 'Projet technologique')
matiere3.grid(row=3, column=0)
coeff = Text(root, height=1, width=5)
coeff.insert(INSERT, 2)
coeff.grid(row=1, column=1)

root.mainloop()
