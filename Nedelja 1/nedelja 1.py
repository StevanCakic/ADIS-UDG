'''
print("123")

ime = "Marko"
prezime = "Markovic"
godine = 20
mail = "marko@gmail.com"
print(f"Email adresa korisnika {ime} {prezime} ({godine}) je {mail}")

# Zadatak 2

x = 3
y = 2
rez = 2 * x **y - 2 * (x - y) ** 3
print(f"Rezultat je: {rez}")

# Zadatak 3
import math

print(math.cos(0))
print(math.sin(math.pi / 2))
print(2 ** 0.5)

print("Broj:" + str(10))

# Zadatak 4
# Ako je cijena računara 400e, štampati koliko treba odvojite za plaćanje PDVa
# Štampati rezultat u sledećem formatu:
    # Cijena računara je 400e. Iznos PDVa je {pdv}, a cijena računara bez PDVa je {cijena bez PDVa}

cijena = 400
pdv = 0.21 * cijena

print(f"Cijena racunara je {cijena}e. Iznos PDVa je {pdv}, a cijena racunara bez PDVa je {cijena - pdv}")

# Stringovi

recenica = "Imamo neki proizvoljan string"
print(recenica[0:10:3])
'''

# Conditions

a = True
if a:
    print("Tacno")
else:
    print("Netacno")

a = int(input("Unesite prvi broj:"))
b = int(input("Unesite drugi broj:"))

if a > b:
    print("Prvi broj je veci od drugog")
    c = a + b
elif a < b:
    print("Drugi broj je veci od prvog")
else:
    print("Jednaki brojevi")

c = True if a > b else False
