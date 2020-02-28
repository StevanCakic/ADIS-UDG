# Dictionaries


my_dict = {"ime":"Marko", "prezime":"Markovic", "godine":30}
print(my_dict["ime"])
print(my_dict.get("adresa", "Default vrijednost"))
print(my_dict)
for key in my_dict:
    print(key)

# Testirati metode

'''
    Napisati funkciju koja omogucava korisniku da unese
    n studenata (n parametar funkcije).
    Svaki student se predstavlja kao dictionary oblika:
    {ime, prezime, godina_studija, prosjek}.
    Funkcija treba da vrati listu studenata.
'''
def unos_studenata(broj_studenata):
    lista_studenata = []
    for i in range(0, broj_studenata):
        ime = input(f"Unesite ime {i+1}. studenta:")
        prezime = input(f"Unesite prezime {i+1}. studenta:")
        godina_studija = int(input(f"Unesite godinu studija {i+1}. studenta:"))
        prosjek = float(input(f"Unesite prosjek {i+1}. studenta:"))
        lista_studenata.append({"ime":ime, "prezime": prezime,
                 "godina_studija":godina_studija, "prosjek":prosjek})
    return lista_studenata

#broj_studenata = int(input("Unesite broj studenata:"))
#lista_studenata = unos_studenata(broj_studenata).copy()
#print(lista_studenata)
'''
    Napisati funkciju koja izdvaja one studente ciji je prosjek veci od zadatog.
    Studenti i prosjek se zadaju kao parametari funkcije.
    Funkcija treba da vrati studente koji zadovoljavaju zadati uslov.
    Funkcije testirati
'''

def studenti_koji_zadovoljavaju_prosjek(studenti, prosjek):
    studenti_sa_zadovoljavajucim_prosjekom = []
    for student in studenti:
        if student["prosjek"] > prosjek:
            studenti_sa_zadovoljavajucim_prosjekom.append(student)
    return studenti_sa_zadovoljavajucim_prosjekom

# print(studenti_koji_zadovoljavaju_prosjek(lista_studenata, 9))

# Napomena:
dictionary = {"ime": "A", "prezime": "B"}
if not "adresa" in dictionary:
    dictionary["adresa"] = "Default"


# Skupovi
skup1 = {1,2,3}
skup1.add(4)
skup2 = {2,4,5}
print(skup1.intersection(skup2))

# List comprehension

squares = [i**2 for i in range(1, 101)]
print(squares)

movies = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 
            'The Shawshank Redemption', 'Pulp Fiction']
movies_start_with_the = [movie.upper() for movie in movies if movie.startswith("The")]
print(movies_start_with_the)

movies = [('The Godfather', 1972, "crime"), 
            ('The Wizard of Oz', 1939, "drama"), 
            ('Citizen Kane', 1941, "drama"), 
            ('The Shawshank Redemption', 1994, "drama"),
            ('Pulp Fiction', 1994, "triller")]

# Izdvojiti sve drama filmove (samo title) koji su snimljeni 
# izmedju 1990 i 2000 godine
a = [title for (title, year, genre) in movies if 1990 <= year <= 2000 and genre=="drama"]

# Files