
# erstellen von Funktionen


def getraenke ():
    # weitere lokale Variablen // da diese durch die auswahl definiert werden

    dateiName = getraenkName + txt[0:]
    print(dateiName)
    dateiNamebez = bez[:3] + getraenkName + txt[0:]
    print(dateiNamebez)

    # getränke datei in einer liste öffnen , dann aufspliten und da mehrere zutaten vorhanden sind,
    # in einen dict container speichern

    f = open(dateiName, "r")
    inhalt_getraenk = f.readlines()
    f.close()
    #    print(inhalt_getraenk)
    for i in range(len(inhalt_getraenk)):
        c = inhalt_getraenk[i].split()
        #        print(c)
        getraenk[(c[0])] = int(c[1])

# wasser vorrat öffnen und wert in int / zahl umwandeln

    f = open("wasser.txt", "r")
    wasser = f.readlines()
    f.close()
    wasser = int(wasser[0])

# wenn espresso oder Kaffee im getränk vorhanden sind sollen die ml vom wasser vorrat abgezogn werden

    if "Espresso" in getraenk:
        wasser = wasser - getraenk["Espresso"]

    if "Kaffee" in getraenk:
        wasser = wasser - getraenk["Kaffee"]
    wasser = str(wasser)

# überschreiben des wasser vorrats nach abzug der bezugsmenge

    f = open("wasser.txt", "w")
    f.write(wasser)
    f.close()

# öffnen des Bohnenvorrats / umwandeln des wertes in int/  und abzug einer bohnen menge in gramm

    f = open("bohnen.txt", "r")
    bohnen = f.readlines()
    f.close()
    bohnen = int(bohnen[0])
    if "Espresso" in getraenk:
        bohnen = bohnen - 20
    if "Kaffee" in getraenk:
        bohnen = bohnen - 20

# umwandeln des wertes in einen string

    bohnen = str(bohnen)

# schreiben des neuen vorrates

    f = open("bohnen.txt", "w")
    f.write(bohnen)
    f.close()

# öffnen des Milch vorrates / umwandeln in eine Zahl / abzug der bezugsmenge

    f = open("milchvorrat.txt", "r")
    Milch = f.readlines()
    f.close()
    Milch = int(Milch[0])
    if "Milch" in getraenk:
        Milch = Milch - getraenk["Milch"]

# umwandeln des ergebnisses in einen string

    Milch = str(Milch)

# schreiben des neuen milchvorrat wertes

    f = open("milchvorrat.txt", "w")
    f.write(Milch)
    f.close()

# das zählen der Bezüge... vorsicht die txt darf nicht leer sein eine "0" muss schon vorhanden sein
#    wichtig für Werkseinstellungen.

    f = open(dateiNamebez, "r")
    bezug = f.readlines()
    f.close()
    bezug = int(bezug[0]) + 1
    bezug = str(bezug)
    f = open(dateiNamebez, "w")
    f.write(bezug)
    f.close()

def mengen():

# um die zutaten des Getränkes zu verändern,  wird der Inhalt in einem dict gespeichert

    dateiNameMenge = getraenkNameMenge + txt[0:]
    #            print(dateiNameMenge)
# öffnen der datei und einlesen der daten in einer liste

    f = open(dateiNameMenge, "r")
    inhalt_getraenk_menge = f.readlines()
    f.close()

# in durchläufen die daten spliten und in ein dict speichern

    for i in range(len(inhalt_getraenk_menge)):
        c = inhalt_getraenk_menge[i].split()
        getraenk[(c[0])] = int(c[1])

# abfrage über den in-operator / löschen und schreiben des neuen wertes

    if "Espresso" in getraenk:
        espresso = int(input("Gib bitte die neue Menge Espresso ein: "))
        del getraenk["Espresso"]
        getraenk["Espresso"] = espresso
    if "Kaffee" in getraenk:
        kaffee = int(input("Gib bitte die neue Menge Kaffee ein: "))
        del getraenk["Kaffee"]
        getraenk["Kaffee"] = kaffee
    if "Milch" in getraenk:
        milch = int(input("Gib bitte die neue Menge Milch ein: "))
        del getraenk["Milch"]
        getraenk["Milch"] = milch

