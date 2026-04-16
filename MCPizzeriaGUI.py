# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
# MCpizzaria
#
#
# Vul hier jullie namen in:
# ruben harms
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------
def zoekKlant():
    #haal de ingevoerde_klantnaam op uit het invoerveld
    # en gebruik dit om met SQL de klant in database te vinden
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    print(gevonden_klanten) # om te testen
    
    invoerveldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
    invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
    for rij in gevonden_klanten: #voor elke rij dat de query oplevert
        #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
        invoerveldKlantNr.insert(END, rij[0])
        #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
        invoerveldKlantnaam.insert(END, rij[1])

def toonMenuInListbox():
    ListboxMenu.delete(0, END) #maak de listbox leeg
    pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
    for regel in pizza_tabel:
        ListboxMenu.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu
        ListboxMenu.insert(0, "ID Gerecht Prijs")

def haalGeselecteerdeRijOp(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = ListboxMenu.curselection()[0]
    #haal tekst uit die regel
    geselecteerdeTekst = ListboxMenu.get(geselecteerdeRegelInLijst)
    #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerveldGeselecteerdePizza.delete(0, END)
    #zet tekst in veld
    invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst)

#voeg de bestelling van klant met gekozen pizza en aantal toe
#in de winkelwagentabel
#en toon de bestelling in de listbox op het scherm
def voegToeAanWinkelWagen():
    klantNr = invoerveldKlantNr.get()
    gerechtID = invoerveldGeselecteerdePizza.get()
    aantal = optionMenuPizzaAantal.cget()
    MCPizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal )
    winkelwagen_tabel = MCPizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
    ListboxWinkelwagen.delete(0, END) #listbox eerst even leeg maken
    for regel in winkelwagen_tabel:
        ListboxWinkelwagen.insert(END, regel)

### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

labelIntro = Label(venster, text="Welkom!", bg="lightblue")
labelIntro.grid(row=0, column=0, sticky="W")
knopSluit = Button(venster, text="Sluiten",width=12,command=venster.destroy, bg="red")
knopSluit.grid(row=17, column=4)

labelPizza = Label(venster, text="Gekozen pizza", bg="lightblue")
labelPizza.grid(row=8, column=0, sticky="W")
invoerveldGeselecteerdePizza = Entry(venster)
invoerveldGeselecteerdePizza.grid(row=8, column=1, sticky="W")

labelKlantnaam = Label(venster, text="Klantnaam!", bg="lightblue")
labelKlantnaam.grid(row=1, column=0, sticky="W")
ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")
invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

knopZoekOpKlantnaam = Button(venster, text="Zoek klant", width=12, command=zoekKlant, bg="lightblue")
knopZoekOpKlantnaam.grid(row=1, column=4)

ListboxMenu = Listbox(venster, height=6, width=50, bg="lightblue")
ListboxMenu.grid(row=2, column=1, rowspan=6, columnspan=2, sticky="W")
ListboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

knopToonPizzas = Button(venster, text="Toon alle pizza’s", width=12, command=toonMenuInListbox, bg="lightblue")
knopToonPizzas.grid(row=3, column=4)

aantalGekozen = IntVar()
aantalGekozen.set(1)
optionMenuPizzaAantal = OptionMenu(venster, aantalGekozen, 1,2,3)
optionMenuPizzaAantal.grid(row=9, column=1, sticky="W")

VoegToeWinkelwagen = Button(venster, text="Voeg toe aan winkelwagen", command=voegToeAanWinkelWagen, bg="lightblue")
VoegToeWinkelwagen.grid(row=11, column=0, sticky="W")

ListboxWinkelwagen = Listbox(venster, height=6, width=50, bg="lightblue")
ListboxWinkelwagen.grid(row=12, column=1, rowspan=6, columnspan=2, sticky="W")
ListboxWinkelwagen.bind("<<ListboxSelect>>", voegToeAanWinkelWagen)



#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
