from tkinter import *
from tkinter import Misc
from typing import Any, Literal

from RaceStat import RaceStat

stats = [
    RaceStat("1", "10:25:11", "Fini", "12:12:12", "12:45:25", "13:45:25", "14:45:25"),
    RaceStat("2", "9:15:52", "Fini", "16:55:45", "12:45:25", "13:45:25", "14:45:25"),
    RaceStat("3", "8:45:68", "Fini", "15:36:36", "12:45:25", "13:45:25", "14:45:25"),
    RaceStat("4", "9:55:46", "Fini", "12:43:52", "12:45:25", "13:45:25", "14:45:25"),
    RaceStat("5", "10:15:12", "Fini", "15:27:13", "12:45:25", "13:45:25", "14:45:25")
    ]

nbrsOfRows = len(stats)
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
            if i < len(stats):
                self.idRow = Label(self, text=stats[i].id, bd=1, relief="solid")
            else:
                self.idRow = Label(self, text="", bd=1, relief="solid")
            self.idRow.grid(row=(2 + i), column=1, sticky="nsew")


    ## Heure départ
        self.heure_depart = Label(self, text="Heure Départ", bg='grey', bd=1, relief="solid")
        self.heure_depart.grid(row=1, column=2, sticky="nsew")
    ## Heure départ rows
        for i in range(nbrsOfRows):
            if i < len(stats):
                self.heure_departRow = Label(self, text=stats[i].time, bd=1, relief="solid")
            else:
                self.heure_departRow = Label(self, text="", bd=1, relief="solid")
            self.heure_departRow.grid(row=(2 + i), column=2, sticky="nsew")


    ## État
        self.state = Label(self, text="État", bg='grey', bd=1, relief="solid")
        self.state.grid(row=1, column=3, sticky="nsew")
    ## État rows
        for i in range(nbrsOfRows):
            if i < len(stats):
                self.stateRow = Label(self, text=stats[i].state, bd=1, relief="solid")
            else:
                self.stateRow = Label(self, text="", bd=1, relief="solid")
            self.stateRow.grid(row=(2 + i), column=3, sticky="nsew")


    ## Capteur 1
        self.c1 = Label(self, text="Temps 1", bg='grey', bd=1, relief="solid")
        self.c1.grid(row=1, column=4, sticky="nsew")
    ## Capteur 1 rows
        for i in range(nbrsOfRows):
            if i < len(stats):
                self.c1TimeRow = Label(self, text=stats[i].c1, bd=1, relief="solid")
            else:
                self.c1TimeRow = Label(self, text="", bd=1, relief="solid")
            self.c1TimeRow.grid(row=(2 + i), column=4, sticky="nsew")

    ## Capteur 2
        self.c2 = Label(self, text="Temps 2", bg='grey', bd=1, relief="solid")
        self.c2.grid(row=1, column=5, sticky="nsew")
    ## Capteur 2 rows
        for i in range(nbrsOfRows):
            if i < len(stats):
                self.c2TimeRow = Label(self, text=stats[i].c2, bd=1, relief="solid")
            else:
                self.c2TimeRow = Label(self, text="", bd=1, relief="solid")
            self.c2TimeRow.grid(row=(2 + i), column=5, sticky="nsew")


    ## Capteur 3
        self.c3 = Label(self, text="Temps 3", bg='grey', bd=1, relief="solid")
        self.c3.grid(row=1, column=6, sticky="nsew")
    ## Capteur 3 rows
        for i in range(nbrsOfRows):
            if i < len(stats):
                self.c3TimeRow = Label(self, text=stats[i].c3, bd=1, relief="solid")
            else:
                self.c3TimeRow = Label(self, text="", bd=1, relief="solid")
            self.c3TimeRow.grid(row=(2 + i), column=6, sticky="nsew")


    ## Capteur 4
        self.c4 = Label(self, text="Temps 4", bg='grey', bd=1, relief="solid")
        self.c4.grid(row=1, column=7, sticky="nsew")
    ## Capteur 4 rows
        for i in range(nbrsOfRows):
            if i < len(stats):
                self.c4TimeRow = Label(self, text=stats[i].c4, bd=1, relief="solid")
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
        for stat in stats:
            print(stat.toString())

    def refresh(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()

root = Tk()
root.title('RacePi Interface')
root.geometry("500x300")
app = Application(root)
app.mainloop()