# umwandeln des dictionary in einen string

    liste_getraenk = str(getraenk)

# formatieren des string, damit eine verwendbare txt datei entsteht

    liste_getraenk = liste_getraenk.replace(",", "\n")
    liste_getraenk = liste_getraenk.replace("{", "")
    liste_getraenk = liste_getraenk.replace("}", "")
    liste_getraenk = liste_getraenk.replace(" '", "")
    liste_getraenk = liste_getraenk.replace("'", "")
    liste_getraenk = liste_getraenk.replace(":", "")

# überschreiben der auswahl datei...

    f = open(dateiNameMenge, "w")
    f.write(liste_getraenk + "\n")
    f.close()
    #    print(getraenk)


# globale container und Variablen erzeugen

weiter = "ja"
wasser = []
bohnen = []
Milch = []
dateiName = ""
dateiNamebez = ""
dateiNameMenge = ""
auswahlWerk = ""
getraenk = dict()
#bezug = dict(Espresso=0, Kaffee=0, KaffeeLatte=0, LatteMacchiato=0, Capuccino=0, flatWhite=0, Milchschaum=0, heißeMilch=0)
espresso = 0
kaffee = 0
milch = 0

# interakrion mit Benutzer

nameAnwender = input("Gib bitte deinen Namen ein: ")
print("Hallo " + nameAnwender + ", herzlich willkommen bei deinem Kaffeevollautomat.")

# while Schleife für " zurück zum Hauptmenü //

while weiter == "ja":

# auswahl des kaffee´s

    print("1 = Espresso, 2 = Kaffee, 3 = Capuccino, 4 = flat white, 5 = Kaffee Latte, 6 = Latte Macchiato"
          " 7 = Milchschaum, 8 = heiße Milch, 0 = Hauptmenü")
    auswahl = input(nameAnwender + ", gib bitte ein, welches Getränk du beziehen möchtest: ")

    # Lokale container und Variablen

    getraenkName = ""
    txt = ".txt"
    bez = "bez"

# nach auswahlnummer erzeugen des dateinamen ohn suffix... einfach nur... um es auszuprobieren
# einbinden der funktion getraenke(), um Milch, Wasser und Bohnen abzurechnen

    if auswahl == "1":
        print("Dein Espresso wird ausgegeben.")
        getraenkName = "espresso"
        getraenke()
    if auswahl == "2":
        print("Dein Kaffe wird ausgegeben.")
        getraenkName = "kaffee"
        getraenke()
    if auswahl == "3":
        print("Dein Capuccino wird ausgegeben.")
        getraenkName = "capuccino"
        getraenke()
    if auswahl == "4":
        print("Dein flat white wird ausgegeben.")
        getraenkName = "flatWhite"
        getraenke()
    if auswahl == "5":
        print("Dein Kaffee Latte wird ausgegeben.")
        getraenkName = "kaffeeLatte"
        getraenke()
    if auswahl == "6":
        print("Dein Latte Macchiato wird ausgegeben.")
        getraenkName = "latteMacchiato"
        getraenke()
    if auswahl == "7":
        print("Dein Milchschaum wird ausgegeben.")
        getraenkName = "Milchschaum"
        getraenke()
    if auswahl == "8":
        print("Deine heiße Milch wird ausgegeben.")
        getraenkName = "Milch"
        getraenke()

## geht ins untermenü / geräte einstellungen

    if auswahl == "0":
        print(nameAnwender + ", Du befindest Dich in den Einstellungen"
                             " 1 = Milch Wasser Bohnen auffüllen, 2 = Mengen verändern, 3 = Bezüge,"
                             " 4 = Werkseinstellungen, 0 = Hauptmenü.")
        auswahlEinstell = input("Bitte gib eine Zahl ein: ")

## befüllen von Milch Wasser und Bohnen

        if auswahlEinstell == "1":
            print("Hallo " + nameAnwender + ", gib bitte ein was Du befuellen möchtest"
                                            " 1 = Milch, 2 = Wasser, 3 = Bohnen.")
            auswahlbef = input("Gib bitte eine Zahl ein: ")

