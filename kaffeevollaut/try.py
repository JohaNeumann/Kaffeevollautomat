
bezug = dict(Espresso=0, Kaffee=0, KaffeeLatte=0, LatteMacchiato=0, Capuccino=0, flatWhite=0, Milchschaum=0, heißeMilch=0)

liste_bezdateien = "bezflatWhite.txt", "bezkaffee.txt", "bezkaffeeLatte.txt", "bezlatteMacchiato.txt", "bezMilch.txt", "bezMilchschaum.txt", "bezespresso.txt", "bezcapuccino.txt"
inhalt_bez = ""
b = ""

for i in range(len(liste_bezdateien)):
    print(liste_bezdateien[i])
    f = open(liste_bezdateien[i], "r")
    inhalt_bez = f.readlines()
    f.close()
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
    del bezug[b]
    bezug[b] = int(inhalt_bez[0])
    print(sorted(bezug.items(), key=lambda kv: kv[1], reverse=True))
    print(sorted(bezug.items(), key=lambda kv: kv[1]))
