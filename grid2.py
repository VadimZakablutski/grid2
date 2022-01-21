from tkinter import*
from tkinter import ttk
from tkinter.messagebox import *
tunn=Tk()
def uus_aken(ind:int):
	if akyesno("Küsimus","Kas teen lahti?"):
		showinfo("Vastus","Teen lahti aken")
	else:
		showinfo("Vastus","Panen kinni aken")
		aken.destroy()
	uusaken=Toplevel()
	tabs=ttk.Notebook(uusaken)
def okno():
	showinfo(title="Oкно",message="Свободное время")
def estt():
	showinfo(title="Доп.Эстонский",message="Доп.урок\n Учитель - Olesja Ojamäe\n Кабинет - B 234")
def log():
	showinfo(title="Логистика",message="Основной урок\n Учитель - Inessa Klemanskaja\n Кабинет - B 002")
def mat():
	showinfo(title="Математика",message="Основной урок\n Учитель - Nadewda Voronova\n Кабинет - B 133")
def matt():
	showinfo(title="Доп.Математика",message="Доп.урок\n Учитель - Nadewda Voronova\n Кабинет - B 133")
def rus():
	showinfo(title="Русский",message="Основной урок\n Учитель - Ljudmila Mikhailova\n Кабинет - B 221")
def kemt():
	showinfo(title="Доп.Химия",message="Основной урок\n Учитель - Svetlana Pesestkaja\n Кабинет - B 144")
def progr():
	showinfo(title="Програмирование",message="Основной урок\n Учитель - Marina Oleinik\n Кабинет - E 07")
def füsik():
	showinfo(title="Физика",message="Основной урок\n Учитель - Nadewda Voronova\n Кабинет - B 133")
def kunst():
	showinfo(title="Исскуство",message="Основной урок\n Учитель - Aleksandrova\n Кабинет - B 232")
def fizra():
	showinfo(title="Физкультура",message="Основной урок\n Учитель - Maksim\n Кабинет - Zal A")
def rak():
	showinfo(title="Ракендусттарквара",message="Основной урок\n Учитель - Merkulova\n Кабинет - E 10")
def est():
	showinfo(title="Эстонский",message="Основной урок\n Учитель - Olesja Ojamäe\n Кабинет - B 234")
def anglt():
	showinfo(title="Доп.Английский",message="Доп.урок\n Учитель - Olga Borodina\n Кабинет - B 227")
def angl():
	showinfo(title="Английский",message="Основной урок\n Учитель - Olga Borodina\n Кабинет - B 227")


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
Button(text="Eesti keel\n Tugiõpe",bg="Grey",relief=RIDGE,font="Arial 20",width=10,height=3,command=estt).grid(row=1,column=2)
Button(text="Logistikateenused",bg="green",relief=RIDGE,font="Arial 20",width=20,height=3,command=log).grid(row=1,column=3,columnspan=2)
Button(text="Matemaatika",bg="pink",relief=RIDGE,font="Arial 20",width=10,height=3,command=mat).grid(row=1,column=5)
Button(text="Matemaatika",bg="pink",relief=RIDGE,font="Arial 20",width=10,height=3,command=mat).grid(row=1,column=6)
Button(text="           ",font="Arial 20",width=10,height=3,command=okno).grid(row=1,column=7)
Button(text="Keel ja kirjandus",bg="Lightgreen",relief=RIDGE,font="Arial 20",width=10,height=3,command=rus).grid(row=1,column=8)
Button(text="Keel ja kirjandus",bg="Lightgreen",relief=RIDGE,font="Arial 20",width=10,height=3,command=rus).grid(row=1,column=9)
Button(text="Matemaatika\n Tugiõpe",bg="pink",relief=RIDGE,font="Arial 20",width=10,height=3,command=matt).grid(row=1,column=10)
#Teisipäev
Button(text="Keemia\n Tugiõpe",bg="purple",relief=RIDGE,font="Arial 20",width=10,height=3,command=kemt).grid(row=2,column=2)
Button(text="Programmeerimise\n alused",bg="Lightblue",relief=RIDGE,font="Arial 20",width=30,height=3,command=progr).grid(row=2,column=3,columnspan=3)
Button(text="           ",font="Arial 20",width=10,height=3,command=okno).grid(row=2,column=6)
Button(text="Füüsika",bg="pink",relief=RIDGE,font="Arial 20",width=20,height=3,command=füsik).grid(row=2,column=7,columnspan=2)
#Kolmapäev
Button(text="Inglise keel\n Tugiõpe",bg="pink",relief=RIDGE,font="Arial 20",width=10,height=3,command=anglt).grid(row=3,column=2)
Button(text="Kunstained",bg="purple",relief=RIDGE,font="Arial 20",width=20,height=3,command=kunst).grid(row=3,column=3,columnspan=2)
Button(text="           ",font="Arial 20",width=10,height=3,command=okno).grid(row=3,column=5)
Button(text="Kehaline kasvatus",bg="purple",relief=RIDGE,font="Arial 20",width=20,height=3,command=fizra).grid(row=3,column=6,columnspan=2)
#Neljapäev
Button(text="Logistikateenused",bg="green",relief=RIDGE,font="Arial 20",width=20,height=3,command=log).grid(row=4,column=2,columnspan=2)
Button(text="           ",font="Arial 20",width=10,height=3,command=okno).grid(row=4,column=4)
Button(text="Programmeerimise\n alused",bg="Lightblue",relief=RIDGE,font="Arial 20",width=20,height=3,command=progr).grid(row=4,column=5,columnspan=2)
Button(text="Arenduskeskkonna",bg="red",relief=RIDGE,font="Arial 20",width=20,height=3,command=rak).grid(row=4,column=7,columnspan=2)
Button(text="Eesti keel",bg="grey",relief=RIDGE,font="Arial 20",width=10,height=3,command=est).grid(row=4,column=9)
Button(text="Eesti keel",bg="grey",relief=RIDGE,font="Arial 20",width=10,height=3,command=est).grid(row=4,column=10)
#Reede
Button(text="Arenduskeskkonna",bg="red",relief=RIDGE,font="Arial 20",width=20,height=3,command=rak).grid(row=5,column=2,columnspan=2)
Button(text="Programmeerimise alused",bg="Lightblue",relief=RIDGE,font="Arial 20",width=65,height=3,command=progr).grid(row=5,column=4,columnspan=5)
Button(text="Inglise keel",bg="lightgreen",relief=RIDGE,font="Arial 20",width=10,height=3,command=angl).grid(row=5,column=9)
Button(text="Inglise keel",bg="Lightgreen",relief=RIDGE,font="Arial 20",width=10,height=3,command=angl).grid(row=5,column=10)


















tunn.mainloop()
