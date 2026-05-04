from tkinter import *
from tkinter import Misc
from typing import Any, Literal

ids = ["0001", "0002", "0003", "0004", "0005", "0006", "0007"]

times = ["10:45:25", "11:25:36", "11:25:45", "11:34:22", "12:52:53", "13:54:23"]

## Sois "Fini", "Faux départ" ou "Incomplet"
states = ["Fini", "Faux départ", "Incomplet", "Fini", "Incomplet", "Fini"]

c1Times = ["11:45:25", "12:25:36", "12:25:45", "12:34:22", "13:52:53", "14:54:23"]

c2Times = ["12:45:25", "13:25:36", "13:25:45", "13:34:22", "14:52:53", "15:54:23"]

c3Times = ["13:45:25", "14:25:36", "14:25:45", "14:34:22", "15:52:53", "16:54:23"]

c4Times = ["14:45:25", "15:25:36", "15:25:45", "15:34:22", "16:52:53", "17:54:23"]

nbrsOfRows = len(max(ids, times, key=len))
print(nbrsOfRows)

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        ## Titre du tableau
        self.titre = Label(self, text="Derniers Résultats", font=("Times", 15))
        self.titre.grid(row=0, column=0, columnspan=3, sticky="nsew")

    ## Tableau
    ## Id
        self.id = Label(self, text="Id", bg='grey', bd=1, relief="solid")
        self.id.grid(row=1, column=1, sticky="nsew")
    ## Id rows
        for i in range(nbrsOfRows):
            if i < len(ids):
                self.idRow = Label(self, text=ids[i], bd=1, relief="solid")
            else:
                self.idRow = Label(self, text="", bd=1, relief="solid")
            self.idRow.grid(row=(2 + i), column=1, sticky="nsew")


    ## Heure départ
        self.heure_depart = Label(self, text="Heure Départ", bg='grey', bd=1, relief="solid")
        self.heure_depart.grid(row=1, column=2, sticky="nsew")
    ## Heure départ rows
        for i in range(nbrsOfRows):
            if i < len(times):
                self.heure_departRow = Label(self, text=times[i], bd=1, relief="solid")
            else:
                self.heure_departRow = Label(self, text="", bd=1, relief="solid")
            self.heure_departRow.grid(row=(2 + i), column=2, sticky="nsew")


    ## État
        self.state = Label(self, text="État", bg='grey', bd=1, relief="solid")
        self.state.grid(row=1, column=3, sticky="nsew")
    ## État rows
        for i in range(nbrsOfRows):
            if i < len(states):
                self.stateRow = Label(self, text=states[i], bd=1, relief="solid")
            else:
                self.stateRow = Label(self, text="", bd=1, relief="solid")
            self.stateRow.grid(row=(2 + i), column=3, sticky="nsew")


    ## Capteur 1
        self.c1 = Label(self, text="Temps 1", bg='grey', bd=1, relief="solid")
        self.c1.grid(row=1, column=4, sticky="nsew")
    ## Capteur 1 rows
        for i in range(nbrsOfRows):
            if i < len(c1Times):
                self.c1TimeRow = Label(self, text=c1Times[i], bd=1, relief="solid")
            else:
                self.c1TimeRow = Label(self, text="", bd=1, relief="solid")
            self.c1TimeRow.grid(row=(2 + i), column=4, sticky="nsew")

    ## Capteur 2
        self.c2 = Label(self, text="Temps 2", bg='grey', bd=1, relief="solid")
        self.c2.grid(row=1, column=5, sticky="nsew")
    ## Capteur 2 rows
        for i in range(nbrsOfRows):
            if i < len(c2Times):
                self.c2TimeRow = Label(self, text=c2Times[i], bd=1, relief="solid")
            else:
                self.c2TimeRow = Label(self, text="", bd=1, relief="solid")
            self.c2TimeRow.grid(row=(2 + i), column=5, sticky="nsew")


    ## Capteur 3
        self.c3 = Label(self, text="Temps 3", bg='grey', bd=1, relief="solid")
        self.c3.grid(row=1, column=6, sticky="nsew")
    ## Capteur 3 rows
        for i in range(nbrsOfRows):
            if i < len(c3Times):
                self.c3TimeRow = Label(self, text=c3Times[i], bd=1, relief="solid")
            else:
                self.c3TimeRow = Label(self, text="", bd=1, relief="solid")
            self.c3TimeRow.grid(row=(2 + i), column=6, sticky="nsew")


    ## Capteur 4
        self.c4 = Label(self, text="Temps 4", bg='grey', bd=1, relief="solid")
        self.c4.grid(row=1, column=7, sticky="nsew")
    ## Capteur 4 rows
        for i in range(nbrsOfRows):
            if i < len(c4Times):
                self.c4TimeRow = Label(self, text=c4Times[i], bd=1, relief="solid")
            else:
                self.c4TimeRow = Label(self, text="", bd=1, relief="solid")
            self.c4TimeRow.grid(row=(2 + i), column=7, sticky="nsew")


    ## Print space
        self.printSpace = Label(self)
        self.printSpace.grid(row=(nbrsOfRows + 3), column=2, sticky="nsew")

    ## Bouton Démarrer
        self.startBtn = Button(self, text="Démarrer la course", command=self.StartRace)
        self.startBtn.grid(row=(nbrsOfRows + 2), column=2, sticky="nsew")

    def print(self, message):
        self.printSpace.config(text=message)

    def StartRace(self):
        print("Starting the Race...")
        ids.append("000" + (str)(len(ids) + 1))

        global nbrsOfRows
        nbrsOfRows = len(max(ids, times, key=len))

        self.refresh()

    def refresh(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()

root = Tk()
root.title('RacePi Interface')
root.geometry("500x300")
app = Application(root)
app.mainloop()