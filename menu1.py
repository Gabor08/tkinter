from tkinter import *
import math
foablak=Tk()
foablak.minsize(width=300, height=100)
def nevjegy():
    ablak=Toplevel(foablak)
    uzenet=Message(ablak, text="Készítette: Gipsz Jakab\nPiripócs\n2009.06.04", width=300)
    gomb2=Button(ablak, text="Kilépés", command=ablak.destroy)
    uzenet.pack()
    gomb2.pack()
    ablak.mainloop()
def felszin():
    def szamitas():
        a=int(amezo.get())
        b=int(bmezo.get())
        c=int(cmezo.get())
        mezo.delete(0, END)
        felszin=2*(a*b+b*c+c*a)
        if a>0 and b>0 and c>0:
            mezo.insert(0, int(felszin))
        else:
            mezo.insert(0, "Nem lehet mínusz vagy 0 az éle.")
    ablak=Toplevel(foablak)
    amezo=Entry(ablak)
    amezo.grid(row=0, column=1)
    amezoszoveg=Label(ablak, text="a:")
    amezoszoveg.grid(row=0, column=0)
    bmezo=Entry(ablak)
    bmezo.grid(row=1, column=1)
    bmezoszoveg=Label(ablak, text="b:")
    bmezoszoveg.grid(row=1, column=0)
    cmezo=Entry(ablak)
    cmezo.grid(row=2, column=1)
    cmezoszoveg=Label(ablak, text="c:")
    cmezoszoveg.grid(row=2, column=0)
    gomb1=Button(ablak, text="Számítás", command=szamitas)
    gomb1.grid(row=3, column=1)
    mezo=Entry(ablak)
    mezo.grid(row=4, column=1)
    mezofelirat=Label(ablak, text="Eredmény:")
    mezofelirat.grid(row=4, column=0)
def terfogat():
    def szamitas():
        a=int(amezo.get())
        b=int(bmezo.get())
        c=int(cmezo.get())
        terfogat=a*b*c
        mezo.delete(0, END)
        if a>0 and b>0 and c>0:
            mezo.insert(0, int(terfogat))
        else:
            mezo.insert(0, "Nem lehet mínusz vagy 0 az éle.")
    ablak=Toplevel(foablak)
    amezo=Entry(ablak)
    amezo.grid(row=0, column=1)
    amezoszoveg=Label(ablak, text="a:")
    amezoszoveg.grid(row=0, column=0)
    bmezo=Entry(ablak)
    bmezo.grid(row=1, column=1)
    bmezoszoveg=Label(ablak, text="b:")
    bmezoszoveg.grid(row=1, column=0)
    cmezo=Entry(ablak)
    cmezo.grid(row=2, column=1)
    cmezoszoveg=Label(ablak, text="c:")
    cmezoszoveg.grid(row=2, column=0)
    gomb1=Button(ablak, text="Számítás", command=szamitas)
    gomb1.grid(row=3, column=1)
    mezo=Entry(ablak)
    mezo.grid(row=4, column=1)
    mezofelirat=Label(ablak, text="Eredmény:")
    mezofelirat.grid(row=4, column=0)
def hengerterfogat():
    def szamitas():
        sugar=int(amezo.get())
        magassag=int(bmezo.get())
        terf=sugar**2*math.pi*magassag
        mezo.delete(0, END)
        if sugar>0 and magassag>0:
            mezo.insert(0, "{:.2f}".format(int(terf)))
        else:
            mezo.insert(0, "Nem lehet mínusz vagy 0 sem a magasság, sem a sugár.")
    ablak=Toplevel(foablak)
    amezo=Entry(ablak)
    amezo.grid(row=0, column=1)
    amezoszoveg=Label(ablak, text="Sugár:")
    amezoszoveg.grid(row=0, column=0)
    bmezo=Entry(ablak)
    bmezo.grid(row=1, column=1)
    bmezoszoveg=Label(ablak, text="Magasság:")
    bmezoszoveg.grid(row=1, column=0)
    gomb1=Button(ablak, text="Számítás", command=szamitas)
    gomb1.grid(row=2, column=1)
    mezo=Entry(ablak)
    mezo.grid(row=3, column=1)
    mezofelirat=Label(ablak, text="Eredmény:")
    mezofelirat.grid(row=3, column=0)
def hengerfelszin():
    def szamitas():
        sugar=int(amezo.get())
        magassag=int(bmezo.get())
        felszin=(2*sugar**2*math.pi)+(2*sugar*math.pi*magassag)
        mezo.delete(0, END)
        if sugar>0 and magassag>0:
            mezo.insert(0, "{:.2f}".format(int(felszin)))
        else:
            mezo.insert(0, "Nem lehet mínusz vagy 0 sem a magasság, sem a sugár.")
    ablak=Toplevel(foablak)
    amezo=Entry(ablak)
    amezo.grid(row=0, column=1)
    amezoszoveg=Label(ablak, text="Sugár:")
    amezoszoveg.grid(row=0, column=0)
    bmezo=Entry(ablak)
    bmezo.grid(row=1, column=1)
    bmezoszoveg=Label(ablak, text="Magasság:")
    bmezoszoveg.grid(row=1, column=0)
    gomb1=Button(ablak, text="Számítás", command=szamitas)
    gomb1.grid(row=2, column=1)
    mezo=Entry(ablak)
    mezo.grid(row=3, column=1)
    mezofelirat=Label(ablak, text="Eredmény:")
    mezofelirat.grid(row=3, column=0)
menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)
menu1=Menubutton(menusor, text="Fájl")
menu1.pack(side=LEFT)
fajl=Menu(menu1)
fajl.add_command(label="Névjegy", command=nevjegy)
fajl.add_command(label="Kilépés", command=foablak.destroy)
menu1.config(menu=fajl)
menu2=Menubutton(menusor, text="Téglatest")
menu2.pack(side=LEFT)
teglatest=Menu(menu2)
teglatest.add_command(label="Felszín", command=felszin)
teglatest.add_command(label="Térfogat", command=terfogat)
menu2.config(menu=teglatest)
menu3=Menubutton(menusor, text="Henger")
menu3.pack(side=LEFT)
henger=Menu(menu3)
henger.add_command(label="Felszín", command=hengerfelszin)
henger.add_command(label="Térfogat", command=hengerterfogat)
menu3.config(menu=henger)
foablak.mainloop()