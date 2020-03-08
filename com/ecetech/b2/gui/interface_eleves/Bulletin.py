import requests
import tkinter as tk
import xml.etree.ElementTree as ET

# Création de la fenêtre principale
root = tk.Tk()
root.title('Bulletin')
root.geometry('800x150')

# Fonction de Séparation des modules
def separation(r, c, h, w):
    ligne = tk.Label(root, height=h, width=w)
    ligne.configure({"background": "black"})
    ligne.grid(row=r, column=c)


# Fonction création entré
def entre(r, c, h, w, la):
    champ = tk.Label(root, text=str(la), height=h, width=w)
    champ.grid(row=r, column=c)


cmw = 23  # largeur champs matières
ccw = 5  # largeur champs coeff
cmew = 13  # largeur champs moyenne eleves
cmcw = 14  # largeur champs moyenne classe
cvmw = 17  # largeur champs validation module
crw = 10  # largeur champs rattrapage
cECTSw = 4  # largeur champs ECTS



# Ouverture et lecture du fichier XML
r_bulletins = "bulletin.xml"
#w_bulletins = "bulletin.xml"
def xml_read():
    # Création et remplissage des différentes catégories
    entre(0, 0, 1, cmw, 'Matières')
    entre(0, 1, 1, ccw, 'Coeff')
    entre(0, 2, 1, cmew, 'Moyenne élèves')
    entre(0, 3, 1, cmcw, 'Moyenne classe')
    entre(0, 4, 1, cvmw, 'Validation module')
    entre(0, 5, 1, crw, 'Rattrapage')
    entre(0, 6, 1, cECTSw, 'ECTS')

    # separation
    separation(1, 0, 1, cmw)
    separation(1, 1, 1, ccw)
    separation(1, 2, 1, cmew)
    separation(1, 3, 1, cmcw)
    separation(1, 4, 1, cvmw)
    separation(1, 5, 1, crw)
    separation(1, 6, 1, cECTSw)

    row = 2
    tree = ET.ElementTree(ET.fromstring(requests.get("").text)).getroot()
    for eleve in tree.findall('eleve'):
        row+=1
        nom = eleve.find('nom').text
        prenom = eleve.find('prenom').text
        nom_module = eleve.get('module')
        moy_module = eleve.get('moyenne_module')
        validation_module = eleve.get('validation')
        ETCS = eleve.get('ECTS')
        entre(row,0,1,cmw,nom_module)

xml_read()
root.mainloop()
