# Srednja vrijednost
def average(lista):
    suma = 0
    for element in lista:
        suma += element
    return suma / len(lista)

# Standardna devijacija (za G2 samo ukloniti ** 0.5 iz return)
def standard_dev(lista, average, n):
    suma = 0
    for element in lista:
        suma += (element - average) ** 2
    return (suma / (n-1)) ** 0.5

lista = [1,2,3,4,5]
avg = average(lista)
print(avg)
print(standard_dev(lista, avg, len(lista) ))