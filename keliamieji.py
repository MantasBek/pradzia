from tkinter import *

langas = Tk()


def keliamieji_metai():
    list = []
    for leap_year in range(int(laukas1.get()), int(laukas2.get())):
        if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
            list.append(leap_year)
    rezultatas["text"] = f"{list}"

uzrasas1 = Label(langas, text="Iveskite pirmus metus")
laukas1 = Entry(langas)
uzrasas2 = Label(langas, text="Iveskite antrus metus")
laukas2 = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=keliamieji_metai)
rezultatas = Label(langas, text="")
langas.iconbitmap(r"calendar.ico")

uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
uzrasas2.grid(row=1, column=0)
laukas2.grid(row=1, column=1)
mygtukas.grid(row=2, columnspan=2)
rezultatas.grid(row=3, columnspan=5)

langas.mainloop()