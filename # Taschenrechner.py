# Taschenrechner

print("Das ist mein Taschenrechner! ")

while True:
    print("(1) Addieren")
    print("(2) Subtrahieren")
    print("(3) Multiplizieren")
    print("(4) Dividieren")
    print("(5) Beenden")

    rechenart = int(input("Nenne mir deinen ersten Befehl! 1,2,3,4 oder 5? "))
    if rechenart == 5:
        print("Vorgang beendet! ")
        break
    else:
        False

    eingabe1 = int(input("Nenne mir deine erste Zahl! "))
    eingabe2 = int(input("Nenne mir deine zweite Zahl! "))
    ergebnis = int()

    if rechenart == 1:
        ergebnis += eingabe1 + eingabe2
        print("=", ergebnis)
    elif rechenart == 2:
        ergebnis += eingabe1 - eingabe2
        print("=", ergebnis)
    elif rechenart == 3:
        ergebnis += eingabe1 * eingabe2
        print("=", ergebnis)
    elif rechenart == 4:
        ergebnis += eingabe1 / eingabe2
        print("=", ergebnis)
    else:
        print("Bitte verwende einen gültigen Vorgang! ")
        False

    print("(6) Beenden")
    print("(7) Weitermachen")

    aktion = int(input("Möchtest du den Vorgang beenden oder weitermachen? 6 oder 7? "))

    if aktion == 6:
        print("Vorgang beendet! ")
        break
    else:
        while True:
            weiterrechnen = input("Möchtest du mit deinem Ergebnis weiterrechnen? j/n").lower()

            if weiterrechnen == "j":
                print("(1) Addieren")
                print("(2) Subtrahieren")
                print("(3) Multiplizieren")
                print("(4) Dividieren")

                rechenart2 = int(input("Nenne mir deine Rechenart! 1,2,3 oder 4? "))
                eingabe3 = int(input("Nenne mir deine Zahl! "))

                if rechenart2 == 1:
                    ergebnis = ergebnis + eingabe3
                    print("=", ergebnis)
                elif rechenart2 == 2:
                    ergebnis = ergebnis - eingabe3
                    print("=", ergebnis)
                elif rechenart2 == 3:
                    ergebnis = ergebnis * eingabe3
                    print("=", ergebnis)
                else:
                    ergebnis = ergebnis / eingabe3
                    print("=", ergebnis)
            elif weiterrechnen == "n":
                break
            else:
                print("Bitte antowrte mit 'j' für 'Ja' oder 'n' für 'Nein'! ")

# Hallo