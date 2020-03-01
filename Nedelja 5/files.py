# Files

# Zadatak 1
# Iz fajlova brojevi.txt izdvojiti sve dvocifrene i trocifrene brojeve
# i upisati ih u novi fajl odabrani_brojevi.txt

# Zadatak 2
# U fajlu studenti nalazi se lista studenata sa ocjenama za zadati predmet.
# (A - 10, B - 9, C - 8, D - 7, E - 6, F - 5)
# Napisati funkciju koja vraca prosjecnu ocjenu ostvarenu na ispitu.
# E [6 - 6.5), D [6.5, 7.5), C [7.5, 8.5), B [8.5, 9.5), A [9.5, 10]
# Studente koji su dobili ocjenu F ne ukljucivati u prosjek

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