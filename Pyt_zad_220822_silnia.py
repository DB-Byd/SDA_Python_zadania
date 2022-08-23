print("\n*** Program obilczający silnię podanej liczby ***")

while True:
    a = 1
    n = input('\nPodaj liczbę lub wpisz "q" aby zakończyć: \t')
    if n == "q":
        break
    else:
        n = int(n)
        for number in range(a,n + 1):
            a = (a) * number
            # print(a)
        print("Silnia liczby", n, "to", a)




