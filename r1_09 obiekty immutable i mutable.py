# obiekty mutowalne - modyfikowalne np listy, slowniki, klasy zdefiniowane przez uzytkownika
# obiekty immutable - niemodyfikowalne np. str int float bool and tuple

# test modyfikacji obiektu typu str

obiekt = "Python"
print(id(obiekt))

# do obiektu mozemy przyisac inna wartosc
obiekt = "Wonder"
print(id(obiekt))

# mozemy zobaczyc element obiektu
print(obiekt[3])

# ale nie mozemy przypisac nic do elementu obiektu
obiekt[3] = "Python Wonder Woman"
