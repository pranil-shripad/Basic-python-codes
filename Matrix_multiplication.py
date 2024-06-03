matA = [[1,2,3],
        [4,5,6],
        [7,8,9]]
matB = [[1,2,3],
        [4,5,6],
        [7,8,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(matA)):
    for j in range(len(matB[0])):
        for k in range(len(matB)):
            result[i][j] += matA[i][k] * matB[k][j]
            
for elements in result:
    print(elements)