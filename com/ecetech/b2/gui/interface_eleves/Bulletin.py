''' importation des modules '''

import requests
import sys
if sys.version[0] =='2':       # le premier caractère de la chaîne nous suffit
    import Tkinter as tk      # module Tkinter pour Python 2
else:
    import tkinter as tk      # module Tkinter pour Python 33

import xml.etree.ElementTree as ET
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A0
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from PIL import *

import os


def window_bulletin(id):
    # Création de la fenêtre principale
    wind = tk.Toplevel()
    wind.title('Bulletin')
    RWidth=wind.winfo_screenwidth()
    RHeight=wind.winfo_screenheight()
    print("Width:",RWidth,"  Height:",RHeight)
    positionRight = int(wind.winfo_screenwidth()/2 - RWidth/10)
    positionDown = int(wind.winfo_screenheight()/2 - RHeight/4)

    wind.geometry("+{}+{}".format(positionRight, positionDown))

    # Fonction de Séparation des modules
    def separation(r, c, h, w):
        ligne = tk.Label(wind, height=h, width=w)
        ligne.configure({"background": "grey"})
        ligne.grid(row=r, column=c)


    # Fonction création entré
    def entre(r, c, h, w, la):
        champ = tk.Label(wind, text=str(la), height=h, width=w, relief=tk.RIDGE)
        champ.grid(row=r, column=c)

    mod=7  #Largeur champs modules
    cmw = 31  # largeur champs matières
    ccw = 5  # largeur champs coeff
    cmew = 13  # largeur champs moyenne eleves
    cmcw = 13  # largeur champs moyenne classe
    cvrmw = 24  # largeur champs validation module
    cECTSw = 5  # largeur champs ECTS

    mati=1
    coef=2
    moye=3
    moyc=4
    val_ou_rat=5
    ec=6

    global save
    save=0

    # Ouverture et lecture du fichier XML
    r_bulletins = "http://www.mesdocumentsinterfaces.org/docs/bulletin.xml"
    #w_bulletins = "bulletin.xml"
    def xml_read():
        row=1
        # Création et remplissage des différentes catégories
        entre(row, mati, 1, cmw, 'Matieres')
        entre(row, coef, 1, ccw, 'Coeff')
        entre(row, moye, 1, cmew, 'Moyenne eleves')
        entre(row, moyc, 1, cmcw, 'Moyenne classe')
        entre(row, val_ou_rat, 1, cvrmw, 'Validation/Rattrapage module')
        entre(row, ec, 1, cECTSw, 'ECTS')
        row+=1

        #recuperation du fichier sur ma VM CentOS (/var/www/Interfaces/docs/bulletin.xml) ;)
        tree = ET.ElementTree(ET.fromstring(requests.get(r_bulletins).text)).getroot()
        print(id)
        for eleve in tree.findall(id):
            row+=1
            nom = eleve.find('nom').text
            prenom = eleve.find('prenom').text
            moyenne_total = eleve.find('moyenne_total').text
            wind.title('Bulletin de ' + prenom + ' ' + nom + '      Moyenne total = ' + moyenne_total)
            M=0 # initialisation nombre de module

            for modules in eleve.findall('module'):
                row+=1
                M+=1
                # separation des modules
                separation(row, 0, 1, mod)
                separation(row, mati, 1, cmw)
                separation(row, coef, 1, ccw)
                separation(row, moye, 1, cmew)
                separation(row, moyc, 1, cmcw)
                separation(row, val_ou_rat, 1, cvrmw)
                separation(row, ec, 1, cECTSw)
                row+=1

                #recuperation et affichage des modules de l'eleve

                entre(row,0,1,mod,'Module '+str(M))
                nom_module = modules.get('nom_module')
                moy_module = modules.get('moyenne_module')
                if moy_module is None: moy_module = "-"
                validation_module = modules.get('validation')
                ECTS = modules.get('ECTS')
                entre(row,mati,1,cmw,nom_module)
                entre(row,coef,1,ccw,'')
                entre(row, moye, 1, cmew, moy_module)
                entre(row, moyc, 1, cmcw, '')
                entre(row, val_ou_rat, 1, cvrmw, validation_module)
                entre(row, ec, 1, cECTSw, ECTS)
                row+=1


                for matiere in modules.findall('matiere'):
                    row+=1
                    nom_matiere = matiere.get('nom_matiere')
                    moy_matiere = matiere.get('moyenne')
                    if moy_matiere is None: moy_matiere = "-"
                    coeff = matiere.find('coeff').text
                    moyenne_eleve = matiere.find('moyenne_eleve').text
                    if moyenne_eleve is None: moyenne_eleve= "-"
                    entre(row,mati,1,cmw,nom_matiere)
                    entre(row,moyc,1,cmcw,moy_matiere)
                    entre(row,coef,1,ccw,coeff)
                    entre(row,moye,1,cmew,moyenne_eleve)
            print('ligne à la fin de l\'affichage du bulletin', row)

        def enregistrer():
            # le fichier est enregistré avec le nom de l'élève en question
            global save
            filename = 'Bulletin de '+nom+' '+prenom+'.pdf'

            # le fichier est enregistré dans le dossier des téléchargements peut importe le PC et l'utilisateur (sous Windows)
            whereto=os.path.join(os.path.expanduser('~'),'Downloads',filename)

            #Génération d'un PDF
            pdf= canvas.Canvas("{0}".format(whereto), pagesize=A4)
            pdf.setFont('Helvetica', 14)
            pdf.setFillColor(colors.black)

            pdf.drawString(2*cm,27*cm,'Bulletin de semestre')
            pdf.drawString(2*cm,27.5*cm, nom+' '+prenom)


            pdf.setFillColor(colors.blue)
            pdf.drawString(400,50, text="campus en ligne de l'ecetech")
            pdf.linkURL(url="ecetech.campusonline.me", rect="")

            pdf.showPage()

            pdf.save()
            save+=1
            print('sauvegarde faite ',save,' fois')



        rowb = row+10
        bouton = tk.Button(wind, text="Exporter en PDF le bulletin",command=enregistrer)
        bouton.grid(row=rowb, column=val_ou_rat)
        print('ligne après bulletin:',rowb)


    xml_read()
    wind.mainloop()

###window_bulletin('DD')