# öffnen und überschreiben der vorrats dateinen

            if auswahlbef == "1":
                print("Der Milchvorrat wurde aufgefüllt.")
                f = open("milchvorrat.txt", "w")
                f.write("1000")
                f.close()

            if auswahlbef == "2":
                print("Der Wasserbehälter wurde aufgefüllt.")
                f = open("wasser.txt", "w")
                f.write("1000")
                f.close()

            if auswahlbef == "3":
                print("Der Bohnenbehälter wurde aufgefüllt.")
                f = open("bohnen.txt", "w")
                f.write("250")
                f.close()

## anpassen der Getränke

        if auswahlEinstell == "2":

            print("Welche Kaffeespezialität möchtest du anpassen?"
                  " 1 = Espresso, 2 = Kaffee, 3 = Capuccino, 4 = flat white, 5 = Kaffee Latte, 6 = Latte Macchiato"
                  " 7 = Milchschaum, 8 = heiße Milch")
            auswahlMenge = input(nameAnwender + ", gib bitte eine Zahl ein: ")

# erstellen der lokalen Container

            getraenkNameMenge = ""
            txt = ".txt"

# über sie auswahl definieren des dateinamens ohne suffix und einbinden der funktion mengen()

            if auswahlMenge == "1":
                print("Dein Espresso wird angepasst.")
                getraenkNameMenge = "espresso"
                mengen()
            if auswahlMenge == "2":
                print("Dein Kaffe wird angepasst.")
                getraenkNameMenge = "kaffee"
                mengen()
            if auswahlMenge == "3":
                print("Dein Capuccino wird angepasst.")
                getraenkNameMenge = "capuccino"
                mengen()
            if auswahlMenge == "4":
                print("Dein flat white wird angepasst.")
                getraenkNameMenge = "flatWhite"
                mengen()
            if auswahlMenge == "5":
                print("Dein Kaffee Latte wird angepasst.")
                getraenkNameMenge = "kaffeeLatte"
                mengen()
            if auswahlMenge == "6":
                print("Dein Latte Macchiato wird angepasst.")
                getraenkNameMenge = "latteMacchiato"
                mengen()
            if auswahlMenge == "7":
                print("Dein Milchschaum wird angepasst.")
                getraenkNameMenge = "Milchschaum"
                mengen()
            if auswahlMenge == "8":
                print("Deine heiße Milch wird angepasst.")
                getraenkNameMenge = "Milch"
                mengen()
            if auswahlMenge == "0":
                print("Zurück zum Hauptmenü.")

## bezüge ausgegeben

        if auswahlEinstell == "3":

# erstellen des dict Containers

            bezug = dict(Espresso=0, Kaffee=0, KaffeeLatte=0, LatteMacchiato=0, Capuccino=0, flatWhite=0, Milchschaum=0,
                         heißeMilch=0)

# Liste aller einzulesenden dateien // sowie container/Variablen

            liste_bezdateien = "bezflatWhite.txt", "bezkaffee.txt", "bezkaffeeLatte.txt", "bezlatteMacchiato.txt", "bezMilch.txt", "bezMilchschaum.txt", "bezespresso.txt", "bezcapuccino.txt"
            inhalt_bez = ""
            b = ""

# öffnen und einlesen aller Dateien in Durchläufen

            for i in range(len(liste_bezdateien)):
#                print(liste_bezdateien[i])
                f = open(liste_bezdateien[i], "r")
                inhalt_bez = f.readlines()
                f.close()

# erstellen der Schlüsselwörter des dict in der variablen b

                if liste_bezdateien[i] == "bezflatWhite.txt":
                    b = "flatWhite"
                if liste_bezdateien[i] == "bezkaffee.txt":
                    b = "Kaffee"
                if liste_bezdateien[i] == "bezkaffeeLatte.txt":
                    b = "KaffeeLatte"
                if liste_bezdateien[i] == "bezlatteMacchiato.txt":
                    b = "LatteMacchiato"
                if liste_bezdateien[i] == "bezMilch.txt":
                    b = "heißeMilch"
                if liste_bezdateien[i] == "bezMilchschaum.txt":
                    b = "Milchschaum"
                if liste_bezdateien[i] == "bezespresso.txt":
                    b = "Espresso"
                if liste_bezdateien[i] == "bezcapuccino.txt":
                    b = "Capuccino"
