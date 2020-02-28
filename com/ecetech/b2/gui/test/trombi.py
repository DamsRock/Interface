from Tkinter import * 
from functools import partial
from lxml import etree 



root = Tk()

root.geometry("1040x1000")


button = []
photo = []
a=0
b=0
c=0


mytree = etree.parse('img_trombi.xml')
myroot = mytree.getroot()


for x in myroot.findall ('personne') :
	
	nom=x.find('nom').text
	img=x.find('image').text
	photo.insert(c,PhotoImage(file=img))
	button.insert(c,Button(root,text=nom, image=photo[c] , height=300, width=200,compound="top"))
	
	if a>4 :
		b=b+1
		a=0
		
	button[c].grid (row=b, column=a)
	a=a+1
	c=c+1

	

root.mainloop()