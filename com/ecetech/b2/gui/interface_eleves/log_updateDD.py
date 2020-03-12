from tkinter import *
from functools import partial
from tkinter.messagebox import *
from lxml import etree
import trombi



def LectureXML() :
    tree = etree.parse("XML_login_file.xml")

    for personne in tree.xpath("/repertoire/personne/nom"):
        print(personne.text)

    for personne in tree.xpath("/repertoire/personne/motdepasse"):
        print(personne.text)

def onclick():
    tree = etree.parse("XML_login_file.xml")

    val=0
    val2=0
    print(text_id.get())
    for personne in tree.xpath("/repertoire/personne/nom"):
        if text_id.get() == personne.text :
            print("ok")
            val=1

    for personne in tree.xpath("/repertoire/personne/motdepasse"):
        if text_mdp.get() == personne.text :
            print("ok")
            val2=1

    if (val2+val)==2 :
        #showinfo('Résultat','Mot de passe correct.\n')
        trombi.window_trombi()
    else:
        showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')



def EcritureXML():
    print(text_name.get())
    print(text_password.get())
    tree = etree.parse("XML_login_file.xml")
    rootlogin =tree.getroot()

    #repertoire = etree.Element("repertoire")
    personne = etree.Element("personne")
    nom = etree.SubElement(personne, "nom")
    nom.text = text_name.get()
    mdp = etree.SubElement(personne, "motdepasse")
    mdp.text = text_password.get()

    rootlogin.append(personne)
    tree.write("XML_login_file.xml")




rootlogin = Tk()
rootlogin.title("Fenêtre de connection")
rootlogin.geometry("320x300")
text_id = StringVar(rootlogin)
id = Label(rootlogin, text='Nom')
text_mdp = StringVar(rootlogin)
mdp = Label(rootlogin, text='Mot de passe')
entree_nom = Entry(rootlogin, textvariable=text_id)
entree_mdp = Entry(rootlogin, textvariable=text_mdp, show="*")
button = Button(rootlogin, text='Connection', command=onclick)
mdp.grid(column=1, row=3)
id.grid(column=1, row=1)
entree_nom.grid(column=1, row=2)
entree_mdp.grid(column=1, row=4)
button.grid(column=1, row=5)

Label1 = Label(rootlogin, text ='Si vous êtes un nouvel user inscrivez vous ci-dessous', fg ='red', padx=10)
blanc = Label(rootlogin, text=' ')
blanc2 = Label(rootlogin, text=' ')
blanc.grid(column=1, row=7)
blanc2.grid(column=1, row=9)
text_name = StringVar(rootlogin)
name = Label(rootlogin, text='Nom')
text_password = StringVar(rootlogin)
password = Label(rootlogin, text='Mot de passe')
entree_name = Entry(rootlogin, textvariable=text_name)
entree_password = Entry(rootlogin, textvariable=text_password, show="*")
button = Button(rootlogin, text='Valider')
Label1.grid(column=1, row=8)
name.grid(column=1, row=10)
password.grid(column=1, row=12)
entree_name.grid(column=1, row=11)
entree_password.grid(column=1, row=13)
button.grid(column=1, row=14)

rootlogin.mainloop()

