import sys
import os
if sys.version[0] =='2':       # le premier caractère de la chaîne nous suffit
    import Tkinter as tk      # module Tkinter pour Python 2
else:
    import tkinter as tk      # module Tkinter pour Python 3

from PIL import Image
from io import BytesIO
from lxml import etree
from tkinter.messagebox import *
import requests
import xml.etree.ElementTree as ET


def window_trombi():
    import Bulletin
    a=0
    b=0
    c=0
    i=0

    #root = tk.Tk()
    root = tk.Toplevel()
    root.title('trombi')

    RWidth=root.winfo_screenwidth()
    RHeight=root.winfo_screenheight()
    print("Width:",RWidth,"  Height:",RHeight)
    positionRight = int(root.winfo_screenwidth()/2 - RWidth/5)
    positionDown = int(root.winfo_screenheight()/2 - RHeight/3)
    root.geometry("+{}+{}".format(positionRight, positionDown))

    nombulletin = []
    buttontrombi = []
    photo = []


    mytree = ET.ElementTree(ET.fromstring(requests.get('http://www.mesdocumentsinterfaces.org/img_trombi.xml').text))
    myroot = mytree.getroot()


    for e in myroot.findall('personne'):
        nombull=str(e.find('id').text)
        nombulletin.insert(i,nombull)
        print('\t',nombulletin[i])
        i+=1

    def onclick():
        #valbut = labnom.get()
        Bulletin.window_bulletin(nombulletin[3])



    for x in myroot.findall('personne'):
        nom=str(x.find('nom').text)
        nameimg=x.find('image').text
        print(nameimg)
        #img = requests.get('http://www.mesdocumentsinterfaces.org/docs/antoine.gif')
        #response = requests.get('http://www.mesdocumentsinterfaces.org/docs/'+nameimg)
        #img = Image.open(BytesIO(response.content))
        img=os.path.abspath("./interface_eleves/"+nameimg)

        photo.insert(c,tk.PhotoImage(file=img))

        #labnom = tk.StringVar(root)

        buttontrombi.insert(c,tk.Button(root,text=nom+' ('+nombulletin[c]+')',textvariable=nombulletin[c], image=photo[c] , height=180, width=150,compound="top",command=onclick))

        if a>5 :
            b=b+1
            a=0

        buttontrombi[c].grid (row=b, column=a)
        a=a+1
        c=c+1
    root.mainloop()
#window_trombi()
