from tkinter import *
import math
foablak=Tk()
def szamitasok():
    negyedikmezo.delete(0, END)
    sugar=int(masodikmezo.get())
    magas=int(harmadikmezo.get())
    terf=math.pi*sugar**2*magas
    liter=terf/1000
    bor=int(elsomezo.get())
    otodikmezo.insert(0, "{:.0f}".format(liter)+" l")
    if bor>liter:
        negyedikmezo.insert(0, "Túl sok a bor.")
    else:
        mennyimeg=liter-bor
        negyedikmezo.insert(0, "{:.0f}".format(mennyimeg)+" l")
elsomezo=Entry(foablak)
elsomezo.grid(row=0, column=1)
elsomezofelirat=Label(foablak, text="Bor mennyisége (l): ")
elsomezofelirat.grid(row=0, column=0)
masodikmezo=Entry(foablak)
masodikmezo.grid(row=1, column=1)
masodikmezofelirat=Label(foablak, text="Hordó sugara (cm): ")
masodikmezofelirat.grid(row=1, column=0)
harmadikmezo=Entry(foablak)
harmadikmezo.grid(row=2, column=1)
harmadikmezofelirat=Label(foablak, text="Hordó magassága (cm): ")
harmadikmezofelirat.grid(row=2, column=0)
gomb=Button(foablak, text="Kiszámít", command=szamitasok)
gomb.grid(row=3, column=1)
negyedikmezo=Entry(foablak)
negyedikmezo.grid(row=5, column=1)
otodikmezo=Entry(foablak)
otodikmezo.grid(row=4, column=1)
foablak.mainloop()