from tkinter import *
foablak=Tk()
def ujablak():
    ablak=Toplevel(foablak)
    uzenet=Message(ablak, text="Készítette: Gipsz Jakab\nPiripócs\n2009.06.04", width=300)
    gomb2=Button(ablak, text="Kilépés", command=ablak.destroy)
    uzenet.pack()
    gomb2.pack()
    ablak.mainloop()
szoveg=Label(foablak, text="Kattints a gombra!")
szoveg.pack()
gomb1=Button(foablak, text="Névjegy", command=ujablak)
gomb1.pack()
foablak.mainloop()