# löschen der key/value beziehnung und schreiben der neuen key/value durch den eingelesenen wert
                del bezug[b]
                bezug[b] = int(inhalt_bez[0])
            print("Es wurden so viele Bezüge bezogen.")

# sortieren des dict... nicht anhand des key/schlüsselwortes sondern des value/int Wertes
# dies geht auch durch umwandeln in eine liste... ist im programm sortDictionary.py

            print(sorted(bezug.items(), key=lambda kv: kv[1], reverse=True))
            print(sorted(bezug.items(), key=lambda kv: kv[1]))

## werkseinstellungen

        if auswahlEinstell == "4":

# container erstellen aller zu ändernden dateien

            liste_bezdateien = "bezflatWhite.txt", "bezkaffee.txt", "bezkaffeeLatte.txt", "bezlatteMacchiato.txt", "bezMilch.txt", "bezMilchschaum.txt", "bezespresso.txt", "bezcapuccino.txt"
            liste_dateien = "flatWhite.txt", "kaffee.txt", "kaffeeLatte.txt", "latteMacchiato.txt", "Milch.txt", "Milchschaum.txt", "espresso.txt", "capuccino.txt"

            auswahlWerk = input("möchtest Du wirklich alle Einstellungen zurücksetzen ( ja / nein")
            if auswahlWerk == "ja":
                print("Alle Einstellungen wurden zurückgesetzt!")

# zurücksetzen aller bezüge auf null

                for i in liste_bezdateien:
                    print(i)
                    f = open(i, "w")
                    f.write("0")
                    f.close()

# öffnen aller dateien in durchläufen

                for a in liste_dateien:
                    print(a)
                    f = open(a, "r")
                    inhalt_getraenk_werk = f.readlines()
                    f.close()

# durchlaufe aller inhalte der text datei und schreiben in den container getraenk in das lisen-format dict

                    for i in range(len(inhalt_getraenk_werk)):
                        c = inhalt_getraenk_werk[i].split()
                        getraenk[(c[0])] = int(c[1])

# überprüfen der inhalte der text datei und falls vorhanden löschen und ersetzen

                    if "Espresso" in getraenk:
                        espresso = 25
                        del getraenk["Espresso"]
                        getraenk["Espresso"] = espresso
                    if "Kaffee" in getraenk:
                        kaffee = 180
                        del getraenk["Kaffee"]
                        getraenk["Kaffee"] = kaffee
                    if "Milch" in getraenk:
                        milch = 180
                        del getraenk["Milch"]
                        getraenk["Milch"] = milch

# umwandeln des dict in einen string und speichern in der liste_getraenk

                    liste_getraenk = str(getraenk)

# löschen aller nicht benötigter elemente im string // Text cleanen

                    liste_getraenk = liste_getraenk.replace(",", "\n")
                    liste_getraenk = liste_getraenk.replace("{", "")
                    liste_getraenk = liste_getraenk.replace("}", "")
                    liste_getraenk = liste_getraenk.replace(" '", "")
                    liste_getraenk = liste_getraenk.replace("'", "")
                    liste_getraenk = liste_getraenk.replace(":", "")

# schreiben des formatierten Textes in die Datei

                    f = open(a, "w")
                    f.write(liste_getraenk + "\n")
                    f.close()
# löschen des containers getraenk für den nächsten durchlauf, um nur die Zutaten aufzunehmen, die im Getränk vorhanden sind
                    if "Espresso" in getraenk:
                        del getraenk["Espresso"]
                    if "Kaffee" in getraenk:
                        del getraenk["Kaffee"]
                    if "Milch" in getraenk:
                        del getraenk["Milch"]

## zurück zum hauptmenü

        if auswahlEinstell == "0":
            print("zurück zum Hauptmenü")


    weiter = input(nameAnwender + ", möchtest du noch ein Getränk beziehen ( ja / nein ): ")



