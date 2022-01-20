from tkinter import*
from tkinter import ttk
from tkinter.messagebox import *
tunniplaan={}
tunniplaan[tund]=kirjeldus
tunn=Tk()
def uus_aken(ind:int):
	if akyesno("Küsimus","Kas teen lahti?"):
		showinfo("Vastus","Teen lahti aken")
	else:
		showinfo("Vastus","Panen kinni aken")
		aken.destroy()
	uusaken=Toplevel()
	tabs=ttk.Notebook(uusaken)
#Päevad
Label(text="           ",font="Arial 20").grid(row=0,column=0)
Label(text="Esmaspäev",relief=RIDGE,font="Arial 20").grid(row=1,column=0)
Label(text="Teisipäev",relief=RIDGE,font="Arial 20").grid(row=2,column=0)
Label(text="Kolmapäev",relief=RIDGE,font="Arial 20").grid(row=3,column=0)
Label(text="Neljapäev",relief=RIDGE,font="Arial 20").grid(row=4,column=0)
Label(text="Reede",relief=RIDGE,font="Arial 20").grid(row=5,column=0)
#Tunnid
Label(text="0",relief=RIDGE,font="Arial 20").grid(row=0,column=1)
Label(text="1",relief=RIDGE,font="Arial 20").grid(row=0,column=2)
Label(text="2",relief=RIDGE,font="Arial 20").grid(row=0,column=3)
Label(text="3",relief=RIDGE,font="Arial 20").grid(row=0,column=4)
Label(text="4",relief=RIDGE,font="Arial 20").grid(row=0,column=5)
Label(text="5",relief=RIDGE,font="Arial 20").grid(row=0,column=6)
Label(text="6",relief=RIDGE,font="Arial 20").grid(row=0,column=7)
Label(text="7",relief=RIDGE,font="Arial 20").grid(row=0,column=8)
Label(text="8",relief=RIDGE,font="Arial 20").grid(row=0,column=9)
Label(text="9",relief=RIDGE,font="Arial 20").grid(row=0,column=10)
Label(text="10",relief=RIDGE,font="Arial 20").grid(row=0,column=11)
#Esmaspäev
Label(text="Eesti keel\n Tugiõpe",bg="Grey",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=1,column=2)
Label(text="Logistikateenused",bg="green",relief=RIDGE,font="Arial 20",width=20,height=3).grid(row=1,column=3,columnspan=2)
Label(text="Matemaatika",bg="pink",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=1,column=5)
Label(text="Matemaatika",bg="pink",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=1,column=6)
Label(text="           ",font="Arial 20",width=10,height=3).grid(row=1,column=7)
Label(text="Keel ja kirjandus",bg="Lightgreen",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=1,column=8)
Label(text="Keel ja kirjandus",bg="Lightgreen",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=1,column=9)
Label(text="Matemaatika\n Tugiõpe",bg="pink",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=1,column=10)
#Teisipäev
Label(text="Keemia\n Tugiõpe",bg="purple",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=2,column=2)
Label(text="Programmeerimise\n alused",bg="Lightblue",relief=RIDGE,font="Arial 20",width=30,height=3).grid(row=2,column=3,columnspan=3)
Label(text="           ",font="Arial 20",width=10,height=3).grid(row=2,column=6)
Label(text="Füüsika",bg="pink",relief=RIDGE,font="Arial 20",width=20,height=3).grid(row=2,column=7,columnspan=2)
#Kolmapäev
Label(text="Inglise keel\n Tugiõpe",bg="pink",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=3,column=2)
Label(text="Kunstained",bg="purple",relief=RIDGE,font="Arial 20",width=20,height=3).grid(row=3,column=3,columnspan=2)
Label(text="           ",font="Arial 20",width=10,height=3).grid(row=3,column=5)
Label(text="Kehaline kasvatus",bg="purple",relief=RIDGE,font="Arial 20",width=20,height=3).grid(row=3,column=6,columnspan=2)
#Neljapäev
Label(text="Logistikateenused",bg="green",relief=RIDGE,font="Arial 20",width=20,height=3).grid(row=4,column=2,columnspan=2)
Label(text="           ",font="Arial 20",width=10,height=3).grid(row=4,column=4)
Label(text="Programmeerimise\n alused",bg="Lightblue",relief=RIDGE,font="Arial 20",width=20,height=3).grid(row=4,column=5,columnspan=2)
Label(text="Arenduskeskkonna",bg="red",relief=RIDGE,font="Arial 20",width=20,height=3).grid(row=4,column=7,columnspan=2)
Label(text="Eesti keel",bg="grey",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=4,column=9)
Label(text="Eesti keel",bg="grey",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=4,column=10)
#Reede
Label(text="Arenduskeskkonna",bg="red",relief=RIDGE,font="Arial 20",width=20,height=3).grid(row=5,column=2,columnspan=2)
Label(text="Programmeerimise alused",bg="Lightblue",relief=RIDGE,font="Arial 20",width=65,height=3).grid(row=5,column=4,columnspan=5)
Label(text="Inglise keel",bg="lightgreen",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=5,column=9)
Label(text="Inglise keel",bg="Lightgreen",relief=RIDGE,font="Arial 20",width=10,height=3).grid(row=5,column=10)


















tunn.mainloop()
