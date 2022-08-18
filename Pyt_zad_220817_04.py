# Przed analizą kodu proszę uruchomić program - będzie lepsza zabawa :)
# Taką mam nadzieję.

# Warunki zadania:

# Definiowanie listy l1
l1 = ["K", "A", "U", "B", "R", "E", "W", "T", "A", "R", " ", "O", "A", "K", "W", "O", "R", "I", "U", "A", "K", "O"]

# Definiowanie listy l2
l2 = ["!", "R", "A", "!", "P", "Q", "!", "G", "A", "Ć", "F", "B", "A", "Q", "G", "M"]

# Przetwarzanie drogi l1:
# Identyfikowanie indeksu elementu znajdującego się w połowie listy:
l1_ind_mid = len(l1)//2

# Tworzenie nowej listy z wycinka listy l1 i co drugiego elementu:
l1_wyc = l1[:l1_ind_mid:2]


# Przetwarzanie drogi l2:
# Odwrócenie listy l2:
l2.reverse()

# Tworzenie nowej listy z co trzeciego elementu:
l2_wyc = l2[::3]


# Tworzenie drogi z połączenia przetworzonych list:
l3_haslo = l1_wyc + l2_wyc

# Dalej idzie zabawa w programowanie:

# Zamierzam wyświetlić drogę (w tym przypadku hasło), zatem trzeba przekształcić 
# listę w string.
# https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python

haslo = ' '.join(l3_haslo)

# Teraz będą wyświetlane komunikaty, ale sukcesywnie, z pewnym opóźnieniem.
# https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code
import time

print("\n\nZadanie 4 - Droga ucieczki inaczej! :)")
time.sleep(2)

print('"Seksmisja", scena z windą.\n')
time.sleep(2)

print('Narrator:\nMax i Albert uciekają. Pomaga im Lamia.\nNiestety winda nie chce ruszyć...')
time.sleep(2)

print("\nLamia:")
time.sleep(1)
print("- Dlaczego właz nie zjeżdża w dół?")
time.sleep(1)
print("- Co jest? Co się stało? Dlaczego to nie zjeżdża!")
time.sleep(1)
print("- Pewnie dały nie ten klucz!")
time.sleep(2)

print("\nStrażniczka:")
time.sleep(1)
print("- Klucz nie wystarcza. Potrzebne akustyczne hasło.")
time.sleep(2)

print("\nLamia:")
time.sleep(1)
print("- Jakie hasło?")
time.sleep(2)

print("\nStrażniczka:")
time.sleep(1)
print("- Nie mamy pojęcia!")
time.sleep(1)
print("- Hasło zna tylko Jej Ekscelencja!")
time.sleep(2)

print("\nAlbert:")
time.sleep(1)
print("- Dlaczego nas nie chcą wypuścić, żebyśmy tam sobie spokojnie umarli...")
time.sleep(2)

print("\nMaks:")
time.sleep(1)
print("- Wszystko przepadło...")
time.sleep(2)

print("-", haslo)
time.sleep(1)

print("\nNarrator:")
time.sleep(1)
print("Ups!")
time.sleep(1)
print("Wywalą programistę z tego harcerstwa! :)")
time.sleep(1)
print("Trzeba ratować sytuację: ")
time.sleep(1)
print("- To nie on!!! To taki scenariusz!!! ;)")
time.sleep(2)
print("\nA tymczasem:")
time.sleep(2)
print("WINDA ZACZYNA ZJEŻDŻAĆ!\n\n")
time.sleep(2)

# Wyjaśnienie zadania dla widzów

print("Co takiego wykombinował Maks?\n")
time.sleep(1)
print("Otóż w kaloszu, w siedlisku Dekadencji, znalazł dwie listy:\n")
time.sleep(1)
print("Listę l1:\n", l1)
time.sleep(1)
print("\ni listę l2:\n", l2)
time.sleep(1)
print('\nA w butelce "nasi" zostawili mu algorytm:\n')
time.sleep(1)
print("- Podziel listę l1 na pół i z pierwszej połowy weź co drugi element.")
time.sleep(1)
print("\nWyszła taka lista:\n", l1_wyc)
time.sleep(1)
print("\n- Drugą listę odwróć i wybierz z niej co trzeci element." )
time.sleep(1)
print("\nWyszło coś takiego:\n", l2_wyc )
time.sleep(1)
print("\n- Następnie połącz listy i otrzymasz tajne hasło.")
time.sleep(1)
print("\nWyszła taka lista z hasłem:\n", l3_haslo)
time.sleep(2)
print("\nA teraz najważniejsze pytanie:")
time.sleep(2)
print("\nStrażniczka:")
time.sleep(1)
print("- A co to znaczy?")
time.sleep(2)

print("\n\nWrażliwych oczywiście przepraszam!\nNa co dzień tak nie szaleję! ;)")
time.sleep(2)
print("\nBye!!! :))))")
time.sleep(2)
print("\nTHE END\n\n\n\n")
time.sleep(3)
