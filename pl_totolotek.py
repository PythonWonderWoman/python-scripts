#! /usr/bin/env python3

#author: python.wonder.woman@gmail.com
#wersja PL

#######--------------------------NOTES FROM AUTHOR-----------------------------------#######
#      Celem tego skryptu jest mozliwosc odgadniecia liczby z zakresu 1-49 przez uzytkownika.
#      Skrypt przewiduje, gdy uzytkownik wpisal zbyt niska lub zbyt wysoka dozwolona wartosc.
#      Użytkownik ma 6 szans aby odgadnac te wlasciwa liczbe.
#      Wybory uzytkownika zapisywane sa do listy i nastepnie wyswietlone.
#      Skrypt nie ostrzega uzytkownika, gdy ten ponownie wybral te sama liczbe.
#      To tylko cwiczenie, ktore pozwala mi utrwalic wiedze :)
#######-------------------------------------------------------------------------------#######

# coding: utf-8

import random

liczba = random.randint(1, 49)
twoje_liczby = []

# print(liczba)
for i in range(6):
    print("Proba: ", i + 1)
    uzytkownik_zgaduje = input("Zgadnij liczbę w przedziale od 1 do 49\n")
    twoje_liczby.append(uzytkownik_zgaduje)
    if int(uzytkownik_zgaduje) < 1:
        print("0 nie jest dozwolone w tym przedziale. Uzyj innej liczby")
    elif int(uzytkownik_zgaduje) > 49:
        print("Liczby powyzej 49 nie sa dozwolone. Uzyj innej liczby")
    else:
        if liczba == int(uzytkownik_zgaduje):
            print("Gratulacje, zgadles liczbe, udaj sie do punktu lotto po odbior nagrody.")
            break
        else:
            print("Tym razem nie zgadles, nie poddawaj sie i sprobuj ponownie!")
            print()

print("Twoje wybory byly nastepujace: ", twoje_liczby)