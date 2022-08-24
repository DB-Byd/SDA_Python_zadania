print("*** Dziwny Integer ***")
print("\nPolecenia:")
print("Mając na wejściu zmienną n typu integer, obsłuż przedstawione poniżej warunki:")
print("- Jeżeli n jest nieparzyste, zwróć napis 'Dziwne'")
print("- Jeżeli n jest parzyste i zawiera się w zakresie od 2 do 5, zwróć napis 'Zwykłe'")
print("- Jeżeli n jest parzyste i zawiera się w zakresie od 6 do 20, zwróć napis 'Dziwne'")
print("- Jeżeli n jest parzyste i jest większe od 20, zwróć napis 'Zwykłe'")

while True:
    n = input("\nPodaj liczbę:\t ")
    n = int(n)
    modulo = n % 2
    if modulo == 0:
        if n >= 2 and n <= 5:
            print("Zwykłe")
            # Tu aż się prosi użyć funkcji, ale z tym pokombinujemy później :))
            exit = input("\nSprawdzamy dalej? t=tak\t")
            if exit == "t":
                continue
            else:
                break
        elif n >= 6 and n <= 20:
            print("Dziwne")
            exit = input("\nSprawdzamy dalej? t=tak\t")
            if exit == "t":
                continue
            else:
                break
        elif n >= 20:
            print("Zwykłe")
            exit = input("\nSprawdzamy dalej? t=tak\t")
            if exit == "t":
                continue
            else:
                break
    else:
        print("Dziwne")
        exit = input("\nSprawdzamy dalej? t=tak\t")
        if exit == "t":
            continue
        else:
            break
