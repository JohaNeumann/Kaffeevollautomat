
liste_bezdateien = "bezflatWhite.txt", "bezkaffee.txt", "bezkaffeeLatte.txt", "bezlatteMacchiato.txt", "bezMilch.txt", "bezMilchschaum.txt", "bezespresso.txt", "bezcapuccino.txt"
liste_dateien = "flatWhite.txt", "kaffee.txt", "kaffeeLatte.txt", "latteMacchiato.txt", "Milch.txt", "Milchschaum.txt", "espresso.txt", "capuccino.txt"
getraenk = dict()

for i in liste_bezdateien:
    print(i)
    f = open(i, "w")
    f.write("0")
    f.close()
for a in liste_dateien:
    print(a)
    f = open(a, "r")
    inhalt_getraenk_werk = f.readlines()
    f.close()
    for i in range(len(inhalt_getraenk_werk)):
        c = inhalt_getraenk_werk[i].split()
        getraenk[(c[0])] = int(c[1])
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

    liste_getraenk = str(getraenk)
    liste_getraenk = liste_getraenk.replace(",", "\n")
    liste_getraenk = liste_getraenk.replace("{", "")
    liste_getraenk = liste_getraenk.replace("}", "")
    liste_getraenk = liste_getraenk.replace(" '", "")
    liste_getraenk = liste_getraenk.replace("'", "")
    liste_getraenk = liste_getraenk.replace(":", "")

    f = open(a, "w")
    f.write(liste_getraenk + "\n")
    f.close()

    if "Espresso" in getraenk:
        del getraenk["Espresso"]
    if "Kaffee" in getraenk:
        del getraenk["Kaffee"]
    if "Milch" in getraenk:
        del getraenk["Milch"]
