from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
import tkinter as tk
from PIL import *
monfichier = './random_image.png'

class Applicationpdf :
    def __init__(self):
        self.root = tk.Tk()

        ''' GENERATION DU SCHEMA AVEC UN CANVAS TKINTER '''
        schema = tk.Canvas()
        schema.pack()

        fi = tk.PhotoImage(file=monfichier) # ne pas utiliser le mot réservé file comme variable

        schema.create_image(0, 100, image=fi)

        schema.create_text(50, 110, text="125")
        schema.create_text(500, 300, text="68.3")

        enr = tk.Button(self.root, text="Exporter en PDF",command=self.enregistrer)
        enr.pack()

        self.root.mainloop()


    def enregistrer(self):
        filename = 'TEST.pdf'

        ''' GENERATION DU MEME SCHEMA AVEC UN CANVAS REPORTLAB'''
        pdf = canvas.Canvas(filename, pagesize=A4)

        pdf.drawImage(ImageReader(monfichier), 0, 100, 680, 300)

        pdf.setFont('Helvetica', 14)
        pdf.setFillColor(colors.red)

        pdf.drawString(50, 110, "125")
        pdf.drawString(500, 300, "68.3")

        pdf.showPage()

        pdf.save()


Applicationpdf()
