import random
def create_matrix(n, p):
    matrix = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            if random.random() < p:
                matrix[i][j] = 1
    return matrix

# za grupu g1
def check_position_g1(x, y):
    if matrix[x][y] == 1:
        return False
    if y == 0:
        return 1 if matrix[x][y+1] == 0 else 0
        
    elif y == len(matrix) - 1:
        return 1 if matrix[x][y - 1] == 0 else 0
    else:
        if matrix[x][y-1] + matrix[x][y+1] == 0:
            return 2
        elif matrix[x][y-1] + matrix[x][y+1] == 1:
            return 1
        else:
            return 0

# za grupu g2
def check_position_g2(x, y):
    if matrix[x][y] == 1:
        return False
    if x == 0:
        return 1 if matrix[x+1][y] == 0 else 0
        
    elif y == len(matrix) - 1:
        return 1 if matrix[x-1][y] == 0 else 0
    else:
        if matrix[x-1][y] + matrix[x+1][y] == 0:
            return 2
        elif matrix[x-1][y] + matrix[x+1][y] == 1:
            return 1
        else:
            return 0

dim_matrix = int(input("Unijeti dimenziju kvadratne matrice:"))
vjerovatnoca = float(input("Unesite vjerovatnocu sa kojom se pojavljuje 1 u matrici:"))
matrix = create_matrix(dim_matrix, vjerovatnoca)
print(matrix)

broj_nula_u_matrici = 0
for i in range(dim_matrix):
        for j in range(dim_matrix):
            if matrix[i][j] == 0:
                broj_nula_u_matrici += 1

score = 0
while True:
    vrsta = int(input("Odaberite vrstu:"))
    kolona = int(input("Odaberite kolonu:"))
    broj_nula_oko_elementa = check_position_g1(vrsta, kolona) # za gore i dolje, g2 funkcija
    if broj_nula_oko_elementa == False:
        print(f"Izgubili ste igru,a rezultat koji ste ostvarili je {score}")
        break
    else:
        score += 1
        print(f"Odabrali ste 0. Oko elementa koji ste odabrali ima {broj_nula_oko_elementa} nula. Trenutni score: {score}")
        if score == broj_nula_u_matrici:
            print(f"Pobijedili ste, a rezultat koji ste ostvarili je {score}")
            break