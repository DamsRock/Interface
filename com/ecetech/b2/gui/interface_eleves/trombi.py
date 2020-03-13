def window_trombi():
	import tkinter as tk
	from lxml import etree
	import Bulletin


	#root = tk.Tk()
	root = tk.Toplevel()
	root.title('trombi')

	buttontrombi = []
	photo = []
	a=0
	b=0
	c=0

	mytree = etree.parse('img_trombi.xml')
	myroot = mytree.getroot()

	def onclick():
		Bulletin.window_bulletin()

	for x in myroot.findall ('personne') :
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
