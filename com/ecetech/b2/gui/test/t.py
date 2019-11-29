def demande(phrase,mot):
	test=input('entrer une lettre: ')
	for i in range(4) :
		
		if (test!=(phrase[i])):
			mot=test+mot[i]
			
			print (mot[i])
		
	print (mot)
	
	
mot='*****'
phrase=('lapin')

while (mot!='lapin'):
	print (phrase)
	
	demande(phrase,mot)