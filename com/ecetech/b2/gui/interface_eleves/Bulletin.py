from tkinter import *

root = Tk()
root.title('Bulletin')
root.geometry('500x150')

lignes = 15
colonnes = 4

for i in range(lignes):
    for j in range(colonnes):
        cell1 = Entry()
        cell1.insert(0, 'Matières')
        cell1.grid(row=0, column=0)
        cell2 = Entry()
        cell2.insert(0, 'Coeff')
        cell2.grid(row=0, column=1)
        cell3 = Entry()
        cell3.insert(0, 'Moyenne élève')
        cell3.grid(row=0, column=2)
        cell4 = Entry()
        cell4.insert(0, 'Moyenne Classe')
        cell4.grid(row=0, column=3)
        matiere1 = Entry()
        matiere1.insert(0, 'Mathématiques appliqués')
        matiere1.grid(row=1, column=0)
        matiere2 = Entry()
        matiere2.insert(0, 'Physique appliquée')
        matiere2.grid(row=2, column=0)
        matiere3 = Entry()
        matiere3.insert(0, 'Projet technologique')
        matiere3.grid(row=3, column=0)
        coeff = Entry()
        coeff.insert(0, 2)
        coeff.grid(row=1, column=1)


root.mainloop()
