print("\n*** Łączenie, sortowanie i odwracanie list: ***\n")

l1 = [11, 8, 7, 10, 6, 9]
print("Lista l1: ", l1)
l2 = [1, 3, 2, 4, 5]
print("Lista l2: ", l2)
l3 = l1 + l2
print("Lista l3 - połączone listy l1 i l2:", l3)

l3.sort()
print("Posortowana lista l3:", l3, "\n")

print("Zadanie 1, odwracanie list.\n")
# https://datagy.io/python-reverse-list/

reversed_01 = l3
reversed_01.reverse()
print("Lista l3 odwrócona 1. sposobem:", reversed_01)

reversed_02 = list(reversed(l3))
print("Lista l3 odwrócona 2. sposobem:", reversed_02)

reversed_03 = reversed_02[::-1]
print ("Lista l3 odwrócona 3. sposobem:", reversed_03)

slicer = slice(None, None, -1)
reversed_04 = reversed_03[slicer]
print ("Lista l3 odwrócona 4. sposobem:", reversed_04)

reversed_05 = []
for item in reversed(reversed_04):
    reversed_05.append(item)
print ("Lista l3 odwrócona 5. sposobem:", reversed_05)

reversed_06 = [reversed_05[i] for i in range(len(reversed_05) - 1, -1, -1)]
print ("Lista l3 odwrócona 6. sposobem:", reversed_06)


print("\nZadanie 2, sprawdzanie obecności elementu na liście.\n")
print("Zabawa w sprawdzanie obecności liczby na liście.")
print("Program sprawdza, czy podana przez użytkownika liczba znajduje")
print("się na używanej wcześniej liście l3.")
print("Wynik ma zwrócić wartość True/False.")

while True:
    print('\nAby zakończyć naciśnij "q"')
    liczba = input("Podaj liczbę: ")
    if liczba == "q":
        break
    else:
        if int(liczba) in reversed_06:
            check = True
        else:
            check = False
        print(check)    
print("\n**** Dzięki za klikanie :))) ****\n\n")
