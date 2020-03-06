# Matrice

matrix = [[0 for i in range(0, 3)] for j in range(0, 3)]
# print(matrix)
suma = 0
matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in enumerate(matrix):
    index_1 = row[0]
    for index_2 in range(len(row[1])):
        if index_1 == index_2:
            suma += matrix[index_1][index_2]
        
print(suma)
l = [3,2,1,4]
l.sort(reverse=True)
print(l)