

wasser = []
milch = []
bohnen = []

nameAnwender = input("Gib bitte deinen Namen ein: ")
print("Hallo " + nameAnwender + ", gib bitte ein was Du befuellen möchtest"
                                "1 = Milch, 2 = Wasser, 3 = Bohnen.")
auswahl = input("Gib bitte eine Zahl ein: ")

if auswahl == "1":
    print("Der Milchvorrat wurde aufgefüllt.")
    f = open("milchvorrat.txt", "w")
    f.write("1000")
    f.close()

if auswahl == "2":
    print("Der Wasserbehälter wurde aufgefüllt.")
    f = open("wasser.txt", "w")
    f.write("1000")
    f.close()

if auswahl == "3":
    print("Der Bohnenbehälter wurde aufgefüllt.")
    f = open("bohnen.txt", "w")
    f.write("1000")
    f.close()



