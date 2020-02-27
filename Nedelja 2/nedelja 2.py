# Petlje, nastavak

i = 1
while i <= 10:
    # print(i)
    i = i + 1
    # i += 1

# Naci proizovod brojeva djeljivih sa 3, a ne sa 6 u intervalu od 1 do n (unosi korisnik)
# Ako je proizvod veci od 10 prekinuti izvrsavanje petlje
i = 1
proizvod = 1
n = int(input("Unesite broj n:"))
while i < n:
    if i % 3 == 0 and i % 6 != 0:
        proizvod *= i
    if proizvod > 10:
        break
    i += 1
# print(proizvod)

for j in range(1, 11, 2):
    # print(j)
    pass

lista = [10, 20, 30, "abc", [1,2,3]]
for index, element in enumerate(lista):
    if index % 2 == 0:
        # print(element)
        pass

test_string = "Probni string"
for karakter in test_string:
    # print(karakter)
    pass

# Zadatak 5
# Odraditi i sa for i sa while petljom

'''
    Napisati program koji vraća broj malih i broj velikih slova za zadati string.
    Primjer: upper_lower("Hi Mr. Rober. How are you today?"),
    stampa 19 - broj malih slova, 4 - broj velikih slova. 
    Pomoć: da provjeriti da li je karakter slovo koristiti isalpha metod.
'''
brojac = 0
broj_malih_slova = 0
broj_velikih_slova = 0
ulazni_string = "Hi Mr. Rober. How are you today?"
duzina_stringa = len(ulazni_string)
while brojac < duzina_stringa:
    karakter = ulazni_string[brojac]
    if karakter.isalpha():
        if karakter.isupper():
            broj_velikih_slova += 1
        else:
            broj_malih_slova += 1
    brojac += 1
print(f"Broj malih slova je: {broj_malih_slova}")
print(f"Broj velikih slova je: {broj_velikih_slova}")

broj_malih_slova = 0
broj_velikih_slova = 0
for karakter in ulazni_string:
    if karakter.isalpha():
        if karakter.isupper():
            broj_velikih_slova += 1
        else:
            broj_malih_slova += 1

# Zadatak 6
'''
    Napisati program koji racuna zbir parnih i proizvod neparnih brojeva od 1 do 15
    Takodje, prikazati koliko ima parnih, a koliko neparnih brojeva iz tog segmenta
'''
zbir = 0
proizvod = 1
broj_parnih = 0
broj_neparnih = 0
for i in range(1, 16):
    if i % 2 == 0:
        zbir += i
        broj_parnih += 1
    else:
        proizvod *= i
        broj_neparnih += 1

# Liste

# Prvi dio
# Kreirajmo listu koja sadrži različite tipove podataka
# Isprobajmo indeksiranje i slicing
# Isprobajmo spajanje više listi u jednu
lista_a = [1, 10, "abc", [1, 2, 3]]
lista_b = [2, 3, 7]
# print(lista[-1])
# print(lista_a + lista_b)

for element in lista_a:
    # print(element)
    pass
# print(lista_a[::-1])
print([1,2,3] * 3)
lista = []
for element in [1,2,3]:
    lista.append(element * 3)
# Drugi dio
# Metode za liste
matrica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrica:
    # print(row)
    pass


# Razlika između append i extend
lista_c = [1,2,3]
lista_d = [5, 6]
lista_c.append(lista_d)
print(lista_c)
lista_c = [1,2,3]
lista_c.extend(lista_d)
print(lista_c)

lista_a = [1,2,1,3,1]
print(lista_a.count(1))

# Kreiranje matrice

matrica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for index_1,row in enumerate(matrica):
    for index_2, element in enumerate(row):
        # print(index_1, index_2)
        matrica[index_1][index_2] = 1

# print(matrica)

# Zadatak 7

'''
Naci sumu kvadrata svih neparnih elementa liste
'''
suma = 0
lista = [2,3,7,9]
for element in lista:
    if element % 2 != 0:
        suma = suma + element**2
print(suma)

# Cuvanje po referenci
lista_a = [10, 20, 30]
lista_b = lista_a.copy()
lista_a[0] = 11
lista_b[0] = 7
print(lista_a)
print(lista_b)

# Torke

torka = (1,2)
print(type(torka))

import sys
lista = [1, 2,3,"a","b","c", True, 2.73]
torka = (1, 2,3,"a","b","c", True, 2.73)
print(sys.getsizeof(lista))
print(sys.getsizeof(torka))

import timeit
list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print(f"List time:{list_test}")
print(f"Tuple time:{tuple_test}")

ime, prezime, godine = ("Marko", "Markovic", 20)

# Funkcije

def add_numbers(a=0, b=0):
    return a + b

print(add_numbers(1))

def print_country(country=None):
    if country == None:
        country = "Crna Gora"
    print(country)

print_country("France")

