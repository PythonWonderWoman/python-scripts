# sprawdzanie pamieci operacyjnej obiektow
# dla slownikow dictonary
# program pokazuje adresy pamieci naszych obiektow

obiekt = 10
print(id(obiekt))

obiekt = "wartosc tekstowa"
print(id(obiekt))

obiekt = 3.12
print(id(obiekt))

obiekt = True
print(id(obiekt))

obiekt = [
    3,
    22.1,
    "struktura listy, uporzadkowana kolekcja danych zachowujaca kolejnosc wprowadzania",
    ]
print(id(obiekt))

obiekt = (33, "tuple", "krotki", 5.678)
print(id(obiekt))

obiekt = {
    2: "System",
    "B":"Operacyjny",
    5.5:678,
    "Python":"WonderWoman",
    "strktura":"slownika",
    }
print(id(obiekt))
