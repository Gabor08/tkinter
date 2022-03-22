from tkinter import *
import math
def terfogat():
    sugar=int(mezo1.get())
    magassag=int(mezo2.get())
    terf=sugar*2*math.pi*magassag
    mezo3.insert(0,"{:.2f}".format(terf) + " cm3")
foablak=Tk()
mezo1=Entry(foablak)
mezo1.grid(row=0, column=1)
mezo1felirat=Label(foablak, text="Sugár (cm):")
mezo1felirat.grid(row=0, column=0)
mezo2=Entry(foablak)
mezo2.grid(row=1, column=1)
mezo2felirat=Label(foablak, text="Magasság (cm):")
mezo2felirat.grid(row=1, column=0)
kiszamit=Button(foablak, text="Kiszámít", command=terfogat)
kiszamit.grid(row=2, column=1)
mezo3=Entry(foablak)
mezo3.grid(row=3, column=1)
mezo3felirat=Label(foablak, text="Térfogat:")
mezo3felirat.grid(row=3, column=0)
foablak.mainloop()