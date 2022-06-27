
# erstellen einer funktion, um durch sort den zweiten wert zu sortieren...

def zweitesElement(elem):
    return elem[1]

# erstellen der container

bezug = dict(Espresso=250, Kaffee=100, KaffeeLatte=200, LatteMacchiato=30, Capuccino=3000, flatWhite=10, Milchschaum=980, heißeMilch=40)
liste = []

# um nicht nur die schlüsselwörter sondern auch die Werte erfassen zu können,
# lassen wir uns mit items den gesamten inhalt von bezug ausgeben und speichern ihn in einer liste.
# da wir die zumannenhänge von key und value nicht verlieren wollen und wir mit dem befehl append immer nur ein element
# hinzufügen können , speichern wir key and value immer in einer neuen liste in der liste

for key, value in bezug.items():
    print(key, value)
    liste.append((key, value))
print(liste)
# überprüfung des type, ob die zahl auch als zahl und nicht als string ausgegeben wurde.
print(type(liste[0][1]))
sorted(liste)
# um nun die in der liste enthaltenen listen, nach ihrem Zahlenwerten zu sortieren, stellen wir als key
# die funktion zweitesElement ein
liste.sort(key=zweitesElement)
print(liste)
liste.sort(key=zweitesElement, reverse=True)
print(liste)

# eine andere verkürzte schreibweise mit anonymer Funktion lambda

print(sorted(bezug.items(), key=lambda kv: kv[1], reverse=True))
print(sorted(bezug.items(), key=lambda kv: kv[1]))

