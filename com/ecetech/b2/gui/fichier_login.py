from tkinter import *
from functools import partial
from tkinter.messagebox import *
tab = []


def update_label(label, stringvar):
	text = stringvar.get()
	label.config(text=text)


def lecture(tab):

	file = open ("fichier_login.csv", "r")

	for line in file :
		tab = line.split(";")
		print(tab)

	file.close()


def Verification():
	file = open ("fichier_login.csv", "r")

	for line in file :
		tab = line.split(";")
		

	file.close()

	#if text_id.get() in tab :
		#print('ok')

	if text_mdp.get() == 'NolanC_2015':
		showinfo('Résultat','Mot de passe correct.\nAu revoir !')        
	else:
		# le mot de passe est incorrect : on affiche une boîte de dialogue
		showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')
		text_mdp.set('')


def Inscription():
	register = Tk()
	register.title("Fenêtre d'Inscritption")
	register.geometry("400x300")
	new_name = StringVar(register)
	name = Label(register, text='')
	new_password = StringVar(register)
	password = Label(register, text='')
	entree_name = Entry(register, textvariable=new_name)
	entree_password = Entry(register, textvariable=new_password)
	button = Button(register, text='Valider', command=addfile(new_name,new_password))
	entree_name.grid(column=1, row=2)
	entree_password.grid(column=1, row=3)
	button.grid(column=1, row=4)


def addfile(new_name,new_password):

	
	name=new_name.get()

	mot_de_passe=new_password.get()

	type_de_compte = 'User'

	file = open ("fichier_login.csv","a")
	file.write(name)
	file.write(mot_de_passe)
	file.write(type_de_compte)

	file.close()
	lecture(tab)



root = Tk()
root.title("Fenêtre de connection")
root.geometry("800x600")
lecture(tab)
text_id = StringVar(root)
id = Label(root, text='')
text_mdp = StringVar(root)
mdp = Label(root, text='')
entree_nom = Entry(root, textvariable=text_id)
entree_mdp = Entry(root, textvariable=text_mdp)
button = Button(root, text='Connection', command=Verification)
putton = Button(root, text='Inscription', command=Inscription)
id.grid(column=1, row=0)
entree_nom.grid(column=1, row=2)
entree_mdp.grid(column=1, row=3)
button.grid(column=1, row=4)
putton.grid(column=1, row=5)
root.mainloop()

