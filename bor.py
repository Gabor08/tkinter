from tkinter import *
foablak=Tk()
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
foablak.mainloop()