from tkinter import *
foablak=Tk()
def ujablak():
    ablak=Toplevel(foablak)
    szoveg1=Label(ablak, text="Felszín:")
    szoveg1.grid(row=0, column=0)
    szoveg2=Label(ablak, text="Térfogat:")
    szoveg2.grid(row=1, column=0)
    mezo1=Entry(ablak)
    mezo1.grid(row=0, column=1)
    mezo2=Entry(ablak)
    mezo2.grid(row=1, column=1)
    a=int(amezo.get())
    b=int(bmezo.get())
    c=int(cmezo.get())
    felszin=2*(a*b+b*c+c*a)
    terfogat=a*b*c
    mezo1.delete(0, END)
    mezo1.insert(0, felszin)
    mezo2.delete(0, END)
    mezo2.insert(0, terfogat)
    mezo1.configure(state="readonly")
    mezo2.configure(state="readonly")
    ablak.mainloop()
amezo=Entry(foablak)
amezo.grid(row=0, column=1)
amezoszoveg=Label(foablak, text="a:")
amezoszoveg.grid(row=0, column=0)
bmezo=Entry(foablak)
bmezo.grid(row=1, column=1)
bmezoszoveg=Label(foablak, text="b:")
bmezoszoveg.grid(row=1, column=0)
cmezo=Entry(foablak)
cmezo.grid(row=2, column=1)
cmezoszoveg=Label(foablak, text="c:")
cmezoszoveg.grid(row=2, column=0)
gomb1=Button(foablak, text="Számítás", command=ujablak)
gomb1.grid(row=3, column=1)
foablak.mainloop()