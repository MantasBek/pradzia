from tkinter import *
from tkinter import ttk

langas = Tk()

langas.title("Sveikas")
praeita_atsakymas = StringVar()


def pasisveikinti():
    ivesta = f" Labas, {laukas.get()}!"
    praeita_atsakymas.set(ivesta)
    rezultatas["text"] = ivesta
    patvirtinimas["text"] = "Sukurta"


def isvalyti():
    rezultatas.config(text="")
    patvirtinimas["text"] = "Išvalyta"


def saugoma():
    rezultatas["text"] = praeita_atsakymas.get()
    patvirtinimas["text"] = "Atkurta"


def iseiti():
    langas.destroy()


meniu = Menu(langas)
submeniu = Menu(meniu, tearoff=0)
langas.config(menu=meniu)

uzrasas = Label(langas, text="Iveskite varda")
laukas = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=pasisveikinti)
rezultatas = Label(langas, text="")
patvirtinimas = Label(langas, text="")
langas.iconbitmap(r"wave.ico")

langas.bind("<Return>", lambda x: pasisveikinti())
langas.bind("<Escape>", lambda x: iseiti())

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti paskutinį", command=saugoma)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

uzrasas.grid(row=0, column=0)
laukas.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)
ttk.Separator(langas, orient="horizontal").grid(columnspan=3, sticky="ew")
patvirtinimas.grid(row=3, column=0)

langas.mainloop()