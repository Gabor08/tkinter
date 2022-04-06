from tkinter import *
foablak=Tk()
def ujablak():
    ablak=Toplevel(foablak)
    
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
foablak.mainloop()