from tkinter import *

#la création de cette fonction permet l'affichage d'un image
def image():
    photo = PhotoImage(file="random_image.png") # l'importation de la photo photo ce fait ici
    profil = PhotoImage(file="IMAG0753png.png")
    canvas = Canvas(gui, width=700, height=500)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.grid(column=1, row=0)
    canvas.create_image(0, 0, anchor=NW, image=profil)
    canvas.grid(column=2, row=0)
    canvas.pack()
    canvas.pack()
    gui.mainloop()

gui = Tk()
gui.geometry("700x700")
gui.title("Biographique")
gui.iconphoto(image())
champ = Label(gui, text="Lorem ipsum dolor sit amet")###, consectetur adipiscing elit. Aenean euismod bibendum laoreet. Proin gravida dolor sit amet lacus accumsan et viverra justo commodo. Proin sodales pulvinar sic tempor. Sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam fermentum, nulla luctus pharetra vulputate, felis tellus mollis orci, sed rhoncus pronin sapien nunc accuan eget.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean euismod bibendum laoreet. Proin gravida dolor sit amet lacus accumsan et viverra justo commodo. Proin sodales pulvinar sic tempor. Sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam fermentum, nulla luctus pharetra vulputate, felis tellus mollis orci, sed rhoncus pronin sapien nunc accuan eget.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean euismod bibendum laoreet. Proin gravida dolor sit amet lacus accumsan et viverra justo commodo. Proin sodales pulvinar sic tempor. Sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam fermentum, nulla luctus pharetra vulputate, felis tellus mollis orci, sed rhoncus pronin sapien nunc accuan eget.")
champ.grid(column=0, row=0)
gui.pack(champ)

gui.mainloop()
