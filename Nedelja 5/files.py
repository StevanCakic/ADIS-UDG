# Files
'''
f = open("test.txt")
print(f.read())
print(f.read())

f.seek(0)
print(f.read())
print("***********")
f.seek(0)
for line in f:
    print(line)
f.close()

f = open("test.txt", mode="a")
f.write("\nNovi tekst iz Pythona\n")
f.close()

with open("test.txt") as file:
    print(file.read())

import os


if os.path.exists("./fajlovi/test.txt"):
    os.remove("./fajlovi/test.txt")

for file in os.listdir("./fajlovi"):
    os.remove("./fajlovi/" + file)
os.rmdir("fajlovi")
'''
# Zadatak 1
# Iz fajla brojevi.txt izdvojiti sve dvocifrene i trocifrene brojeve
# i upisati ih u novi fajl odabrani_brojevi.txt

'''
dvocifreni_trocifreni = []
with open("brojevi.txt") as brojevi:
    lines = brojevi.read().split("\n")
    print(lines)
    for line in lines:
        if 1 < len(line) < 4:
            dvocifreni_trocifreni.append(line)
print(dvocifreni_trocifreni) 

with open("odabrani_brojevi", mode="w") as new_file:
    for broj in dvocifreni_trocifreni:
        new_file.write(broj + "\n")
'''

# Zadatak 2
# U fajlu studenti nalazi se lista studenata sa ocjenama za zadati predmet.
# (A - 10, B - 9, C - 8, D - 7, E - 6, F - 5)
# Napisati funkciju koja vraca prosjecnu ocjenu ostvarenu na ispitu.
# E [6 - 6.5), D [6.5, 7.5), C [7.5, 8.5), B [8.5, 9.5), A [9.5, 10]
# Studente koji su dobili ocjenu F ne ukljucivati u prosjek
suma = 0
broj_studenata = 0
prosjek = 1
with open("studenti.txt") as fajl:
    lines = fajl.read().split("\n")
    
    for line in lines:
        student_info = line.split()
        print(student_info)
        if student_info[2] == "A":
            suma += 10
            broj_studenata +=1
        elif student_info[2] == "B":
            suma += 9
            broj_studenata +=1
        elif student_info[2] == "C":
            suma += 8
            broj_studenata +=1
        elif student_info[2] == "D":
            suma += 7
            broj_studenata +=1
        elif student_info[2] == "E":
            suma += 6
            broj_studenata +=1
    prosjek = suma / broj_studenata

print(prosjek)

# Zadatak 3

# Kreirati fajl movies.txt u kome se svaki film, pojedinacno, cuva u jednom redu,
# tj. ako imate unos od 5 filmova, fajl treba da sadrzi 5 linija. 
# Takodje, svaki film je opisan: nazivom, ocjenom, godina izlaska i zanrovima
    # Atributi filma odvojeni su sa ;
    # Naziv filma ne smije da ima vise od 50 karaktera, a ne manje od 2
    # Naziv filma pocinje sa velikim slovom
    # Ocjene su zaokruzeni float brojevi (od 1 do 10) na dvije decimale
    # Film moze da ima vise od jednog zanra, zanrovi su razdvojeni zarezima 

# Potrebno je izdvojiti/prikazati sve filmove cija je ocjena veca od unijete i 
# ciji je zanr filma odgovara unijetom zanru. Omoguciti i pretragu po
# nazivu filma (pocetni term)
# Pomoc: Ponuditi kurisniku dvije opcije, tj. po cemu zeli da filtrira filmove
# a) po ocjena + zanr
# b) naziv (term)
# Preporuka, koristiti list comprehension, funkcija za konverziju stringa u torku je tuple
# Hint: tup = tuple(some_str.split(",")) - konvertuje npr. "abcd,abbccd" -> ("abcd","abbccd")

# Zadatak 4

# Nakon filtriranja filmova, omoguciti korisniku da doda novi film (ne dozvoliti da unese pogresan)
# Npr. postavite mu pitanje, da li zelite da dodate novi film, pa nakon uspjesnog dodavanja
# opet pitate korisnika da li zelite da dodate novi film, i to treba da se ponavlja sve dok ne kaze "ne"
# Nove filmove dodati u postojeci fajl.