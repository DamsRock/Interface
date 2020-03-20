import tkinter as tk
from lxml import etree
import requests
import xml.etree.ElementTree as ET


def window_trombi():
	import Bulletin

	#root = tk.Tk()
	root = tk.Toplevel()
	root.title('trombi')

	RWidth=root.winfo_screenwidth()
	RHeight=root.winfo_screenheight()
	print("Width:",RWidth,"  Height:",RHeight)
	positionRight = int(root.winfo_screenwidth()/2 - RWidth/2)
	positionDown = int(root.winfo_screenheight()/3 - RHeight/2)
	root.geometry("+{}+{}".format(positionRight, positionDown))

	buttontrombi = []
	photo = []
	a=0
	b=0
	c=0

	mytree = ET.ElementTree(ET.fromstring(requests.get('http://www.mesdocumentsinterfaces.org/docs/img_trombi.xml').text))
	myroot = mytree.getroot()

	def onclick():
		Bulletin.window_bulletin()

	for x in myroot.findall('personne'):
		nom=x.find('nom').text
		img=x.find('image').text
		print(img)
		id=x.get('ID')
		photo.insert(c,tk.PhotoImage(file=img))
		buttontrombi.insert(c,tk.Button(root,text=nom, image=photo[c] , height=180, width=150,compound="top"))
		if(id=="DD"):
			print(id)
			buttontrombi.insert(c,tk.Button(root,text=nom, image=photo[c] , height=180, width=150,compound="top",command=onclick))
		if a>5 :
			b=b+1
			a=0
		
		buttontrombi[c].grid (row=b, column=a)
		a=a+1
		c=c+1

	root.mainloop()
#window_trombi()
